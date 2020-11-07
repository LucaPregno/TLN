import os
import re
from DiCaro.Utility import parser, plot, similarity

INPUT_PATH = os.path.abspath('../DiCaro/Exercise4/resources/input.txt')
CLUSTER_STEP = 4
MOST_COMMON_WORDS = 15


def main():
    sentences_as_counter = process_file(INPUT_PATH)
    plot.print_table(sentences_as_counter, MOST_COMMON_WORDS)
    similarity.compute_similarity(sentences_as_counter)


def process_file(path: str) -> list:
    file = open(path, "r")
    file_sentences = re.split('[.!?]', file.read())
    file.close()
    cleaned_sentences = []
    for sentence in file_sentences:
        a = parser.cleaning(sentence, parser.LEMMER)
        cleaned_sentences.append(a)

    return cleaned_sentences
