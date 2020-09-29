# nltk.download()
import Translation.parser as parser_lib
import Translation.simpleNLG as simpleNLG
from Translation.Grammar.utility import grammar_url
from Translation.Model.sentece_plan import SentencePlan


def main():
    sentence_list = ('È la spada laser di tuo padre',
                     'Ha fatto una mossa leale',
                     'Gli ultimi avanzi della vecchia Repubblica sono stati spazzati via',
                     'È una mossa di tuo padre')
    tree_list = parser_lib.parsing(sentence_list)
    simpleNLG.parse_tree_to_sentence_plan(tree_list)


def nltk_methods():
    sentence_list = ["Paolo loves Francesca",
                     "You are imagining things",
                     "the man who likes skating"]
    print("Sentence list:", sentence_list)
    tokenized = parser_lib.tokenize(sentence_list)
    tagged = parser_lib.pos(tokenized)
    stemmed = parser_lib.stemmer(tokenized)
    lemmed = parser_lib.lemmer(tokenized)
    stopwords_removed = parser_lib.remove_stopwords(tokenized)
    entities = parser_lib.chunking(tagged)
    print(entities)


if __name__ == '__main__':
    main()
    # nltk_methods()
