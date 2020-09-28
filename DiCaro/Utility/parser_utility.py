from nltk import pos_tag, word_tokenize, WordNetLemmatizer, PorterStemmer
from nltk.corpus import stopwords

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


def tokenize(phrases, language="english", stamp=False):
    tokenized = []
    for i in range(len(phrases)):
        tokenized.append(word_tokenize(phrases[i], language=language))
    if stamp:
        print("---Tokenization---")
        for i in range(len(tokenized)):
            print("Sentence", i, "tokenized", tokenized[i])
    return tokenized


def pos(tokens, language="eng", stamp=False):
    tagged = []
    for i in range(len(tokens)):
        tagged.append(pos_tag(tokens[i], lang=language))
    if stamp:
        print("---PoS Tagging---")
        # print(upenn_tagset()) # show tag meanings
        for i in range(len(tagged)):
            print("Sentence", i, "tagged", tagged[i])
    return tagged


def stemmer(tokens):
    stemmed = []
    port_stemmer = PorterStemmer()
    print("---Stemming---")
    for t in tokens:
        sentence = []
        for w in t:
            s = port_stemmer.stem(w)
            sentence.append(s)
            print(w, " ==> ", s)
        stemmed.append(sentence)
    print("Stemmed:", stemmed)
    return stemmed
