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


def cleaning(sentence: str, method: str, frequency: int = None, percentage: int = 0):
    """
        :param sentence: Definition to clean
        :param method: string which define which method to call
        :param frequency: if not None define minimum number of words repetition
        :param percentage: percentage of the highest frequent words to take
        :return Counter: sentence cleaned
    """
    tokenized: Counter = rm_stopwords_punctuation(sentence)
    if frequency is None or frequency <= 0:
        # If a percentage is defined take the first elements (based on the percentage), otherwise take everything
        if percentage != 0:
            percentage = int((percentage/100) * len(tokenized))
            most_common = tokenized.most_common(percentage)
            tokenized = Counter(dict(filter(lambda elem: elem[0] in dict(most_common).keys(), tokenized.items())))
        return globals()[method](tokenized)
    else:
        # filtering only words with at least frequency occurrences
        f_removed = dict(filter(lambda x: x[1] >= frequency, tokenized.items()))
        i = 1
        while len(f_removed) <= 0:
            f_removed = dict(filter(lambda x: x[1] >= frequency-i, tokenized.items()))
            i += 1
        return globals()[method](Counter(f_removed))
