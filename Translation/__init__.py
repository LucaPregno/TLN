# nltk.download()
import Translation.parser as parser_lib
import Translation.simpleNLG as simpleNLG


def main():
    # sentence_list = ["Paolo loves Francesca", "You are imagining things", "the man who likes skating"]
    # print("Sentence list:", sentence_list)
    # tokenized = parser_lib.tokenize(sentence_list)
    # tagged = parser_lib.pos(tokenized)
    # stemmed = parser_lib.stemmer(tokenized)
    # lemmed = parser_lib.lemmer(tokenized)
    # stopwords_removed = parser_lib.remove_stopwords(tokenized)
    # entities = parser_lib.chunking(tagged)
    # print(entities)

    sentence_list = ('È la spada laser di tuo padre',
                     'Ha fatto una mossa leale',
                     'Gli ultimi avanzi della vecchia Repubblica sono stati spazzati via')

    tree_list = parser_lib.parsing(sentence_list)
    simpleNLG.parse_tree_to_sentence_plan(tree_list)


if __name__ == '__main__':
    main()
