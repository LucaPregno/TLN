# nltk.download()
import Translation.parser as parser_lib


def main():
    # sentence_list = ["Paolo loves Francesca", "You are imagining things", "the man who likes skating"]
    # print("Sentence list:", sentence_list)
    # tokenized = parserLib.tokenize(sentence_list)
    # tagged = parserLib.pos(tokenized)
    # stemmed = parserLib.stemmer(tokenized)
    # lemmed = parserLib.lemmer(tokenized)
    # stopwords_removed = parserLib.remove_stopwords(tokenized)
    # entities = parserLib.chunking(tagged)
    # print(entities)
    # t = treebank.parsed_sents('wsj_0001.mrg')[0]
    # t.draw()

    sentence_list = ('È la spada laser di tuo padre',
                     'Ha fatto una mossa leale',
                     'Gli ultimi avanzi della vecchia Repubblica sono stati spazzati via',
                     'spazzati via')
    parser_lib.parsing(sentence_list)
    # parserLib.print_grammar_rules()


if __name__ == '__main__':
    main()
