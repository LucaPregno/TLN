import spacy
from nltk import word_tokenize, pos_tag, WordNetLemmatizer, PorterStemmer, Counter
from nltk.corpus import stopwords
from DiCaro.Utility import utility, resources
from DiCaro.Utility.wordnet import lesk
from DiCaro.Exercise3.verb import Verb


LEMMER = "lemmer"
LEMMER_SET = "lemmer_set"
lemmatizer = WordNetLemmatizer()
STEMMER = "stemmer"
STEMMER_SET = "stemmer_set"
stemmatizer = PorterStemmer()

SPACY_CORE = 'en_core_web_sm'
nlp = spacy.load(SPACY_CORE)


def pos(tokens, language="eng"):
    tagged = []
    for i in range(len(tokens)):
        tagged.append(pos_tag(tokens[i], lang=language))
    return tagged


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
    stop_punctuation = stopwords_list + Counter(resources.punctuation)
    filtered = utility.remove(sentence, stop_punctuation)
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
        :return Counter(key=word,value=frequency): sentence cleaned
    """
    tokenized: Counter = rm_stopwords_punctuation(sentence)
    if frequency is None or frequency <= 0:
        # If a percentage is defined take the first elements (based on percentage), otherwise take everything
        if percentage != 0:
            percentage = int((percentage/100) * len(tokenized))
            most_common = tokenized.most_common(percentage)
            tokenized = Counter(dict(filter(lambda elem: elem[0] in dict(most_common).keys(), tokenized.items())))
        return globals()[method](tokenized)
    else:
        # Filtering only words with at least frequency occurrences
        filtered = dict(filter(lambda x: x[1] >= frequency, tokenized.items()))
        i = 1
        while len(filtered) <= 0:
            filtered = dict(filter(lambda x: x[1] >= frequency-i, tokenized.items()))
            i += 1
        return globals()[method](Counter(filtered))


def get_dependency_tree(verb: Verb, sentence: str):
    """
    Create the verb with its slots.
    Words are assigned to the slot with number equal to the index of the value
    they correspond to in the "resources.arguments" list.
    :param verb: verb to update
    :param sentence: From which to extract subject and complement
    """
    doc = nlp(sentence)
    for token in doc:
        if token.head.pos_ == "VERB" and (token.dep_ in resources.arguments):
            lemma = lemmatizer.lemmatize(token.text)
            synset = lesk(word=lemma, sentence=sentence)
            if synset is not None:
                verb.add_filler(lemma, synset.lexname(), resources.arguments.index(token.dep_))
