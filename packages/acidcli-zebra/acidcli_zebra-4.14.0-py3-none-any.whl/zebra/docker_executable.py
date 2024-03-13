# Copyright Capgemini Engineering B.V.

"""Interface for Docker."""

from pathlib import Path
from shutil import which

import docker
import i18n
from loguru import logger

from zebra.decorators import catch_docker_errors
from zebra.exceptions import CLIError
from zebra.subprocess import Subprocess


class DockerExecutable:
    """Interface for Docker."""

    def __init__(self):
        """__init__."""

    def switch_engine(self, engine):
        """Switch engine.

        Switch Docker engine to Linux or Windows.
        """
        logger.info(i18n.t("zebra.docker_executable.switching_engine", engine=engine))
        if engine == "linux":
            command = [self.get_dockercli_path(), "-SwitchLinuxEngine"]
            process = Subprocess(command)
            process.execute()
        elif engine == "windows":
            command = [self.get_dockercli_path(), "-SwitchWindowsEngine"]
            process = Subprocess(command)
            process.execute()

        self.__is_ready()

    @staticmethod
    @catch_docker_errors
    def __is_ready():
        """Is ready.

        Checking status of Docker Daemon, ping/version/info calls may
        raise various errors when Docker Daemon not ready.

        If Docker Daemon is up, docker-py references will be refreshed
        to prevent random errors being thrown on docker-py calls.

        When it succeeds, Docker daemon is ready.
        When it fails, @catch_docker_errors will retry until timeout.
        """
        logger.debug(i18n.t("zebra.docker_executable.docker_ready"))

        docker_client = docker.from_env()
        logger.debug(
            i18n.t("zebra.docker_executable.docker_ping", ping=docker_client.ping())
        )
        logger.debug(
            i18n.t(
                "zebra.docker_executable.docker_version",
                version=docker_client.version(),
            )
        )
        logger.debug(
            i18n.t("zebra.docker_executable.docker_info", info=docker_client.info())
        )

        logger.debug(i18n.t("zebra.docker_executable.docker_is_ready"))

    @staticmethod
    def get_dockercli_path():
        """Get dockercli path.

        Get path to DockerCLi.exe

        ZebraError when docker not installed.
        ZebraError when DockerCLi.exe not at expected location.

        :return: string path to DockerCli.exe
        """
        docker_path = which("docker")
        if not docker_path:
            raise CLIError(i18n.t("zebra.docker_executable.docker_not_installed"))
        path = Path(docker_path).parent.parent.parent.joinpath("DockerCli.exe")
        if path.exists():
            return str(path)
        raise CLIError(
            i18n.t("zebra.docker_executable.docker_cli_not_found", path=path)
        )
