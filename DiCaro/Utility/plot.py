from functools import reduce

import matplotlib.pyplot as plt
from collections import Counter
from DiCaro.Utility import resources
from numpy import *
from DiCaro.Exercise4.main import CLUSTER_STEP


def plot_cluster(word: str, sem_types: Counter):
    print(sem_types)
    sem_types = dict(sem_types.most_common(10))
    sem_type_relation = []
    for keys in sem_types.keys():
        name = ""
        for k in keys:
            name += k + " "
        sem_type_relation.append(name)

    fig, ax = plt.subplots()

    ax.barh(sem_type_relation, list(sem_types.values()))
    ax.set_yticks(sem_type_relation)
    ax.set_yticklabels(sem_type_relation)
    ax.invert_yaxis()
    ax.set_xlabel('Frequency')
    ax.set_title(f'{word.upper()} verb with {len(resources.arguments)} arguments')
    plt.show()


def get_frequency_matrix(cluster_table: list):
    step_list = [i for i in range(0, len(cluster_table), CLUSTER_STEP)]

    frequency_matrix = array(zeros((len(cluster_table), len(step_list))))
    frequency_matrix = insert(frequency_matrix, 0, step_list, axis=0)

    keys = []
    for counter in cluster_table:
        keys.append( reduce(lambda first, second: first + second, list(counter.keys()), "") )

    for i, counter in enumerate(cluster_table):
        for k in counter:
            frequency_matrix[1][i] = counter[k]


def print_table(cluster_table: list):
    get_frequency_matrix(cluster_table)

    a = 0
    sem_type_relation = []
    # for keys in sem_types.keys():
    #     name = ""
    #     for k in keys:
    #         name += k + " "
    #     sem_type_relation.append(name)
    #
    # fig, ax = plt.subplots()
    #
    # ax.barh(sem_type_relation, list(sem_types.values()))
    # ax.set_yticks(sem_type_relation)
    # ax.set_yticklabels(sem_type_relation)
    # ax.invert_yaxis()
    # ax.set_xlabel('Frequency')
    # ax.set_title(f'{word.upper()} verb with {len(resources.arguments)} arguments')
    # plt.show()



