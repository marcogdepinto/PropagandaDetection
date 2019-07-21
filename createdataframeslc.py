import os
import argparse
import numpy as np
import pandas as pd
from createlabelsdataframeslc import CreateLabelsDataframeSLC


class CreateDataframeSLC:

    '''
    Task SLC
    The format of a tab-separated line of the gold label and the submission files for task SLC is:
    article_id   sentence_id    label
    where article_id and sentence_id are the identifiers of the article and the sentence
    (the first sentence has id 1) and label={propaganda/non-propaganda}.
    Gold and submission files must have the same number of rows as the number of sentences,
    i.e. of lines, in the article. In order to help participants preparing a submission, we provide
    template prediction files, which have the same format of the gold files where label is replaced with ?.
    Sentences are splitted using dots.
    '''

    def load_sentences_with_labels(path: str, path_to_labels: str, savepath: str):

        '''
        This function will be used to create the Pandas dataframe.
        It will also pickle the dataframe to use it later.
        :param path: str
        :param path_to_labels: str
        :param savepath: str
        :return: Pandas dataframe
        '''

        lst = []
        newlst = []

        print("Creating the labels dataframe..")
        # Creating the labels dataframe using the helper function
        labels_df = CreateLabelsDataframeSLC.load_labels(path_to_labels)

        print("Looping through the articles")
        # Creating the series to be used to match the indexes of the single words within the loop

        for dirs, subdir, files in os.walk(path):  # Go through the directory with the files
            for file in files:
                filepath = dirs + '/' + file
                article_id = str(file[:-4][7:])
                with open(filepath, 'r') as f:
                    # loop through all lines using f.readlines() method
                    for line in f.readlines():
                        # this is how you would loop through each letter
                        line = line.strip().split('\t')
                        print(line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path to get the train dataset")
    parser.add_argument("path_to_labels", help="Path to get the labels dataset")
    parser.add_argument("savepath", help="Path to save the pickle of the output dataframe")
    args = parser.parse_args()
    load_articles = CreateDataframeSLC.load_sentences_with_labels(args.path, args.path_to_labels, args.savepath)

