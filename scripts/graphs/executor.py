#!/usr/bin/env python3

"""
Master code file.
"""

__author__ = "Scott Teresi"

import argparse
import os
import logging
import coloredlogs

# from module import module

# TODO import your functions and classes here to invoke in process()


def process():
    raise NotImplementedError

    # In the short term we want to understand what genes are repeated within a
    # given module. We also want to know how many genes are repeated between
    # modules

    # In the longer term we want to know how many genes are repeated within a
    # DEG library comparison. We also want to know how many genes are repeated
    # between library comparisons

    # In the even longer term we want to know how many genes are shared between
    # the network and between the full body of DEGs. Venn diagram?

    # Define your instances here.
    # And use them below and we will invoke all of the graphing commands in
    # process()

    # TODO
    # Iterate over the module dir here, declare a function
    # Call the constructor (ModuleData)in the iterator
    # modulesObject = ModuleData(path_to_modules)
    # Add the module object to some sort of container or iterable
    # Return a list of modules??? Then every following graphing function then
    # has to accept a list of modules or a single module.... Is that what we
    # want?
    # FInish the iterator

    degsObject = DegData()


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
