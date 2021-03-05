#!/usr/bin/env python

"""
Combine module enrichment data and differential expression data
"""

__author__ = "Scott Teresi, Alder Fulton"

# IMPORTS go here


class Module_Enrichment_Data:
    def __init__(self, color, component_data):
        """
        color (str): color of the module

        """
        self.color = color

        # This will be refactored
        if component_data is not None:
            # Read and initialize data as
            self.component_data = self.read_component_data(component_data)

        else:
            self.component_data = None

        # Then we can store all as an HDF5 later.

    # This could be refacotred into a factory method
    def read_component_data(component_data):
        """
        This function will read the component data and return it as a pandas
        data file

        Args:
            component_data (str): Path to the component data file formatted as
            xyz
        """
        pass

    def __repr__(self):
        """
        Redefines the string method when you try to print an object
        """
        info = "Hi my color is {self.color}!"
        return info.format(self=self)


# ----------------

Blue = Module_Enrichment_Data(component_data)


object_list = []
for a_file in directory_of_data:
    object_list.append(Module_Enrichment_Data(component_data))  # this would
    # append an object to the list

# Now if you want to iterate over the list of modules and see what color you
# are working with you can do:
for module in object_list:
    print(module.color)
    print(module)
