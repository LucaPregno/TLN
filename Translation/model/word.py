class Word:
    def __init__(self, value, tag, index):
        self.value = value
        self.tag = tag
        self.index = index

    def print(self):
        print("Word:", self.value, ", Tag:", self.tag, ", Index:", self.index)


def word_list(index_list, value, tag):
    words_list = []
    for i in index_list:
        words_list.append(Word(value=value, tag=tag, index=i))
    return words_list
