from collections import Counter
from nltk.corpus import wordnet
import DiCaro.Utility.parser_utility as parser


def get_concept(table: list):
    """
    For each table row (concept definition) calculate the highest intersection between
    the row words with the related (hypernyms, hyponyms, siblings) definition of the corresponding synsets.
    :param table: list of most frequent words in every definitions grouped by concept
    :return concepts: list of concept with his associated score
    """
    concepts = list()
    for row in table:
        hypernyms = hyponyms = siblings = related_synsets = set()
        best_synset = None
        best_score = 0
        for word in row:
            synsets = wordnet.synsets(word)
            hypernyms = get_hypernyms(synsets)
            for hyper in hypernyms:
                siblings = hyper.hyponyms()
            related_synsets.update(synsets, hypernyms, get_hyponyms(synsets), siblings)

            for related in related_synsets:
                new_synset, new_score = bag_of_words_weighted(related, row)
                if new_score > best_score:
                    best_score = new_score
                    best_synset = new_synset

        concepts.append([best_synset, best_score])
    return concepts


def get_hypernyms(synsets) -> set:
    hypernyms = set()
    for s in synsets:
        for hypernym in s.hypernyms():
            hypernyms.add(hypernym)
    return hypernyms


def get_hyponyms(synsets) -> set:
    hyponyms = set()
    for s in synsets:
        for hyponym in s.hyponyms():
            hyponyms.add(hyponym)
    return hyponyms


def get_context(synsets) -> str:
    context = synsets.definition()
    for e in synsets.examples():
        context += e
    return context


def bag_of_words(synset, term_dictionary: set) -> tuple:
    synset_context = set(parser.cleaning(get_context(synset), parser.LEMMER).keys())
    intersection = synset_context.intersection(term_dictionary)
    return synset, len(intersection)


def bag_of_words_weighted(synset, term_dictionary: Counter) -> tuple:
    score = 0
    synset_context = set(parser.cleaning(get_context(synset), parser.LEMMER).keys())
    for word in synset_context:
        if term_dictionary[word] >= 0:
            score += term_dictionary[word]
    return synset, score
