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
    df = pd.read_excel(file_path, usecols="B:E").fillna("o")
    print("Using Lemmer")
    table = process(df, parser.LEMMER)
    compute_similarity(table)
    print("Using Stemmer")
    table = process(df, parser.STEMMER)
    compute_similarity(table)


def process(df, clean_method: str):
    value_table = {
        CONCRETE_G: [],
        CONCRETE_S: [],
        ABSTRACT_G: [],
        ABSTRACT_S: []
    }
    for column in df:
        processed = []
        for definition in df[column]:
            cleaned = parser.cleaning(definition, clean_method)
            if len(cleaned) == 0:
                continue
            processed.append(cleaned)

        if "concreto_generico" in column:
            value_table[CONCRETE_G] = processed.copy()
        elif "concreto_specifico" in column:
            value_table[CONCRETE_S] = processed.copy()
        elif "astratto_generico" in column:
            value_table[ABSTRACT_G] = processed.copy()
        elif "astratto_specifico" in column:
            value_table[ABSTRACT_S] = processed.copy()
    return value_table
