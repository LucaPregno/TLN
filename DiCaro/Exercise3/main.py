import importlib
from nltk.corpus import brown
from DiCaro.Utility.parser_utility import pos


def main(*words: str, corpus: str = 'nltk.corpus.brown'):
    # c = import_corpus(corpus)
    for word in words:
        extract_from_corpus(word)


def import_corpus(corpus: str):
    try:
        modules = importlib.import_module(corpus)
        return modules
    except ImportError:
        print("Import exception occurred")


def extract_from_corpus(word):
    sentences = [s for s in brown.sents() if word in s]
    a = 0


