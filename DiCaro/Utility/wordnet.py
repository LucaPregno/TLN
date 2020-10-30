from collections import Counter
from nltk.corpus import wordnet
from DiCaro.Utility import resources, parser


def genus_differentia(table: list):
    """
    For each table row (concept definition) calculate highest intersection between
    the row words with the related (hypernyms, hyponyms, siblings) definition of the corresponding synsets.
    :param table: list of most frequent words in every definitions grouped by concept
    :return concepts: list of concept with his associated score
    """
    concepts = list()
    for sentence in table:
        siblings = related_synsets = set()
        best_synset = None
        best_score = 0
        for word in sentence:
            synsets = wordnet.synsets(word)
            for hyper in get_hypernyms(synsets):
                siblings = siblings.union(hyper.hyponyms())
            related_synsets.update(synsets, get_hyponyms(synsets), siblings)

            for related in related_synsets:
                new_synset, new_score = bag_of_words_weighted(related, sentence)
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


def lesk(word: str, sentence: str):
    """
    If word is a pronoun return person synset, otherwise apply lesk algorithm
    :param word: word needs to be disambiguated
    :param sentence: used to disambiguate
    :return: synset with best intersection between phrase and word context
    """
    # If the word is catalogued return
    ambiguous = catalogue_ambiguous_terms(word)
    if ambiguous is not False:
        return ambiguous

    synsets = wordnet.synsets(word)
    sentence = set(parser.cleaning(sentence=sentence, method=parser.LEMMER))
    best_synset = None
    best_score = 0
    for synset in synsets:
        new_synset, new_score = bag_of_words(synset, sentence)
        if new_score > best_score:
            best_score = new_score
            best_synset = new_synset
    return best_synset


def catalogue_ambiguous_terms(word):
    ambiguous = resources.super_sense_dictionary.keys()
    if word[0].isupper() or word in ambiguous:
        word = word.lower()
        # If the word is a dictionary key return correspondent synset
        for key in ambiguous:
            if word in key:
                value = resources.super_sense_dictionary[key]
                return wordnet.synset(value)
        # Proper Noun
        return wordnet.synset("entity.n.01")

    return False
