import os
import re
from collections import Counter
from DiCaro.Utility import parser, plot, similarity, wordnet, utility

INPUT_PATH = os.path.abspath('../DiCaro/Exercise4/resources/input.txt')
OUTPUT_PATH = os.path.abspath('../DiCaro/Exercise4/resources/output.txt')
CLUSTER_STEP = [6, 5, 4, 3, 2]
MOST_COMMON_WORDS = 15
MIN_FREQUENCY = 3


def main():
    for step in CLUSTER_STEP:
        print("CLUSTERING WITH STEP:", step)
        sentences = process_file(INPUT_PATH)
        clustered_sentences = cluster_sentences(sentences, break_points=[*range(step, len(sentences), step)])
        plot.print_table(clustered_sentences, MOST_COMMON_WORDS, OUTPUT_PATH, step)
        average_list, global_average = similarity.compute_similarity(clustered_sentences)
        min_list = text_tiling(average_list, global_average)
        plot.text_tiling_graph(average_list, min_list, global_average, step)

        print("\n CONCEPT FROM DEFINITIONS\n")
        text_tiling_cluster = cluster_sentences(sentences, [*map(lambda x: x[1], min_list)])
        concept_list = wordnet.genus_differentia(
            [*map(lambda x: utility.filter_by_frequency(x, MIN_FREQUENCY), text_tiling_cluster)]
        )
        utility.write_on_file(concept_list, OUTPUT_PATH)


def process_file(path: str) -> list:
    """
    Read the file and extract sentences, then cluster them
    :param path: file path to read
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

    return cleaned_sentences


def cluster_sentences(sentences: list, break_points: list):
    table_sentence = []
    counter = Counter()
    for i in range(len(sentences)):
        counter = counter + sentences[i]
        if (i in break_points or i == len(sentences) - 1) and len(counter.keys()) > 0:
            table_sentence.append(counter.copy())
            counter.clear()

    return table_sentence


def text_tiling(local_values: list, average: int):
    local_mins = []
    for i, value in enumerate(local_values):
        if i == 0 or i == len(local_values) - 1:
            continue
        if is_local_min(value, local_values[i - 1], local_values[i + 1], average):
            local_mins.append((value, i))

    return local_mins


def is_local_min(value: int, prev: int, follow: int, average: int) -> bool:
    """ Return true if value is lower then global average, min then previous and under follow """
    return value < average and (prev > value < follow)
