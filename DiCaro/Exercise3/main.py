import DiCaro.Utility.parser as parser
from collections import Counter
from nltk import pos_tag
from nltk.corpus import brown
from DiCaro.Utility import resources, plot


def main(*words: str):
    # l = "a", "a", "b", "b", "c"
    # list = [("u", "c"), ("abra", "kadabra")]
    # print(list)
    # counter = Counter()
    # counter.update(list)
    # counter.update("a")
    # print(counter)
    # hola = map(lambda x: counter.update(x), list)
    # print(counter)
    # print(hola)
    for word in words:
        sem_types = extract_from_corpus(word)
        plot.plot_cluster(word, sem_types)


def extract_from_corpus(word: str):
    sentences = brown.sents()
    lemma = parser.lemmatizer.lemmatize(word)
    dependency_list = []
    for sentence in sentences:
        if lemma not in parser.lemmer_set(sentence):
            continue
        if is_verb(lemma, sentence):
            s = ""
            for w in sentence:
                s += w + " "
            dep_dictionary = parser.get_hanks_verb(s, word)
            if len(dep_dictionary.values()) > 0:
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
