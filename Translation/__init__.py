# nltk.download()
from Translation.Utility import tokenize, stemmer, pos, lemmer
from nltk import pos_tag, word_tokenize
from nltk import sent_tokenize


def main():
    sentence_list = ["Paolo loves Francesca", "You are imagining things"]
    print("Sentence list:", sentence_list)
    tokenized = tokenize(sentence_list)
    tagged = pos(tokenized)
    stemmed = stemmer(tokenized)
    lemmed = lemmer(tokenized)


if __name__ == '__main__':
    main()
