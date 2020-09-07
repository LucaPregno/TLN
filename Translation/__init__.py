# nltk.download()
from Translation.Utility import tokenize, stemmer, pos, lemmer, remove_stopwords
from nltk import pos_tag, word_tokenize
from nltk import sent_tokenize


def main():
    sentence_list = ["Paolo loves Francesca", "You are imagining things", "the man who likes skating"]
    print("Sentence list:", sentence_list)
    tokenized = tokenize(sentence_list)
    tagged = pos(tokenized)
    stemmed = stemmer(tokenized)
    lemmed = lemmer(tokenized)
    stopwords_removed = remove_stopwords(tokenized)


if __name__ == '__main__':
    main()
