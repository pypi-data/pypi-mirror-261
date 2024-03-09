import yaml
from .InsulaApiConfig import InsulaApiConfig
from .InsulaWorkflowStep import InsulaWorkflowStep
from .InsulaJobStatus import InsulaJobStatus
from .InsulaFilesJobResult import InsulaFilesJobResult
from .InsulaWorkflowStepRunner import InsulaWorkflowStepRunner
from .WorkflowDataManager import WorkflowDataManager


class InsulaWorkflow(object):

    def __init__(self, insula_config: InsulaApiConfig, workflow: str, parameters: dict = None):
        super().__init__()
        self.__insula_api_config = insula_config

        self.__wfm = WorkflowDataManager(yaml.safe_load(workflow))
        self.__steps_order = []
        self.__validate_version()
        self.__get_workflow_info()
        self.__load_templates()
        self.__update_templates()
        self.__check_parameters_and_add_external(parameters)
        self.__init_job_requirements()

    def __load_templates(self):

        workflow_wfm = self.__wfm.get_workflow()
        templates_wfm = self.__wfm.get_templates()

        if 'templates' in workflow_wfm:
            for template in workflow_wfm['templates']:
                if 'name' in template:
                    templates_wfm[template['name']] = template

    @staticmethod
    def __update_existing_param(template_param: list, step_param: list):
        for template in template_param:
            template_name = template['name']
            find_param = False
            for step in step_param:
                step_name = step['name']
                if template_name == step_name:
                    find_param = True
                    break

            if not find_param:
                step_param.append(template)

    # TODO: questo metodo e' senza parole, va sistemato
    def __update_templates(self):

        workflow_wfm = self.__wfm.get_workflow()
        templates = self.__wfm.get_templates()

        to_jump = ['name']
        if 'templates' in workflow_wfm:
            for steps in self.__steps_order:
                for step in steps:
                    if 'template' in step:
                        if step['template'] in templates:
                            template = templates[step['template']]

                            for key, value in template.items():
                                if key not in to_jump:
                                    if key not in step:
                                        step[key] = value
                                    else:
                                        if key == 'params':
                                            self.__update_existing_param(value, step[key])
                        else:
                            raise Exception(f'Template {step["template"]} not found')

    def __validate_version(self):

        workflow_wfs = self.__wfm.get_workflow()

        if 'version' not in workflow_wfs:
            print('This workflow requires insulaClient version 0.0.1')
            exit(1)
        self.__version = workflow_wfs['version']
        if self.__version != 'beta/1':
            print('Version not compatible with beta/1')
            exit(1)

    # TODO: remove from here and move in WorkflowDataManager
    def __check_parameters_and_add_external(self, parameters):

        parameters_wfm = self.__wfm.get_parameters()

        if parameters is not None and isinstance(parameters, dict):
            for key, value in parameters.items():
                parameters_wfm[key] = value

        for key, value in parameters_wfm.items():
            if isinstance(value, str):
                pass
            elif isinstance(value, list):
                for v in value:
                    if not isinstance(v, str):
                        raise Exception(f'Parameter {key} format type not supported')
            else:
                raise Exception(f'Parameter {key} format type not supported')

    def __get_workflow_info(self):

        self.__name = self.__wfm.get_workflow_name()
        self.__type = self.__wfm.get_workflow_type()

        for step in self.__wfm.get_workflow_steps():
            self.__steps_order.append(InsulaWorkflowStep(step))

    def __init_job_requirements(self):

        for requirement in self.__wfm.get_jobs_requirement():
            job_id = self.__wfm.match_from_parameters(str(requirement['id']))
            # TODO: the step_resoult should be a class
            run = {
                'name': requirement['name'],
                'service_id': 0,
                'status': {
                    "config_id": 0,
                    "job_id": job_id,
                    "status": "REQUIREMENTS_RETRIEVED"
                },
                'results':
                    InsulaFilesJobResult(self.__insula_api_config).get_result_from_job(job_id)
            }

            self.__wfm.append_result_step(run)

    def __filter_log_properties(self):
        to_save = {
            'workflow': self.__wfm.get_workflow(),
            # 'parameters': self.__wfm.get_parameters(),
            # 'requirements': self.__wfm.get_requirements(),
            'steps': self.__wfm.get_result_steps(),
        }

        return to_save

    def run(self) -> WorkflowDataManager:

        config_wfm = self.__wfm.get_config()

        print(f'configuration: {config_wfm}\n')
        print('Running...\n')

        insula_job_status = InsulaJobStatus()
        insula_job_status.set_job_id(f'wf_{self.__name}')
        insula_job_status.set_properties(self.__filter_log_properties()).save()

        try:
            for step in self.__steps_order:
                print(f'running... step: Step: {step}')
                _ = InsulaWorkflowStepRunner(
                    self.__insula_api_config,
                    step,
                    self.__wfm
                )
                results = _.run()
                for result in results['results']:
                    self.__wfm.append_result_step(result['run'])
                insula_job_status.set_properties(self.__filter_log_properties()).save()

                if results['error']:
                    if not config_wfm['continue_on_error']:
                        raise Exception('there is an error, check the pid file')

            if config_wfm['delete_workflow_log']:
                insula_job_status.remove()

            return self.__wfm

        except Exception as error:
            insula_job_status.set_job_error('ERROR', error).save()
            raise Exception(error)
