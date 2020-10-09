#!/usr/bin/env python3

"""
Master code file.
"""

__author__ = "Scott Teresi"

import argparse
import os
import logging
import coloredlogs

# TODO import your functions and classes here to invoke in process()


def process():
    raise NotImplementedError


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    path_main = os.path.abspath(__file__)

    # TODO add your arguments here. Some arguments will be directories

    parser.add_argument(
        "-v", "--verbose", action="store_true", help="set debugging level to DEBUG"
    )

    args = parser.parse_args()
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logger = logging.getLogger(__name__)
    coloredlogs.install(level=log_level)

    # Process
    process()
