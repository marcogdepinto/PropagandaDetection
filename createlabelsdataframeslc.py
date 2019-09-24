"""
This file creates the labels of the dataframe for the SLC task.
"""

import os
import pandas as pd


class CreateLabelsDataframeSLC:
    """
    Class to create the labels of the SLC dataframe.
    """

    @staticmethod
    def load_labels(path: str):
        '''
        This helper function will create a dataframe with the labels of the dataset.
        It will be then called from the createdataframeslc.py.

        :type: path: str
        :return: Pandas dataframe
        '''

        data = []

        for dirs, subdir, files in os.walk(path):  # Go through the directory with the files
            for file in files:
                filepath = dirs + '/' + file
                with open(filepath, 'r') as single_file:
                    # loop through all lines using f.readlines() method
                    for line in single_file.readlines():
                        line = line.strip().split('\t')
                        # print(line)
                        data.append(line)

        dataframe = pd.DataFrame(data, columns=['article_id', 'line',
                                                'is_propaganda'])
        # print(df)  # Debug
        return dataframe


# load_labels = CreateLabelsDataframeSLC.load_labels('./datasets/slclabelsdev') # Debug
