import os
import pandas as pd
from DiCaro.Utility import parser, wordnet, utility

INPUT_PATH = os.path.abspath('../DiCaro/Exercise2/resources/content_to_form.xlsx')
OUTPUT_PATH = os.path.abspath('../DiCaro/Exercise2/resources/output.txt')
MIN_FREQUENCY = 3
MOST_COMMON_PERCENTAGE = 0


def main():
    df = pd.read_excel(INPUT_PATH, usecols="B:I").fillna("o")
    print("Using", parser.LEMMER)
    concept_table = process(df, parser.LEMMER)
    concept_list = wordnet.genus_differentia(concept_table)
    utility.write_on_file(concept_list, OUTPUT_PATH, MIN_FREQUENCY, MOST_COMMON_PERCENTAGE)


def process(df, clean_method: str) -> list:
    processed = []
    for column in df:
        concept = ""
        for definition in df[column]:
            concept += definition
        cleaned = parser.cleaning(concept, clean_method, frequency=MIN_FREQUENCY, percentage=MOST_COMMON_PERCENTAGE)
        processed.append(cleaned)
    return processed
