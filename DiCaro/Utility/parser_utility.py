from nltk import pos_tag, word_tokenize, WordNetLemmatizer, PorterStemmer
from nltk.corpus import stopwords

LEMMER = "lemmer"
STEMMER = "stemmer"
punctuation = {',', ';', '(', ')', '{', '}', ':', '?', '!', '.', "'s"}


def lemmer(tokens, stamp=False):
    lemmed = set()
    lemmatizer = WordNetLemmatizer()
    if stamp:
        print("---Lemming---")
        for i, t in enumerate(tokens):
            l = lemmatizer.lemmatize(t)
            lemmed.add(l)
            print(t, " ==> ", l)
        print("Lemmed:", lemmed)
    else:
        for t in tokens:
            lemmed.add(lemmatizer.lemmatize(t))
    return lemmed


def stemmer(tokens, stamp=False):
    stemmed = set()
    stemmer = PorterStemmer()
    if stamp:
        print("---Stemming---")
        for i, t in enumerate(tokens):
            l = stemmer.stem(t)
            stemmed.add(l)
            print(t, " ==> ", l)
        print("Stemmed:", stemmed)
    else:
        for t in tokens:
            stemmed.add(stemmer.stem(t))
    return stemmed


def rm_stopwords_punctuation(sentence, language="english", stamp=False):
    sentence = set(word_tokenize(sentence))
    stopwords_list = set(stopwords.words(language))
    stop_punctuation = stopwords_list.union(punctuation)
    filtered = sentence.difference(stop_punctuation)
    if stamp:
        print("---Removing Stopwords---")
        print("Stopwords in", language, ":", stopwords_list)
        print("Sentence with stopwords and punctuation removed:\n", filtered)
    return filtered


def cleaning(sentence: str, method: str):
    tokenized = rm_stopwords_punctuation(sentence)
    if method == LEMMER:
        return lemmer(tokenized)
    else:
        return stemmer(tokenized)