import os
import pandas as pd
import DiCaro.Utility.parser_utility as parser

file_path = os.path.abspath('../DiCaro/Exercise2/content_to_form.xlsx')


def main():
    df = pd.read_excel(file_path, usecols="B:M").fillna("o")
    print("Using Lemmer")
    concept_table = process(df, parser.LEMMER)


def process(df, clean_method: str) -> list:
    processed = []
    for column in df:
        concept = set()
        for definition in df[column]:
            cleaned = parser.cleaning(definition, clean_method)
            if len(cleaned) == 0:
                continue
            concept = concept.union(cleaned)
        processed.append(concept)

    return processed
