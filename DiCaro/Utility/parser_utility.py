from nltk import word_tokenize, WordNetLemmatizer, PorterStemmer, Counter
from nltk.corpus import stopwords
from DiCaro.Utility.utility import remove


LEMMER = "lemmer"
LEMMER_SET = "lemmer_set"
lemmatizer = WordNetLemmatizer()
STEMMER = "stemmer"
STEMMER_SET = "stemmer_set"
stemmatizer = PorterStemmer()
punctuation = {',', ';', '(', ')', '{', '}', ':', '?', '!', '.', "'s"}


def lemmer(tokens) -> Counter:
    lemmed = Counter()
    for k in tokens.keys():
        lemmed.update({lemmatizer.lemmatize(k): tokens[k]})
    return lemmed


def lemmer_set(tokens, stamp=False) -> set:
    lemmed = set()
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


def stemmer(tokens) -> Counter:
    stemmed = Counter()
    for k in tokens.keys():
        stemmed.update({stemmatizer.stem(k): tokens[k]})
    return stemmed


def stemmer_set(tokens, stamp=False) -> set:
    stemmed = set()
    if stamp:
        print("---Stemming---")
        for i, t in enumerate(tokens):
            s = stemmatizer.stem(t)
            stemmed.add(s)
            print(t, " ==> ", s)
        print("Stemmed:", stemmed)
    else:
        for t in tokens:
            stemmed.add(stemmatizer.stem(t))
    return stemmed


def rm_stopwords_punctuation(sentence, language="english", stamp=False) -> Counter:
    sentence = Counter(word_tokenize(sentence))
    stopwords_list = Counter(stopwords.words(language))
    stop_punctuation = stopwords_list + Counter(punctuation)
    filtered = remove(sentence, stop_punctuation)
    if stamp:
        print("---Removing Stopwords---")
        print("Stopwords in", language, ":", stopwords_list)
        print("Sentence with stopwords and punctuation removed:\n", filtered)
    return filtered


def keep_frequency(counter: Counter, frequency: int) -> list:
    """ For each set of the list keep only the word that occur at least frequency times """
    new_concept_table = []
    for word_set in counter:
        word_set = list(word_set)
        new_concept_table.append(set([w for w in word_set if word_set.count(w) >= frequency]))
    return new_concept_table


def cleaning(sentence: str, method: str, frequency: int = None):
    """
    :param sentence: Definition to clean
    :param method: string which define which method to call
    :param frequency: if not None define minimum number of words repetition
    :return: sentence cleaned
    """
    if frequency is None or frequency <= 0:
        tokenized = rm_stopwords_punctuation(sentence)
        return globals()[method](tokenized)
    else:
        tokenized = rm_stopwords_punctuation(sentence)
        # keep_frequency(tokenized, frequency)
        # filtering only words with at least frequency occurrences
        tokenized = dict(filter(lambda x: x[1] >= frequency, tokenized.items()))
        return globals()[method](Counter(tokenized))
