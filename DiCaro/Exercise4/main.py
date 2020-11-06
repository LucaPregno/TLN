import os
import re
from DiCaro.Utility import parser, plot

INPUT_PATH = os.path.abspath('../DiCaro/Exercise4/resources/input.txt')
CLUSTER_STEP = 4
MOST_COMMON_WORDS = 15


def main():
    sentence_table = process_file(INPUT_PATH)
    plot.print_table(sentence_table, MOST_COMMON_WORDS)
    # sentence_table = cluster_sentences(sentence_table)


def process_file(path: str) -> list:
    file = open(path, "r")
    sentences = re.split('[.!?]', file.read())
    file.close()
    processed_sentence = []
    for sentence in sentences:
        processed_sentence.append(parser.cleaning(sentence, parser.LEMMER))

    return processed_sentence
