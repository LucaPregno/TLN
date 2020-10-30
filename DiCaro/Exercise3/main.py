import importlib
import DiCaro.Utility.parser as parser
from nltk.corpus import brown
from DiCaro.Exercise3.verb import Verb


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
    verb = Verb()
    for sentence in sentences:
        s = ""
        for w in sentence:
            s += w + " "
        parser.get_dependency_tree(verb, s)
    print(verb.print())
    a = 0


