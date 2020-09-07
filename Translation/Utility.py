from nltk import sent_tokenize
from nltk import pos_tag, word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.help import upenn_tagset


def tokenize(phrases, language="english"):
    tokenized = []
    for i in range(len(phrases)):
        tokenized.append(word_tokenize(phrases[i], language=language))

    print("---Tokenization---")
    for i in range(len(tokenized)):
        print("Sentence ", i, "tokenized ", tokenized[i])

    return tokenized


def pos(tokens, language="eng"):
    tagged = []
    for i in range(len(tokens)):
        tagged.append(pos_tag(tokens[i], lang=language))

    print("---PoS Tagging---")
    # print(upenn_tagset()) # show tag meanings
    for i in range(len(tagged)):
        print("Sentence ", i, "tagged ", tagged[i])

    return tagged


def stemmer(tokens):
    stemmed = []
    portStemmer = PorterStemmer()
    print("---Stemming---")

    for t in tokens:
        sentence = []
        for w in t:
            s = portStemmer.stem(w)
            sentence.append(s)
            print(w, " ==> ", s)

        stemmed.append(sentence)

    print("Stemmed:", stemmed)
    return stemmed


def lemmer(tokens):
    lemmed = []
    lemmatizer = WordNetLemmatizer()
    print("---Lemming---")

    for t in tokens:
        sentence = []
        for w in t:
            s = lemmatizer.lemmatize(w)
            sentence.append(s)
            print(w, " ==> ", s)

        lemmed.append(sentence)

    print("Lemmed:", lemmed)
    return lemmed