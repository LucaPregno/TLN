import os
import re
from collections import Counter
from DiCaro.Utility import parser, plot

INPUT_PATH = os.path.abspath('../DiCaro/Exercise4/resources/input.txt')
CLUSTER_STEP = 4


def main():
    sentence_table = process_file(INPUT_PATH)
    plot.print_table(sentence_table)
    # sentence_table = cluster_sentences(sentence_table)


def process_file(path: str) -> list:
    file = open(path, "r")
    sentences = re.split('[.!?]', file.read())
    file.close()
    processed_sentence = []
    for sentence in sentences:
        processed_sentence.append(parser.cleaning(sentence, parser.LEMMER))

    return processed_sentence


def cluster_sentences(sentences: list, step: int = CLUSTER_STEP) -> list:
    # step = round(len(sentences) * CLUSTER_STEP/100)
    table_sentence = []
    counter = Counter()
    for i in range(len(sentences)):
        counter = counter + sentences[i]
        if i % step == 0 or i == len(sentences):
            table_sentence.append(counter.copy())
            counter.clear()
    print("CLUSTERED SENTENCES")
    print(list(map(print, table_sentence)))
    return table_sentence
