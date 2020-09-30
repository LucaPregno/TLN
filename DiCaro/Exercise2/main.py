import os
import pandas as pd
import DiCaro.Utility.parser_utility as parser

file_path = os.path.abspath('../DiCaro/Exercise2/content_to_form.xlsx')


def main():
    df = pd.read_excel(file_path, usecols="B:M").fillna("o")
    print("Using Lemmer")
    concept_table = process(df, parser.LEMMER)
    # concept_table = parser.keep_frequency(concept_table, 1)
    print(concept_table)


def process(df, clean_method: str) -> list:
    processed = []
    for column in df:
        concept = ""
        for definition in df[column]:
            concept += definition
        cleaned = parser.cleaning(concept, clean_method, 2)
        #     if len(cleaned) == 0:
        #         continue
        #     concept = concept.union(cleaned)
        # processed.append(concept)
        print(concept)

    return processed
