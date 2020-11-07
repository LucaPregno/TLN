import os
import re
from collections import Counter
from DiCaro.Utility import parser, plot, similarity

INPUT_PATH = os.path.abspath('../DiCaro/Exercise4/resources/input.txt')
CLUSTER_STEP = [1, 4, 8]
MOST_COMMON_WORDS = 15


def main():
    for step in CLUSTER_STEP:
        print("CLUSTERING WITH STEP:", step)
        sentences_as_counter = process_file(INPUT_PATH, step)
        plot.print_table(sentences_as_counter, MOST_COMMON_WORDS)
        similarity.compute_similarity(sentences_as_counter)


def process_file(path: str, step: int = 1) -> list:
    """
    Read the file and extract sentences, then cluster them
    :param path: file path to read
    :param step: cluster step dimension
    :return: clustered Counter list of the sentences
    """
    file = open(path, "r")
    file_sentences = re.split('[.!?]', file.read())
    file.close()
    cleaned_sentences = []
    for sentence in file_sentences:
        sentence_counter = parser.cleaning(sentence, parser.LEMMER)
        if len(sentence_counter.keys()) > 0:
            cleaned_sentences.append(sentence_counter)

    return cluster_sentences(cleaned_sentences, step=step)


def cluster_sentences(sentences: list, step: int) -> list:
    table_sentence = []
    counter = Counter()
    for i in range(len(sentences)):
        counter = counter + sentences[i]
        if (i % step == 0 or i == len(sentences)) and len(counter.keys()) > 0:
            table_sentence.append(counter.copy())
            counter.clear()

    return table_sentence
