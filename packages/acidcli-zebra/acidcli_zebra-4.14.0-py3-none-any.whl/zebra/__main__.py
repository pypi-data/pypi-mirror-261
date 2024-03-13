# Copyright Capgemini Engineering B.V.

"""Zebra Command Line Interface."""
import os
import sys
from types import SimpleNamespace

import i18n
import yaml
from dotenv import dotenv_values
from loguru import logger
from pyfiglet import figlet_format

from zebra import __version__ as zebra_version
from zebra.cli import CLI
from zebra.docker_client import DockerClient
from zebra.docker_executable import DockerExecutable
from zebra.exceptions import CLIError, DockerClientError
from zebra.pipeline_model import PipelineModel

i18n.load_path.append(os.path.join(os.path.dirname(__file__), "locale"))

logger.remove()
logger.add(
    "zebra.log",
    rotation="daily",
    retention="1 week",
    filter=lambda record: "not_to_file" not in record["extra"],
)


def __print_error(error):
    """Print error.

    Print error to logger. Split newline into multiple logger calls.

    :param error: string with error to print
    """
    for line in str(error).split("\n"):
        logger.error(line)


def determine_container_types():
    """Determine container types.

    Return the types of container that can be run.

    :return: list with container types (windows and/or linux)
    """
    platform = sys.platform
    container_types = []
    if platform == "linux":
        container_types = ["linux"]
    elif platform == "darwin":
        container_types = ["linux"]
    elif platform == "win32":
        container_types = ["linux", "windows"]
    logger.debug(
        i18n.t(
            "zebra.found_host_os",
            platform=platform,
            container_types=container_types,
        )
    )
    return container_types


def __parse_pipeline_model():
    """Parse pipeline model.

    Parses Gitlab-ci.yml pipeline into a pipeline model.
    Interpolates variables.

    :return: parsed pipeline model
    """
    try:
        pipeline_model = PipelineModel()
    except FileNotFoundError as error:
        __print_error(i18n.t("zebra.gitlab_yaml_not_found", filename=error.filename))
        pipeline_model = SimpleNamespace(stages=[])
    except yaml.YAMLError as error:
        __print_error(i18n.t("zebra.gitlab_yaml_invalid_format", error=error))
        pipeline_model = SimpleNamespace(stages=[])

    return pipeline_model


def _get_dot_env_variables():
    """Get dot env variables.

    Load variables from .env file.
    If no .env file exists, then empty array will be returned.

    :return: array with string, key=value pairs
    """
    variables = []

    for key, value in dotenv_values(".env").items():
        logger.debug(i18n.t("zebra.dot_env.loading_variable", variable=key))
        variables.append(f"{key}={value}")

    logger.debug(i18n.t("zebra.dot_env.loaded_variables", count=len(variables)))

    return variables


def __run_stage(docker_client, config, jobs):
    """Run stage.

    For each job, invokes job runner.

    :param docker_client: Docker client to run image on
    :param config: config to pass to Docker client
    :param jobs: jobs to run
    """
    for job in jobs:
        stagejob = f"{config.stage}: {job.name}"
        logger.info(
            i18n.t(
                "zebra.terminal_divider.with_name",
                name=f"{stagejob:^20}",
            )
        )
        __run_job(docker_client, config, job, _get_dot_env_variables())


def __run_job(docker_client, config, job, dot_env_variables):
    """Run job.

    Prepares and executes job in a container.
    Kills and removes container afterwards.

    :param docker_client: Docker client to run image on
    :param config: config to pass to Docker client
    :param job: job to run
    :param dot_env_variables: env variables to inject
    """
    if getattr(job, "unsupported_attributes", None):
        raise CLIError(
            i18n.t(
                "zebra.pipeline_model.unsupported_attributes",
                count=len(job.unsupported_attributes),
                job=job.name,
                attributes=job.unsupported_attributes,
            )
        )

    container = None

    try:
        docker_client.pull_image(job.image)

        container = docker_client.start_container(
            job.image, config.verbose, dot_env_variables
        )
        docker_client.execute_commands(container, job)
    except CLIError as error:
        raise error from error

    finally:
        if container:
            logger.debug(i18n.t("zebra.stop_container"))
            container.kill()
            container.remove()


def main():
    """Execute Zebra."""
    info_logger = logger.add(
        sys.stdout,
        colorize=True,
        format="Zebra: <level>{level: <8} - {message}</level>",
        level="INFO",
    )

    logger.bind(not_to_file=True).opt(raw=True).info(
        figlet_format("zebra", font="starwars")
    )
    logger.info(i18n.t("zebra.versioning.zebra_version", version=zebra_version))

    try:
        pipeline_model = __parse_pipeline_model()

        cli = CLI(pipeline_model)
        config = cli.parser.parse_args(sys.argv[1:])

        if config.verbose > 0:
            logger.remove(info_logger)
            logger.add(
                sys.stdout,
                colorize=True,
                format="Zebra: <level>{level: <8} - {message}</level>",
                level="DEBUG",
            )

        # Execute jobs of current Docker engine type
        docker_client = DockerClient()
        jobs_to_run = pipeline_model.get_jobs_for_engine(
            docker_client.get_engine(), config.stage, config.job
        )

        __run_stage(docker_client, config, jobs_to_run)

        # if there are jobs for other engine ....
        engine_2 = docker_client.get_other_engine()
        jobs_to_run_2nd_engine = pipeline_model.get_jobs_for_engine(
            engine_2, config.stage, config.job
        )

        if jobs_to_run_2nd_engine:
            logger.debug(i18n.t("zebra.switch_engine_needed"))
            if engine_2 in determine_container_types():
                logger.debug(i18n.t("zebra.device_can_run_engine", engine=engine_2))

                if config.switch:
                    DockerExecutable().switch_engine(engine_2)
                    docker_client_2 = DockerClient()
                    __run_stage(
                        docker_client_2,
                        config,
                        jobs_to_run_2nd_engine,
                    )
                else:
                    logger.warning(i18n.t("zebra.switch_disabled", engine=engine_2))
            else:
                logger.warning(
                    i18n.t("zebra.device_cannot_run_engine", engine=engine_2)
                )

        logger.info(i18n.t("zebra.zebra_finished"))

    except CLIError as error:
        __print_error(error)
        sys.exit(1)
    except DockerClientError as error:
        __print_error(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
