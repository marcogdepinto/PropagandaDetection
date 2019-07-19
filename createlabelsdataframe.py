import os
import pandas as pd


class CreateLabelsDataframe:

    def load_labels(path: str):

        '''
        This helper function will create a dataframe with the labels of the dataset.
        It will be then called from the createdataframe.py.

        :type: path: str
        :return: dataframe
        '''

        data = []

        for dirs, subdir, files in os.walk(path):  # Go through the directory with the files
            for file in files:
                filepath = dirs + '/' + file
                with open(filepath, 'r') as f:
                    # loop through all lines using f.readlines() method
                    for line in f.readlines():
                        line = line.split()
                        data.append(line)

        df = pd.DataFrame(data, columns=['article_id', 'technique', 'start_index', 'end_index'])
        # print(df)  # Debug
        return df

# load_articles = CreateLabelsDataframe.load_labels('./datasets/couplelabelsfordev') # Debug
