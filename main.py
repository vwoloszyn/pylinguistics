import pandas as pd
import sys
import os

sys.path.append("../../pylinguistics/pylinguistics")
from pylinguistics import Pylinguistics as pl

original_features = []


def get_text_features(sent):
    objpl = pl.text(sent)
    objpl.setLanguage("pt")

    features_dict = objpl.getFeatures()
    features_dict.update({'sent': sent})
    return pd.DataFrame.from_dict(features_dict, orient='index').T


def save_readability_report(files_dir):
    for file in os.listdir(files_dir):
        print("Dataset: ", file.split('-')[0])
        sentences = open(os.path.join(files_dir, file), encoding='utf8').readlines()

        sentences = list(map(str.strip, sentences))

        dfs = map(get_text_features, sentences)

        report_df = pd.concat(dfs).loc[:, ['redability', 'sent', 'LexicalDiversty', 'ContentDiversty']]
        report_df.to_csv(file.split('.')[0] + '.' + files_dir + '.csv')
        print("Média Readability: ", report_df['redability'].mean())
        print()
        print("STD Readability: ", report_df['redability'].std())
        print()
        print("-" * 40)
        print()


PRED_DIR = 'samples'
save_readability_report(PRED_DIR)
sent = "Olá Mundo"
