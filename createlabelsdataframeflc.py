"""
This file creates the labels of the dataframe for the FLC task.
"""

import os
import pandas as pd


class CreateLabelsDataframeFLC:
    """
    Class to create the labels of the FLC dataframe.
    """

    @staticmethod
    def load_labels(path: str):
        '''
        This helper function will create a dataframe with the labels of the dataset.
        It will be then called from the createdataframeflc.py.

        :type: path: str
        :return: Pandas dataframe
        '''

        data = []

        for dirs, subdir, files in os.walk(path):
            # Go through the directory with the files
            for file in files:
                filepath = dirs + '/' + file
                with open(filepath, 'r') as single_file:
                    # loop through all lines using f.readlines() method
                    for line in single_file.readlines():
                        line = line.split()
                        data.append(line)

        dataframe = pd.DataFrame(data, columns=['article_id', 'technique',
                                                'start_index', 'end_index'])
        # print(df)  # Debug
        return dataframe

# load_labels = CreateLabelsDataframe.load_labels('./datasets/couplelabelsfordev') # Debug
