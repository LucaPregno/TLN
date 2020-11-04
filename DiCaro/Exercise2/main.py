import os
import pandas as pd
from DiCaro.Utility import parser, wordnet

INPUT_PATH = os.path.abspath('../DiCaro/Exercise2/resources/content_to_form.xlsx')
OUTPUT_PATH = os.path.abspath('../DiCaro/Exercise2/resources/output.txt')
MIN_FREQUENCY = 0
PERCENTAGE = 50


def main():
    df = pd.read_excel(INPUT_PATH, usecols="B:I").fillna("o")
    print("Using", parser.LEMMER)
    concept_table = process(df, parser.LEMMER)
    concept_list = wordnet.genus_differentia(concept_table)
    write_output(concept_list)


def process(df, clean_method: str) -> list:
    processed = []
    for column in df:
        concept = ""
        for definition in df[column]:
            concept += definition
        cleaned = parser.cleaning(concept, clean_method, frequency=MIN_FREQUENCY, percentage=PERCENTAGE)
        processed.append(cleaned)
    return processed


def write_output(concept_list):
    file = open(OUTPUT_PATH, "a")
    file.write(f'\nFrequency:{MIN_FREQUENCY} Percentage:{PERCENTAGE} Method:{parser.LEMMER}\n\n')
    for c in concept_list:
        line = f'{c[0]} {c[0].definition()} | Score:{c[1]}'
        print(line)
        file.write(f'{line}\n')
    file.write("-------------------------------------------------------------------------")
    file.close()
