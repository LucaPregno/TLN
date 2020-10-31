from nltk import pos_tag

import DiCaro.Utility.parser as parser
from nltk.corpus import brown
from DiCaro.Exercise3.verb import Verb
from DiCaro.Utility import resources


def main(*words: str):
    for word in words:
        verb = extract_from_corpus(word)
        # print(verb.print())
        # print(verb.filler_frequency())


def extract_from_corpus(word: str):
    sentences = brown.sents()
    lemma = parser.lemmatizer.lemmatize(word)
    verb = Verb()
    for sentence in sentences:
        if lemma not in parser.lemmer_set(sentence):
            continue
        if is_verb(lemma, sentence):
            s = ""
            for w in sentence:
                s += w + " "
            parser.get_hanks_verb(verb, s, word)

    return verb


def is_verb(lemma: str, sentence) -> bool:
    tag = pos_tag(sentence)
    for t in tag:
        if lemma in t[0] and "VB" in t[1]:
            return True
    return False
