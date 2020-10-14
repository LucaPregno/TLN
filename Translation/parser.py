from nltk import pos_tag, word_tokenize, ne_chunk, load, RecursiveDescentParser
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from Translation.Model.dictionary import translation_dictionary
import Translation.Grammar.utility as grammar_utility


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


def parsing(phrases, grammar=load(grammar_utility.grammar_url), draw_tree: bool = False):
    rd = RecursiveDescentParser(grammar)
    tree_list = []
    print("---Parsing---")
    for i in range(len(phrases)):
        print("Sentence", i, ":", phrases[i])
        sentence_split = phrases[i].split()
        parsed_tree = rd.parse(sentence_split)
        print("Parsing tree:")
        tree_list.append(translate_tree(parsed_tree, draw_tree))
        print("------------------")
    return tree_list


def translate_tree(parsed_tree, draw_tree: bool):
    """
    Translate the tree leaves using a dictionary
    :param parsed_tree: An iterator of all parses
    :param draw_tree: boolean to choose if draw the tree
    :return: translated tree
    """
    for tree in parsed_tree:
        if draw_tree:
            tree.draw()
        print("Tree before translation")
        print(tree)
        for position in tree.treepositions('leaves'):
            tree[position] = translation_dictionary[tree[position]]
        print("Tree after translation")
        print(tree)

        return tree

