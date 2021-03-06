"""
This file creates the dataframe for the FLC task.
"""

import os
import argparse
import numpy as np
import pandas as pd
from createlabelsdataframeflc import CreateLabelsDataframeFLC


class CreateDataFrameFLC:
    '''
    Task: FLC
    The format of a tab-separated line of the gold label and the submission files for task FLC is:

    id   technique    begin_offset     end_offset

    where id is the identifier of the article, technique is one out of the 18 techniques,
    begin_offset is the character where the covered span begins (included) and end_offset
    is the character where the covered span ends (not included).
    Therefore, a span ranges from begin_offset to end_offset-1.
    The first character of an article has index 0.
    The number of lines in the file corresponds to the number of techniques spotted.
    This is the gold file for the article article123456.txt:

    123456    Name_Calling,Labeling      34    40
    123456    Black-and-White_Fallacy    299    368
    123456    Loaded_Language            400    416
    123456    Exaggeration,Minimization  607    653
    123456    Loaded_Language            635    653
    '''
    @staticmethod
    def load_sentences_with_labels(path: str, path_to_labels: str, savepath: str):

        '''
        This function will be used to create the Pandas dataframe.
        For the training, we will extract from the full corpus
        - the full sentences;
        - the sentences marked with the index (start-end).
        It will also pickle the dataframe to use it later.
        :return: Pandas dataframe
        '''

        lst = []
        newlst = []

        print("Creating the labels dataframe..")
        # Creating the labels dataframe using the helper function
        labels_df = CreateLabelsDataframeFLC.load_labels(path_to_labels)

        print("Creating a Pandas series with the words"
              "of the articles splitted with the related indexes..")
        # Creating the series to be used to match the indexes
        # of the single words within the loop

        for dirs, subdir, files in os.walk(path):
            # Go through the directory with the files
            for file in files:
                filepath = dirs + '/' + file
                article_id = str(file[:-4][7:])
                with open(filepath, 'r') as single_file:
                    # loop through all lines using f.readlines() method
                    for line in single_file.readlines():
                        # this is how you would loop through each letter
                        for value in line:
                            # Compare the index position with the interval
                            # provided in the task-FLC.labels
                            # corresponding file: get only the
                            # sentences you need using the indexes of the words
                            lst.append([value, article_id])

        print("Joining words in sentences... (It may take some time)")

        # print(labels_df)

        words = pd.DataFrame(lst, columns=['letter', 'article_id'])
        # print(words)

        for index, tok in labels_df.iterrows():
            # Get word data
            identifier = tok['article_id']
            technique = tok['technique']
            start = tok['start_index']
            end = tok['end_index']

            # print(start, end)

            start = int(start)
            end = int(end)

            # Get slice
            slice_str = np.array(words[start:(end+1)]['letter'])
            # print("Slice: ", slice)

            # Join letters
            word_from_slice = str("".join(slice_str))
            # print('Word_from_slice: ', word_from_slice)

            # Get full sentence
            sent_slice = np.array(words[words['article_id'] == identifier]['letter'])
            # print(sent_slice)
            target_sentence = str("".join(word_from_slice))
            full_sentence = str("".join(sent_slice))
            # print(target_sentence)
            # print(full_sentence)

            newlst.append([identifier, start, end, full_sentence, target_sentence, technique])
            # print(newlst)

        dataframe = pd.DataFrame(newlst, columns=['article_id', 'start_index', 'end_index',
                                                  'full_sentence', 'target_sentence', 'technique'])

        # Create a pickle of the dataframe
        print('Saving dataframe..')
        dataframe.to_pickle(savepath)
        print("completed")

        return dataframe


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("path", help="Path to get the train dataset")
    PARSER.add_argument("path_to_labels", help="Path to get the labels dataset")
    PARSER.add_argument("savepath", help="Path to save the pickle of the output dataframe")
    ARGS = PARSER.parse_args()
    LOAD_ARTICLES = CreateDataFrameFLC.load_sentences_with_labels(ARGS.path,
                                                                  ARGS.path_to_labels,
                                                                  ARGS.savepath)
