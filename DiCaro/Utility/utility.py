from collections import Counter


def remove(multiset1: Counter, multiset2: Counter):
    """ :return: the result of removing second multiset elements from first one """
    for m1 in multiset2:
        del multiset1[m1]
    return multiset1
