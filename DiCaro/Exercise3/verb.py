from collections import Counter


class Verb:
    def __init__(self, *slots: dict):
        self.arguments: list = [dict(), dict()]
        for slot in slots:
            self.arguments.append(slot)

    def print(self):
        for i, slot in enumerate(self.arguments):
            print("Slot", i)
            print("Filler", slot)

    def append_slot(self, slot: dict):
        self.arguments.append(slot)

    def add_filler(self, filler_key: str, filler_value, slot_index: int):
        """
        Add filler in the specified slot number, if there aren't enough slot add empty sets
        :param filler_key: filler key (string) to add
        :param filler_value: filler value (synset) to add
        :param slot_index: slot number designed for the filler
        :return:
        """
        if len(self.arguments) <= slot_index:
            for i in range(len(self.arguments) - slot_index + 1):
                self.arguments.append(dict())

        self.arguments[slot_index][filler_key] = filler_value

    def filler_frequency(self) -> list:
        frequency_list = []
        for a in self.arguments:
            counter = Counter(a.values())
            frequency_list.append(counter)
        return frequency_list


class Sentence:
    def __init__(self, sentence: str, subj: str, obj: str):
        self.sentence = sentence
        self.subj = subj
        self.obj = obj
