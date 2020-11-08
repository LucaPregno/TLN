import math
from collections import Counter
from numpy.core import array, zeros
from DiCaro.Utility import parser


def get_item(key, counter: Counter) -> Counter:
    return Counter({key: counter[key]})


def filter_by_set(multiset: Counter, remove_set: set) -> Counter:
    """ :return: Result of removing set elements from first one """
    filtered = {key: count for key, count in multiset.items() if key not in remove_set}
    return Counter(filtered)


def filter_by_frequency(multiset: Counter, frequency: int):
    """ :return: Removing elements with count less then frequency """
    filtered = {key: count for key, count in multiset.items() if count >= frequency}
    return Counter(filtered)


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

    return filter_by_set(multiset, elem_to_remove)


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


def write_on_file(concept_list: list, path, frequency: int = 0, percentage: int = 0):
    file = open(path, "a")
    file.write(f'Frequency:{frequency} Percentage:{percentage} Method:{parser.LEMMER}\n\n')
    for i, c in enumerate(concept_list):
        if c[0] is not None:
            line = f'{i}- {c[0]} {c[0].definition()} | Score:{c[1]}'
            print(line)
            file.write(f'{line}\n')
        else:
            print(f'{i}- No synset found')
            file.write(f'{i}- No synset found\n')

    print("\n")
    file.write("\n-------------------------------------------------------------------------\n")
    file.close()
