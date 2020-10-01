from nltk.corpus import wordnet


def calculate_hyponyms(name: str):
    synset = wordnet.synsets(name)
    print(synset)


