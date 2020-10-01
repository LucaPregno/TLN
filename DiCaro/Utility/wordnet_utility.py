from collections import Counter
from nltk.corpus import wordnet
import DiCaro.Utility.parser_utility as parser


def get_concept(table: list):
    """
    For each table row (concept definition) calculate the highest intersection between
    the row words with the related (hypernyms, hyponyms, siblings) definition of the corresponding synsets.
    :param table:
    :return:
    """
    concepts = list()
    for row in table:
        hypernyms = hyponyms = siblings = related = set()
        best_synset = None
        best_score = 0
        for word in row:
            hypernyms = calculate_hypernyms(word)
            for hyper in hypernyms:
                siblings = hyper.hyponyms()
            related.update(hypernyms, calculate_hyponyms(word), siblings)

            for r in related:
                new_synset, new_score = bag_of_words(r, row.keys())
                if new_score > best_score:
                    best_score = new_score
                    best_synset = new_synset

        concepts.append([best_synset, best_score])
    return concepts


def calculate_hypernyms(name: str) -> set:
    synsets = wordnet.synsets(name)
    hypernyms = set()
    for s in synsets:
        for hypernym in s.hypernyms():
            hypernyms.add(hypernym)
    return hypernyms


def calculate_hyponyms(name: str) -> set:
    synsets = wordnet.synsets(name)
    hyponyms = set()
    for s in synsets:
        for hyponym in s.hyponyms():
            hyponyms.add(hyponym)
    return hyponyms


def bag_of_words(synset, frequent_words: set) -> tuple:
    cleaned_definition = set(parser.cleaning(synset.definition(), parser.LEMMER).keys())
    intersection = cleaned_definition.intersection(frequent_words)
    return synset, len(intersection)
