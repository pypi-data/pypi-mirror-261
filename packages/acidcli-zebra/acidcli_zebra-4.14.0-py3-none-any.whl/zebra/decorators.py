# Copyright Capgemini Engineering B.V.

"""Decorators.

General python function decorators.
"""
import time

from functools import wraps

import i18n
from docker.errors import DockerException
from loguru import logger
from zebra.exceptions import DockerClientError


__DOCKER_CLIENT_TIMEOUT_SECONDS = 180
__SLEEP_INTERVAL = 1


def catch_docker_errors(func):
    """Catch docker errors.

    Wrapper around Docker functions. Docker will throw errors when Docker daemon
    is not ready yet. This wrapper will try the wrapped function until none of
    the excepted errors occur anymore.

    If the wrapper needs more than __DOCKER_CLIENT_TIMEOUT_SECONDS seconds to
    fulfill the func, it will throw a ZebraError.

    :param func: function attribute of wrapped function
    :return: function results
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        error_raised = False

        while True:
            current_time = time.time()

            if (current_time - start_time) > __DOCKER_CLIENT_TIMEOUT_SECONDS:
                raise DockerClientError(
                    i18n.t("zebra.docker_executable.docker_switch_failed")
                )

            try:
                # When error did occur, always wait one extra __SLEEP_INTERVAL before calling wrapped function
                if error_raised:
                    time.sleep(__SLEEP_INTERVAL)
                    return func(*args, **kwargs)

                return func(*args, **kwargs)

            except DockerException as error:
                error_raised = True
                time.sleep(__SLEEP_INTERVAL)
                logger.debug(error)
                logger.debug("Waiting...")
                continue

    return wrapper
