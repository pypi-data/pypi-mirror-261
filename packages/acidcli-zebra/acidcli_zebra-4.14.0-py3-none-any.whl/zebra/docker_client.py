# Copyright Capgemini Engineering B.V.

"""Client for Docker communication."""

import hashlib
import os

import docker
import i18n
from docker.errors import ImageNotFound, DockerException, APIError
from docker.types import Mount
from loguru import logger

from zebra.exceptions import DockerClientError, CLIError


class DockerClient:
    """Interface for Docker."""

    __engine = None
    __docker_client = None
    __docker_api = None

    def __init__(self):
        """__init__."""
        try:
            self.__docker_client = docker.from_env()
            self.__docker_api = docker.APIClient()
            self.__engine = self.__get_container_engine()
        except DockerException as error:
            logger.debug(
                i18n.t("zebra.docker_client.docker_exception_debug", error=error)
            )
            raise DockerClientError(
                i18n.t("zebra.docker_client.docker_exception_startup_user")
            ) from error

    def __get_container_engine(self):
        """Get engine from docker.

        Return current engine type from Docker.

        :return: string with engine type (windows or linux)
        """
        engine = self.__docker_client.info()["OSType"]

        logger.debug(
            i18n.t("zebra.docker_client.container_engine_found", engine=engine)
        )

        return engine

    def get_engine(self):
        """Get engine.

        Return engine.

        :return: string with engine (windows/linux)
        """
        return self.__engine

    def get_other_engine(self):
        """Get other engine.

        Return the engine that's currently not used.

        :return: string with engine (windows/linux)
        """
        if self.__engine == "linux":
            engine = "windows"
        else:
            engine = "linux"
        return engine

    def create_mounts(self):
        """Create mounts.

        Creates writeable mount for project directory.

        :return: list with all mounts
        """
        logger.debug(i18n.t("zebra.docker_client.create_mounts"))

        mounts = []
        if self.__engine == "linux":
            mounts.append(
                Mount("/zebra_mount", os.getcwd(), type="bind", read_only=False)
            )
        elif self.__engine == "windows":
            mounts.append(
                Mount("c:\\zebra_mount", os.getcwd(), type="bind", read_only=False)
            )
        logger.debug(mounts)

        return mounts

    def create_volumes(self, container_name):
        """Create volumes.

        Create volume for Poetry cache folder.

        Working dir + container identifier are used for hash of volume.
        Another project dir, other container or other version of container
        will lead to a new hash and thus to a new Poetry volume.

        :param container_name: container identifier for hash
        :return: list with volumes
        """
        volume_hash = f"{os.getcwd()}-{container_name}"
        context_hash = hashlib.sha256(
            volume_hash.encode(), usedforsecurity=False
        ).hexdigest()

        logger.debug(i18n.t("zebra.docker_client.create_volumes"))
        volumes = None
        if self.__engine == "linux":
            volumes = {
                f"zebra_cache_{context_hash}": {"bind": "/poetry/cache/", "mode": "rw"}
            }
        elif self.__engine == "windows":
            volumes = {
                f"zebra_cache_{context_hash}": {
                    "bind": "c:\\poetry\\cache\\",
                    "mode": "rw",
                }
            }
        logger.debug(volumes)

        return volumes

    def pull_image(self, image):
        """Pull image from docker.

        Pull the image from the registry when not available and show the streamed progress on screen.

        :param image: image to pull
        """
        try:
            self.__docker_client.images.get(image)
        except ImageNotFound:
            logger.info(i18n.t("zebra.docker_client.image_not_available", image=image))
            logger.info(i18n.t("zebra.docker_client.image_pull"))

            try:
                for line in self.__docker_client.api.pull(
                    image, stream=True, decode=True
                ):
                    status = line["status"]
                    if "progress" in line:
                        logger.info(f"{status} {line['progress']}")
                logger.debug(i18n.t("zebra.docker_client.image_pulled"))
            except APIError as error:
                if "denied: access forbidden" in error.explanation:
                    raise DockerClientError(
                        i18n.t(
                            "zebra.docker_client.failed_image_pull_not_logged_in",
                            image=image,
                        )
                    ) from error
                if (
                    "Client.Timeout exceeded while awaiting headers"
                    in error.explanation
                ):
                    raise DockerClientError(
                        i18n.t(
                            "zebra.docker_client.failed_image_pull_not_connected_to_vpn",
                            image=image,
                        )
                    ) from error
                raise DockerClientError(
                    i18n.t(
                        "zebra.docker_client.docker_exception_debug",
                        error=error.explanation,
                    )
                ) from error

    def start_container(self, image, verbosity, dot_env_variables):
        """Start container.

        Start detached container.
        tty is used to keep container alive.

        :param image: image to start
        :param dot_env_variables: env variables to inject
        :return: container handle
        """
        container = None

        mounts = self.create_mounts()
        volumes = self.create_volumes(image)

        if self.__engine == "linux":
            environment = [
                "POETRY_VIRTUALENVS_PATH=/poetry/cache/",
                "POETRY_VIRTUALENVS_IN_PROJECT=false",
                f"ZEBRA_VERBOSITY={verbosity}",
            ]
            environment.extend(dot_env_variables)

            container = self.__docker_client.containers.run(
                image,
                working_dir="/zebra_mount",
                mounts=mounts,
                volumes=volumes,
                detach=True,
                tty=True,
                environment=environment,
            )
        elif self.__engine == "windows":
            environment = [
                "POETRY_VIRTUALENVS_PATH=c:\\poetry\\cache\\",
                "POETRY_VIRTUALENVS_IN_PROJECT=false",
                f"ZEBRA_VERBOSITY={verbosity}",
            ]
            environment.extend(dot_env_variables)

            container = self.__docker_client.containers.run(
                image,
                working_dir="c:\\zebra_mount",
                mounts=mounts,
                volumes=volumes,
                detach=True,
                tty=True,
                environment=environment,
            )

        return container

    def execute_commands(self, container, job):
        """Execute commands.

        Execute given command on given container.
        Streams logging of container to Zebra logging.
        Checks exit code, when not 0, raises ZebraError

        :param container: container to run command on
        :param commands: command to run on container
        """
        cascaded_commands = self.__concatenate_job_script_to_command(job.script)

        logger.debug(
            i18n.t(
                "zebra.docker_client.execute_command_debug",
                command=cascaded_commands,
                container=container.image.tags,
            )
        )

        exec_handler = self.__docker_api.exec_create(container.id, cascaded_commands)
        result_handler = self.__docker_api.exec_start(exec_handler, stream=True)

        # Blocking for loop as long as container proces is not exited.
        # Last read may throw: The pipe has ended.
        try:
            for result in result_handler:
                logger.opt(raw=True).info(result.decode())
        except BaseException as error:
            # Exceptions may be different on different OS types
            logger.debug(
                i18n.t("zebra.docker_client.execute_command_failed_debug", error=error)
            )

        logger.debug(i18n.t("zebra.docker_client.execute_command_get_exit"))
        exit_code = self.__docker_api.exec_inspect(exec_handler["Id"]).get("ExitCode")
        logger.debug(
            i18n.t(
                "zebra.docker_client.execute_command_get_exit_result",
                exit_code=exit_code,
            )
        )

        if exit_code != 0:
            raise CLIError(
                i18n.t("zebra.docker_client.execute_job_failed", job=job.name)
            )

    def __concatenate_job_script_to_command(self, commands):
        """Concatenate job script to command.

        Transform list of commands in single shell call.

        For Linux, sh is used.
        For Windows powershell is used.

        :param commands: list of commands to transform
        :return: single shell call with all commands
        """
        logger.debug(
            i18n.t("zebra.docker_client.concatenate_commands", commands=commands)
        )

        if self.__engine == "linux":
            joined_commands = " && ".join(commands)
            cascaded_commands = f'sh -c "{joined_commands}"'
        elif self.__engine == "windows":
            joined_commands = " ; ".join(commands)
            cascaded_commands = f'powershell "{joined_commands}"'

        logger.debug(
            i18n.t(
                "zebra.docker_client.concatenate_commands_result",
                command=cascaded_commands,
            )
        )

        return cascaded_commands
