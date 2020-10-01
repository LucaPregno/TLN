import os
import pandas as pd
import DiCaro.Utility.parser_utility as parser
import DiCaro.Utility.wordnet_utility as wn_utility

file_path = os.path.abspath('../DiCaro/Exercise2/content_to_form.xlsx')


def main():
    df = pd.read_excel(file_path, usecols="B:M").fillna("o")
    print("Using Lemmer")
    concept_table = process(df, parser.LEMMER)
    concept_list = wn_utility.get_concept(concept_table)
    print(concept_list)


def process(df, clean_method: str) -> list:
    processed = []
    for column in df:
        concept = ""
        for definition in df[column]:
            concept += definition
        cleaned = parser.cleaning(concept, clean_method)
        processed.append(cleaned)
    return processed
