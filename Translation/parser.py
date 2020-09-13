from nltk import pos_tag, word_tokenize, ne_chunk, load, sent_tokenize, RecursiveDescentParser, Tree
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
import Translation.grammars.utility as grammar_utility


def tokenize(phrases, language="english"):
    tokenized = []
    for i in range(len(phrases)):
        tokenized.append(word_tokenize(phrases[i], language=language))

    print("---Tokenization---")
    for i in range(len(tokenized)):
        print("Sentence", i, "tokenized", tokenized[i])

    return tokenized


def pos(tokens, language="eng"):
    tagged = []
    for i in range(len(tokens)):
        tagged.append(pos_tag(tokens[i], lang=language))

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


def remove_stopwords(tokens, language="english"):
    stopwords_removed = []
    stopwords_list = stopwords.words(language)
    print("Stopwords in", language, ":", stopwords_list)
    print("---Removing Stopwords---")

    for t in tokens:
        stopwords_removed.append([word for word in t if word not in stopwords_list])

    print("Stopwords removed:", stopwords_removed)
    return stopwords_removed


def chunking(tagged):
    entities = []
    for i in range(len(tagged)):
        entities.append(ne_chunk(tagged[i]))

    print("---Chunking---")
    for i in range(len(entities)):
        print("Sentence", i, "chunk", entities[i])

    return tagged


dictionary = {
    "Repubblica": "Repubblica",
    "il": "the",
    "la": "the",
    "una": "a",
    "tuo": "your",
    "Gli": "the",
    "spada": "sword",
    "padre": "father",
    "mossa": "move",
    "avanzi": "leftovers",
    "leale": "loyal",
    "ultimi": "last",
    "vecchia": "old",
    "laser": "laser",
    "È": "Is",
    "è": "is",
    "fatto": "done",
    "spazzati": "swept",
    "Ha": "Has",
    "sono": "are",
    "stati": "been",
    "via": "away",
    "in": "in",
    "su": "on",
    "da": "by",
    "con": "with",
    "di": "of",
    "della": "of",
    "cane": "dog",
    "gatto": "cat",
    "rincorre": "chased"
}


def parsing(phrases, grammar=load(grammar_utility.grammar_url)):
    rd = RecursiveDescentParser(grammar)
    print("---Parsing---")
    for i in range(len(phrases)):
        print("Sentence", i, ":", phrases[i])
        sentence = phrases[i].split()
        tree = rd.parse(sentence)
        print("Parsing tree:")
        en_tree = parse_tree_to_sentence_plan(tree)
        print("FINEEE")
        for t in en_tree:
            print(t)
        print("------------------")


def parse_tree_to_sentence_plan(tree):
    pos_tagging = []
    for t in tree:
        print("Tree before", t)
        for position in t.treepositions('leaves'):
            t[position] = dictionary[t[position]]
        print("Tree after", t)
        pos_tagging = t.pos()

    print(pos_tagging)

    for t in tree:
        print("Nuovo", t)
    # for index, subtree in enumerate(tree):
    #     print("Tipo", type(subtree), "label", subtree.label())
    #     if type(subtree) == Tree and subtree.label() in lhs_list:
    #         print("sub", subtree[0])
    #         subtree[0] = dictionary[subtree[0]]

    return tree

