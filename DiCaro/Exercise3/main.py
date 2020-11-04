from collections import Counter
from nltk import pos_tag
from nltk.corpus import brown
from DiCaro.Utility import parser, resources, plot


def main(words: list):
    for word in words[:-1]:
        sem_types = extract_sem_types(word)
        plot.plot_cluster(word, sem_types)


def extract_sem_types(word: str):
    sentences = brown.sents()
    lemma = parser.lemmatizer.lemmatize(word)
    dependency_list = []
    for sentence in sentences:
        if lemma not in parser.lemmer_set(sentence):
            continue
        if is_verb(lemma, sentence):
            s = ""
            for token in sentence:
                s += token + " "
            dep_dictionary = parser.get_dependency(s, word)
            # Values extracted must be the same number of arguments
            if len(dep_dictionary.values()) == len(resources.arguments):
                dependency_list.append(dep_dictionary)

    sem_types = semantic_type_cluster(dependency_list)
    return sem_types


def is_verb(lemma: str, sentence: str) -> bool:
    tag = pos_tag(sentence)
    for t in tag:
        if lemma in t[0] and "VB" in t[1]:
            return True
    return False


def semantic_type_cluster(sentence_list):
    couple_list = []
    for sentence in sentence_list:
        couple_list.append(tuple(sentence.values()))
    counter = Counter(couple_list)

    return counter
