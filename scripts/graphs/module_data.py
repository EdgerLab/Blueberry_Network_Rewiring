#!/usr/bin/env python3

"""
Contains the data and functions inherent to the modules
"""

__author__ = "Scott Teresi"


class ModuleData(object):
    def __init__(self, module_file):
        raise NotImplementedError

        self.module_dataframe = self.import_module(module_file)

    # @classmethod
    # def iterate_over_dir(cls, module_dir, more....):
    # Look up class methods
    # Somewhere in your iterate the variable module_file is declared
    # This will return an instance!

    # raise NotImplementedError

    # return ModuleData(module_file)

    @staticmethod
    def import_modules(module_file):
        """
        Import AT gene modules (Blueberry genes converted to AT
        orthologs into a dictionary.

        Args:
            module_older (str): Directory in which deg files are located

        Returns:
            module_dict (dictionary): A dicitonary of modules with the key
            being the module name (color) and the value being the module
            dataframe

        """
        # Iterate over the module folder
        # Put the module file into a pandaframe
        # Add the pandaframe to the dictionary
        # Add the

        raise NotImplementedError
