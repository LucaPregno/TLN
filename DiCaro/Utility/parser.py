import spacy
from nltk import word_tokenize, pos_tag, WordNetLemmatizer, PorterStemmer, Counter
from nltk.corpus import stopwords
from DiCaro.Utility import utility, resources
from DiCaro.Utility.wordnet import lesk

LEMMER = "lemmer"
LEMMER_SET = "lemmer_set"
lemmatizer = WordNetLemmatizer()
STEMMER = "stemmer"
STEMMER_SET = "stemmer_set"
stemmatizer = PorterStemmer()

SPACY_CORE = 'en_core_web_sm'
nlp = spacy.load(SPACY_CORE)


def pos(sentence):
    token = word_tokenize(sentence)
    return pos_tag(token)


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
            lemma = lemmatizer.lemmatize(t)
            lemmed.add(lemma)
            print(t, " ==> ", lemma)
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


def rm_stopwords_punctuation(sentence: str, language="english", stamp=False) -> Counter:
    tokens = word_tokenize(sentence)
    if len(tokens) > 0:
        tokens[0] = tokens[0].lower()
    sentence = Counter(tokens)
    stopwords_list = set(stopwords.words(language))
    stop_punctuation = stopwords_list.union(resources.punctuation)
    filtered = utility.remove(sentence, stop_punctuation)
    if stamp:
        print("---Removing Stopwords---")
        print("Stopwords in", language, ":", stopwords_list)
        print("Sentence with stopwords and punctuation removed:\n", filtered)
    return filtered


def cleaning(sentence: str, method: str, frequency: int = 0, percentage: int = 0):
    """
    :param sentence: Definition to clean
    :param method: string which define which method to call
    :param frequency: if not None define minimum number of words repetition
    :param percentage: percentage of the highest frequent words to take
    :return Counter(key=word,value=frequency): sentence cleaned
    """
    tokenized: Counter = rm_stopwords_punctuation(sentence)
    tokenized = utility.remove_number_key(tokenized, minimum=1950, maximum=2030)
    if frequency > 0:
        # Filtering only words with at least frequency occurrences
        filtered = dict(filter(lambda x: x[1] >= frequency, tokenized.items()))
        i = 1
        while len(filtered) <= 0:
            filtered = dict(filter(lambda x: x[1] >= frequency-i, tokenized.items()))
            i += 1
        return globals()[method](Counter(filtered))
    # If a percentage is defined take the first elements (based on percentage), otherwise take everything
    elif percentage > 0:
        percentage = int((percentage/100) * len(tokenized))
        most_common = tokenized.most_common(percentage)
        tokenized = Counter(dict(filter(lambda elem: elem[0] in dict(most_common).keys(), tokenized.items())))

    return globals()[method](tokenized)


def get_dependency(sentence: str, word: str) -> dict:
    """
    Create the verb with its slots.
    Words are assigned to the slot with number equal to the index of the value
    they correspond to in the "resources.arguments" list.
    :param sentence: From which to extract subject and complement
    :param word: word that must be a verb
    """
    doc = nlp(sentence)
    print(sentence)
    dep_dictionary = dict()

    for token in doc:
        if token.dep_ in resources.arguments and word in token.head.lemma_:
            print(token.lemma_, token.pos_, token.dep_, "HEAD:", token.head.text)
            lemma = token.lemma_
            tag = token.pos_
            # If it is a pronoun spacy write -PRON- as lemma
            if tag in resources.pronoun:
                ambiguous = catalogue_ambiguous_terms(token.text.lower())
                dep_dictionary[token.text.lower()] = ambiguous
            else:
                synset = lesk(word=lemma, sentence=sentence)
                if synset is not None:
                    dep_dictionary[lemma] = synset.lexname()

    print(dep_dictionary)
    return dep_dictionary


def catalogue_ambiguous_terms(word: str):
    for key in resources.super_sense_dictionary.keys():
        if word.lower() in key:
            return resources.super_sense_dictionary[key]

    return "noun.entity"
