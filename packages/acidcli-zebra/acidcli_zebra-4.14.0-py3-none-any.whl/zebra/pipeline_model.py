# Copyright Capgemini Engineering B.V.

"""Gitlab CI interface."""
from types import SimpleNamespace

import i18n
import yaml
from loguru import logger

from zebra.exceptions import CLIError


# pylint: disable=too-few-public-methods
class PipelineModel:
    """PipelineModel interface class."""

    __unsupported_attributes = [
        "extends",
        "before_script",
        "after_script",
        "hooks",
        "inherit",
        "services",
        "trigger",
    ]

    def __init__(self):
        """Init PipelineModel class."""
        self.__pipeline = None
        self.stages = []
        self.__pipeline = self.__load_pipeline_with_included_pipelines()
        self.__replace_variables()
        self.__create_model()

    def __create_model(self):
        for stage_name in self.__pipeline["stages"]:
            jobs = []
            for possible_job in self.__pipeline:
                try:
                    job_stage = self.__pipeline[possible_job]["stage"]
                    job_tag = self.__pipeline[possible_job]["tags"][0]
                    image = self.__pipeline[possible_job]["image"]
                    script = self.__pipeline[possible_job]["script"]
                    unsupported_attributes = self._get_unsupported_attributes(
                        self.__pipeline, possible_job
                    )
                except KeyError:
                    pass
                except TypeError:
                    pass
                else:
                    if job_stage == stage_name:
                        self.__create_job_and_add_to_list(
                            image,
                            job_tag,
                            jobs,
                            possible_job,
                            script,
                            unsupported_attributes,
                        )

            self.stages.append(SimpleNamespace(name=stage_name, jobs=jobs))

    def _get_unsupported_attributes(self, pipeline, job):
        """Get unsupported attributes.

        Checks if job contains unsupported attributes.
        Will also check "default" tag in pipeline definition since it will interpolate with all jobs.

        :param pipeline: pipeline to look into
        :param job: job to analyze
        :return: list with unsupported attributes in job
        """
        unsupported_attributes = []

        for attribute in pipeline[job]:
            if attribute in self.__unsupported_attributes:
                unsupported_attributes.append(attribute)

        if "default" in self.__pipeline:
            for attribute in self.__pipeline["default"]:
                if attribute in self.__unsupported_attributes:
                    if attribute not in unsupported_attributes:
                        unsupported_attributes.append(attribute)

        return unsupported_attributes

    @staticmethod
    def __create_job_and_add_to_list(
        image, job_tag, jobs, possible_job, script, unsupported_attributes
    ):
        """Create job and add to list.

        Determine the correct docker engine and add job to list
        """
        engine = None
        if "linux_docker" in job_tag:
            engine = "linux"
        elif "windows_docker" in job_tag:
            engine = "windows"
        if engine:
            job = SimpleNamespace(
                name=possible_job,
                engine=engine,
                image=image,
                script=script,
                unsupported_attributes=unsupported_attributes,
            )
            jobs.append(job)

    def get_jobs_for_engine(self, engine, stage_name, job_name=None):
        """Get jobs for engine.

        Return the jobs for the specified engine
        """
        job_exclusions = ["crimescene"]
        jobs_to_run = []
        for stage in self.stages:
            if stage.name == stage_name:
                for job in stage.jobs:
                    if (
                        job.engine == engine
                        and (job.name == job_name or job_name is None)
                        and job.name not in job_exclusions
                    ):
                        jobs_to_run.append(job)

        logger.debug(
            i18n.t("zebra.pipeline_model.found_jobs", engine=engine, jobs=jobs_to_run)
        )
        return jobs_to_run

    @staticmethod
    def __load_pipeline(file_name=r".gitlab-ci.yml"):
        logger.debug(i18n.t("zebra.pipeline_model.loading_model"))
        with open(file_name, encoding="utf-8") as file:
            return yaml.safe_load(file)

    def __replace_variables(self):
        """__replace_variables.

        Replace variables in image tag of ci file.
        """
        logger.debug(i18n.t("zebra.pipeline_model.replace_var"))
        raw_pipeline_definition = yaml.dump(self.__pipeline)
        if "variables" in self.__pipeline:
            for key, value in self.__pipeline["variables"].items():
                raw_pipeline_definition = raw_pipeline_definition.replace(
                    f"${{{key}}}", value
                )

        self.__pipeline = yaml.safe_load(raw_pipeline_definition)

    def __load_pipeline_with_included_pipelines(self, file_name=r".gitlab-ci.yml"):
        pipeline = self.__load_pipeline(file_name)
        if "include" in pipeline:
            for included_pipeline in pipeline["include"]:
                try:
                    loaded_pipeline = self.__load_pipeline_with_included_pipelines(
                        included_pipeline.lstrip("/")
                    )
                except RecursionError as error:
                    raise CLIError(
                        i18n.t("zebra.gitlab_yaml_include_recursion_error")
                    ) from error
                if "variables" in loaded_pipeline:
                    loaded_vars = loaded_pipeline["variables"]
                    if "variables" in pipeline:
                        pipeline["variables"] = {**loaded_vars, **pipeline["variables"]}
                loaded_pipeline.update(pipeline)
                pipeline = loaded_pipeline
        return pipeline


# pylint: enable=too-few-public-methods
