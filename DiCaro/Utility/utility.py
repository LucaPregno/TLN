import math
from collections import Counter
from functools import reduce
from numpy.core import array, zeros


def get_item(key, counter: Counter) -> Counter:
    return Counter({key: counter[key]})


def remove(multiset: Counter, remove_set: set):
    """ :return: result of removing set elements from first one """
    return Counter(list(filter(lambda key: key not in remove_set, multiset.keys())))


def remove_number_key(multiset: Counter, minimum: int = math.inf, maximum: int = -math.inf):
    """
    Remove counter element that have a number (outside of range) as key
    :param multiset:
    :param minimum:
    :param maximum:
    :return:
    """
    elem_to_remove = set()
    for key in multiset.keys():
        if key.isnumeric():
            if int(key) < minimum or int(key) > maximum:
                elem_to_remove.add(key)

    return remove(multiset, elem_to_remove)


def get_frequency_matrix(cluster_table: list, most_common: int):
    # List of most common words
    commons = list(most_common_counter(cluster_table, most_common).keys())

    frequency_matrix = array(
        zeros((len(commons), len(cluster_table))),
        dtype=int
    )
    for j, counter in enumerate(cluster_table):
        for k in counter:
            if k in commons:
                i = commons.index(k)
                frequency_matrix[i][j] = counter[k]
    return commons, frequency_matrix


def most_common_counter(counter_list, most_common: int = 0, step: int = 1):
    sum_counter = Counter()
    for counter in counter_list[::step]:
        sum_counter = sum_counter + counter

    if most_common > 0:
        most = sum_counter.most_common(most_common)
        sum_counter.clear()
        for item in most:
            sum_counter[item[0]] = item[1]

    return sum_counter


# def cluster_sentences(sentences: list, step: int = 4) -> list:
#     table_sentence = []
#     counter = Counter()
#     for i in range(len(sentences)):
#         counter = counter + sentences[i]
#         if i % step == 0 or i == len(sentences):
#             table_sentence.append(counter.copy())
#             counter.clear()
#     print("CLUSTERED SENTENCES WITH STEP", step)
#     print(list(map(print, table_sentence)))
#     return table_sentence
#
#
# def flat_no_duplicate(nested_list: list):
#     """
#     :param nested_list:
#     :return: Flatten nested list without duplicate
#     """
#     keys = []
#     for lst in nested_list:
#         if len(lst) > 0:
#             # Concatenate and flatten the counter dictionary keys
#             if lst[0] is dict or Counter:
#                 keys = reduce(add_not_present, list(lst.keys()), keys)
#             else:
#                 keys = reduce(add_not_present, lst.keys(), keys)
#         # keys.append(
#         #   reduce(lambda first, second: first + [second], list(counter.keys()), [])
#         # )
#     return keys
#
#
# def add_not_present(lst1: list, element: str):
#     if element not in lst1:
#         lst1 = lst1 + [element]
#     return lst1
