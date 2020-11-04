import os
import re
from collections import Counter
from DiCaro.Utility import parser

INPUT_PATH = os.path.abspath('../DiCaro/Exercise4/resources/input.txt')
CLUSTER_STEP = 5


def main():
    sentences = process_file(INPUT_PATH)
    cluster_sentences(sentences)


def process_file(path: str):
    file = open(path, "r")
    sentences = re.split('[.!?]', file.read())
    for s in sentences:
        print(s)
    file.close()
    processed_sentence = []
    for sentence in sentences:
        processed_sentence.append(parser.cleaning(sentence, parser.LEMMER))

    return processed_sentence


def cluster_sentences(sentences):
    step = round(len(sentences) * CLUSTER_STEP/100)
    clustered_sentences = []
    counter = Counter()
    for i in range(len(sentences)):
        counter = counter + sentences[i]
        if i % step == 0 or i == len(sentences):
            clustered_sentences.append((counter.copy(), i))
            counter.clear()
    print("CLUSTERED SENTENCES")
    print(list(map(print, clustered_sentences)))
    # print(clustered_sentences, "\n length:", len(clustered_sentences))





