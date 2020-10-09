#!/usr/bin/env python3

"""
Import differentially expressed genes (Blueberry genes converted to AT
orthologs
"""

__author__ = "Scott Teresi"

import pandas as pd


def import_degs(deg_folder):
    """

    Args:
        deg_folder (str): Directory in which deg files are located

    """

    # TODO
    # Pick the main folder 'Bonferroni', we will refrain from using FDR data in
    # our final output. The Bonferroni folder contains ~20 folders itself, each
    # folder name tells you the comparison being made, as do the files in each
    # folder.

    # Loop through each folder and take the appropriate union file (I will
    # let you know whether to use the dups or no dups file, have not decided
    # yet, but you can pick one for now and work with that) and store it
    # somewhere, as a pandasframe.
    # It may make sense to store each union file in a dictionary
    # with the key being the comparison being made and the value being the
    # dataframe.

    # Then loop over the dictionary and collate all of the dataframes into one
    # large dataframe of all the differentially expressed AT genes.

    raise NotImplementedError
