#!/usr/bin/env python3

"""
Master code file.
"""

__author__ = "Alder Fulton"

import argparse
import os
import logging
import coloredlogs
import pandas as pd
import matplotlib.pyplot as plt

# from module import module

# TODO import your functions and classes here to invoke in process()


def process(folder):
    """
    Args:
        folder (str): path to the folder in which the modules are stored.
    """
    total_df = import_dataframe(folder)
    print(total_df)
    print(genes_repeated(5, total_df))
    print(genes_repeated_same_module(2,total_df))
    save(total_df)

def import_dataframe(folder):
    """
    Args:
        folder (str): path to folder with multiple tsv files in it.
    Returns:
        total_df (dataframe): Dataframe containing each unique row in each tsv
        file as well as the numbe of times that row shows up in each tsv.
    """
    genes = []  # Initialize list of unique genes
    df_list = []  # Initialize list of dataframes
    df_names = []  # Initialize list of unique dataframe names
    for files in os.listdir(folder):
        if files.endswith(".tsv"):
            df_list.append(
                pd.value_counts(
                    pd.read_csv(folder + files, names=[files[0:-4]]).iloc[:, 0]
                )
            )
            df_names.append(files[0:-4])
            genes = set(list(genes) + list(df_list[-1].index))
    total_df = pd.DataFrame(index=genes)
    for df in df_list:
        total_df = total_df.join(df)
    total_df = total_df.fillna(0)
    return total_df


def uniques(df):
    # Returns the dataframe so that each value that was more than one is set to
    # one. Useful for determining overlap ocurring outside of the same module.
    df[df > 1] = 1
    return df


def genes_repeated(N, df):
    # Returns a list of the genes repeated at least N times.
    return df[df.sum(axis=1) >= N].index

def genes_repeated_same_module(N,df):
    '''
    Args:
        N (int): the number of repetitions that you want to know about.
        df (dataframe): The dataframe you want to test the collumns of.
    Returns:
        repeated (dataframe): A dataframe with the same collumns of df, dropped
            if there are no values in it, and contains a row of a list of each
            gene repeated that many times.
    '''
    dictionary = {}
    for name in df.columns:
        mask = df[name] >= N
        if mask.any():
            dictionary[name] = list(df[mask].index.values)
    return dictionary

def create_histogram(sr,name):
    """
    Args:
        sr (pandas series): The series of the genes
    Outputs:
        fig (plt figure): Histogram of the number of ocurrences.
    """
    sr = sr[sr!=0]
    values = sr.value_counts().values
    fig =  plt.bar(range(1,len(values)+1),values,align = 'edge')
    plt.xlabel("# of Repetitions")
    plt.ylabel("# of Genes")
    plt.yscale('log')
    for i in range(1,len(values)+1):
        plt.text(i,values[i-1]+.01,str(values[i-1]))
    plt.savefig("hist_" + name, bbox_inches='tight', dpi=150)
    return fig

def save(df,filename = 'results.csv'):
    df.to_csv(filename,sep='\t')

def read(filename):
    df = pd.read_csv(filename,sep = '\t')
    df.set_index(df.columns[0],inplace=True)


    name = df.columns[0]
    for name in df.columns:
        fig = create_histogram(df[name],name)
        plt.clf()
if __name__ == "__main__":
    """
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

    """
    read_only = True
    if read_only:
        read('results.csv')
    else:
        # Process
        process("/home/alder/research/Blueberry_Data/WGCNA_Data/modulecolors_AT_with_duplicates/")
        #process("/home/alder/research/Blueberry_Data/WGCNA_Data/missing_modulecolors_BB/")
