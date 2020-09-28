import os
import pandas as pd
import DiCaro.Utility.parser_utility as parser
from DiCaro.Exercise1.similarity import compute_similarity

file_path = os.path.abspath('../DiCaro/Exercise1/definizioni.xlsx')
CONCRETE_G = "concrete_generic"
CONCRETE_S = "concrete_specific"
ABSTRACT_G = "abstract_generic"
ABSTRACT_S = "abstract_specific"


def main():
    table = read_and_process()
    compute_similarity(table)


def read_and_process():
    value_table = {
        CONCRETE_G: [],
        CONCRETE_S: [],
        ABSTRACT_G: [],
        ABSTRACT_S: []
    }
    df = pd.read_excel(file_path, usecols="B:E")
    df = df.dropna()
    for column in df:
        processed = []
        for data in df[column]:
            processed.append(cleaning(data))

        if "concreto_generico" in column:
            value_table[CONCRETE_G] = processed.copy()
        elif "concreto_specifico" in column:
            value_table[CONCRETE_S] = processed.copy()
        elif "astratto_generico" in column:
            value_table[ABSTRACT_G] = processed.copy()
        elif "astratto_specifico" in column:
            value_table[ABSTRACT_S] = processed.copy()
    return value_table


def cleaning(sentence: str):
    tokenized = parser.rm_stopwords_punctuation(sentence)
    return parser.lemmer(tokenized)
