import matplotlib.pyplot as plt
from numpy import *
from collections import Counter
from prettytable import PrettyTable, ALL, FRAME, NONE
from DiCaro.Utility import resources, utility


def plot_cluster(word: str, sem_types: Counter):
    print(sem_types)
    sem_types = dict(sem_types.most_common(10))
    sem_type_relation = []
    for keys in sem_types.keys():
        name = ""
        for key in keys:
            name += key + " "
        sem_type_relation.append(name)

    fig, ax = plt.subplots()

    ax.barh(sem_type_relation, list(sem_types.values()))
    ax.set_yticks(sem_type_relation)
    ax.set_yticklabels(sem_type_relation)
    ax.invert_yaxis()
    ax.set_xlabel('Frequency')
    ax.set_title(f'{word.upper()} verb with {len(resources.arguments)} arguments')
    plt.show()


def print_table(cluster_table: list, most_common: int):
    keys, frequency_matrix = utility.get_frequency_matrix(cluster_table, most_common)
    # Header
    table = PrettyTable()
    table.field_names = ["Words"] + [i for i in range(0, len(cluster_table), 1)]
    # Body
    for i, k in enumerate(keys):
        table.add_row([k] + list(frequency_matrix[i]))

    table.vrules = FRAME
    print(table)



