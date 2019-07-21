import os
import pandas as pd


class CreateLabelsDataframeSLC:

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
                with open(filepath, 'r') as f:
                    # loop through all lines using f.readlines() method
                    for line in f.readlines():
                        line = line.strip().split('\t')
                        # print(line)
                        data.append(line)

        df = pd.DataFrame(data, columns=['article_id', 'line', 'is_propaganda'])
        # print(df)  # Debug
        return df


# load_labels = CreateLabelsDataframeSLC.load_labels('./datasets/slclabelsdev') # Debug
