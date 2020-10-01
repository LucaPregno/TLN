import os
import pandas as pd
import DiCaro.Utility.parser_utility as parser
import DiCaro.Utility.wordnet_utility as wn_utility

file_path = os.path.abspath('../DiCaro/Exercise2/content_to_form.xlsx')


def main():
    df = pd.read_excel(file_path, usecols="B:M").fillna("o")
    print("Using Lemmer")
    concept_table = process(df, parser.LEMMER)
    wn_utility.calculate_hyponyms("dog")


def process(df, clean_method: str) -> list:
    processed = []
    for column in df:
        concept = ""
        for definition in df[column]:
            concept += definition
        cleaned = parser.cleaning(concept, clean_method, frequency=2)
        processed.append(cleaned)
    return processed
