import uuid
from re import findall
from .StepResult import StepResult
from .s3 import S3Client


class WorkflowDataManager(object):
    def __init__(self, workflow: dict):
        super().__init__()
        self.__uuid = str(uuid.uuid1())
        self.__workflow = workflow
        self.__parameters = {}
        self.__steps = []
        self.__connections = {}
        self.__templates = {}
        self.__config = {}

        self.__init_parameters()
        self.__init_config()
        self.__init_connection_requirements()

    def __init_parameters(self):
        if 'parameters' in self.__workflow:
            self.__parameters = self.__workflow['parameters']

    def __init_config(self):

        self.__config = {
            'continue_on_error': False,
            'max_parallel_jobs': 3,
            'delete_workflow_log': False
        }

        if 'configuration' in self.__workflow:
            if 'continue_on_error' in self.__workflow['configuration']:
                self.__config['continue_on_error'] = self.__workflow['configuration']['continue_on_error']

        if 'max_parallel_jobs' in self.__workflow['configuration']:
            self.__config['max_parallel_jobs'] = int(self.__workflow['configuration']['max_parallel_jobs'])

        if 'delete_workflow_log' in self.__workflow['configuration']:
            self.__config['delete_workflow_log'] = self.__workflow['configuration']['delete_workflow_log']

    def __init_connection_requirements(self):

        if 'requirements' in self.__workflow and 'connections' in self.__workflow['requirements']:
            for conn in self.__workflow['requirements']['connections']:
                if 'type' not in conn or 'name' not in conn:
                    raise Exception('The connection must have a type and name.')

                connection = {
                    'name': conn['name'],
                    'type': conn['type'],
                    'connection': None
                }

                if conn['type'] == 's3':
                    access_key = self.match_from_parameters(conn['params']['access_key'])
                    secret_key = self.match_from_parameters(conn['params']['secret_key'])
                    endpoint = self.match_from_parameters(conn['params']['endpoint'])
                    bucket = self.match_from_parameters(conn['params']['bucket'])

                    connection['connection'] = S3Client(access_key=access_key, secret_key=secret_key, endpoint=endpoint,
                                                        bucket=bucket)
                    self.__connections[connection['name']] = connection

                else:
                    raise Exception(f"Connection type {conn['type']} not supported.")

    def match_from_parameters(self, value: str):

        res = self.parse_match(value).get_param_changed()
        if len(res) == 0:
            return value
        return res[0].get('default')

    def get_workflow_name(self):
        return self.__workflow.get('name', 'UnName')

    def get_workflow_type(self):
        return self.__workflow.get('type', None)

    def get_config(self) -> dict:
        '''
        Returns a COPY of the workflow configuration
        :return: dictionary containing the workflow configuration
        '''
        return self.__config.copy()

    def get_jobs_requirement(self) -> list:
        if 'requirements' in self.__workflow and 'jobs' in self.__workflow['requirements']:
            return self.__workflow['requirements']['jobs']
        return []

    def get_identifier(self):
        return self.__uuid

    def get_connection(self, identifier: str):
        connection = self.__connections.get(identifier, None)
        if connection:
            return connection['connection']
        return None

    def get_max_parallel_jobs(self):
        return self.__config.get('max_parallel_jobs', 3)

    def get_connections(self):
        return self.__connections

    def get_workflow(self):
        return self.__workflow

    def get_templates(self):
        return self.__templates

    def get_parameters(self) -> dict:
        return self.__parameters

    def get_workflow_steps(self) -> list:
        return self.__workflow.get('steps', [])

    def get_result_steps(self) -> list:
        '''
        Returns a COPY list of dictionaries with the result of the workflow steps
        :return: List of COPY dictionaries with the result of the workflow steps
        '''
        return self.__steps.copy()

    def append_result_step(self, step):
        self.__steps.append(step)

    def parse_match(self, value):
        return InsulaParamFilter(value, self)

    def translate_values(self, param) -> list[StepResult]:

        job_results = []
        for value in [param['values']] if isinstance(param['values'], str) else param['values']:
            ipf = self.parse_match(str(value))
            if ipf.has_match():
                job_results.extend(
                    ipf.get_param_changed()
                )
            else:
                job_results.append(StepResult(default=value, type='single'))

        return job_results


# TODO: va riscritta tutta... che cosa orrenda e cambiata di posizione... tutto...tutto...
class InsulaParamFilter(object):
    __result_pattern = '\\${(.*?)}'

    def __init__(self, value, wfm: WorkflowDataManager):
        super().__init__()
        self.__value = value
        self.__all_match = findall(self.__result_pattern, value)
        self.__has_match = len(self.__all_match) > 0
        self.__wfm = wfm

        self.__match_dot_split = []
        if self.__has_match:
            self.__match_dot_split = self.__all_match[0].split('.')

    def has_match(self) -> bool:
        return self.__has_match

    def get_base_id(self) -> str:
        return self.__match_dot_split[2]

    def has_step_output(self) -> bool:
        return len(self.__match_dot_split) == 4

    def get_step_output(self):
        if len(self.__match_dot_split) == 4:
            return self.__match_dot_split[3]
        return None

    def get_param_changed(self) -> list[StepResult]:

        if not self.__has_match or len(self.__match_dot_split) <= 2:
            return []

        if self.__match_dot_split[0] == 'workflow' and self.__match_dot_split[1] == 'step':

            return FilterResulter.get_from_results(self, self.__value, self.__wfm.get_result_steps())
        elif self.__match_dot_split[0] == 'status' and self.__match_dot_split[1] == 'step':

            return Runtime.get_runtime_info(self, self.__wfm.get_result_steps())
        elif self.__match_dot_split[0] == 'workflow' and self.__match_dot_split[1] == 'param':

            return FilterResulter.get_from_parameters(self, self.__wfm.get_parameters())
        else:
            return []


class Runtime(object):
    @staticmethod
    def get_runtime_info(ipf: InsulaParamFilter, global_parameters: list):

        step_id = ipf.get_base_id()
        for step_results in global_parameters:
            if step_id == step_results['name']:
                out = ipf.get_step_output()
                if out is not None and out in step_results['status']:
                    return [StepResult(default=step_results['status'][out], output_id=out, type='status')]

        return []


class FilterResultName:
    __result_filter_pattern = '\\$\\[(.*?)]'

    def __init__(self, raw: str):
        self.__filters = findall(self.__result_filter_pattern, raw)

    def has_filters(self):
        return len(self.__filters) > 0

    def get_filters(self):
        return self.__filters

    def filter(self, filename):
        if self.has_filters():
            for filter_in in self.__filters:
                res = findall(filter_in, filename)
                if len(res) > 0:
                    return True
        return False


class FilterResulter(object):

    @staticmethod
    def get_from_parameters(ipf: InsulaParamFilter, global_parameters: dict) -> list[StepResult]:
        values = []
        a = ipf.get_base_id()
        if a not in global_parameters:
            return values

        gp = global_parameters[a]
        if isinstance(gp, str):
            return [StepResult(default=gp, type='param')]
        elif isinstance(gp, list):
            for v in gp:
                values.append(StepResult(default=v, type='param'))

        return values

    @staticmethod
    def get_from_results(ipf: InsulaParamFilter, raw, global_results: list) -> list[StepResult]:
        values = []
        ipf_filters = FilterResultName(raw)
        for step_results in global_results:
            if ipf.get_base_id() == step_results['name']:
                for step_result in step_results['results']:
                    if ipf.has_step_output() and step_result.get('output_id') != ipf.get_step_output():
                        continue

                    if ipf_filters.has_filters():
                        if ipf_filters.filter(step_result.get('default')):
                            values.append(step_result)
                    else:
                        values.append(step_result)

        return values
