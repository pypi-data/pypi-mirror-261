# Copyright Capgemini Engineering B.V.

"""Command Line Interface.

Command line interface for zebra tooling
"""
import argparse
import sys

from zebra import __version__ as zebra_version


class DerivedArgumentParser(argparse.ArgumentParser):
    """Override of standard ArgumentParser."""

    def error(self, message):
        """Override of error message function for ArgumentParser."""
        sys.stderr.write(f"error: {message}\n")
        self.print_help()
        sys.exit(1)


# pylint: disable=too-few-public-methods
class CLI:
    """Main Command Line Interface parser."""

    def __init__(self, pipeline_model):
        """Initialize CLI."""
        parser = DerivedArgumentParser(
            description="CICD Command Line Interface for %(prog)s"
        )

        parser.add_argument(
            "--version",
            action="version",
            version=f"{parser.prog} {zebra_version}",
        )

        parser.add_argument(
            "--verbose",
            "-v",
            action="count",
            default=0,
            help="verbose mode (-vv for more, -vvv to enable full verbosity)",
        )

        parser.add_argument(
            "--switch",
            "-s",
            action="store_true",
            default=False,
            help="Enable automatic switching of Docker engine between Windows and Linux",
        )

        parent_parser = argparse.ArgumentParser(add_help=False)

        subparsers = parser.add_subparsers(
            title="pipeline stages", dest="stage", required=True
        )

        for stage in pipeline_model.stages:
            subparser = subparsers.add_parser(
                stage.name, help=f"available {stage.name} commands"
            )
            subsubparsers = subparser.add_subparsers(
                title=f"{stage.name} tasks", dest="job"
            )

            for job in stage.jobs:
                subsubparsers.add_parser(
                    job.name, parents=[parent_parser], help=f"{stage.name} {job.name}"
                )

        self.parser = parser


# pylint: enable=too-few-public-methods
