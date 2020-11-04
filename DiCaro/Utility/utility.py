import math
from collections import Counter


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
