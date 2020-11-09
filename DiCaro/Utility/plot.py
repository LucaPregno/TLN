import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from numpy import *
from collections import Counter
from prettytable import PrettyTable, FRAME, NONE
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


def print_table(cluster_table: list, most_common: int, file_path: str, step: int):
    keys, frequency_matrix = utility.get_frequency_matrix(cluster_table, most_common)
    # Header
    table = PrettyTable()
    table.field_names = ["Words"] + [i for i in range(0, len(cluster_table), 1)]
    # Body
    for i, k in enumerate(keys):
        table.add_row([k] + list(frequency_matrix[i]))

    table.vrules = NONE
    plt.title(f'Cohesion function with cluster of {step}')
    print(table)
    # Prints table on file
    # table_txt = table.get_string()
    # with open(file_path, 'a') as file:
    #     file.write(table_txt)
    # file.close()


def text_tiling_graph(average_list: list, min_list: list, global_average: int, step: int):
    x = range(0, len(average_list) * step, step)
    y = average_list
    for x_min in min_list:
        plt.axvline(x_min[1]*step, color="r")
    plt.axhline(global_average, color="blue")
    plt.plot(x, y, color="black")
    legend_elements = [Line2D([0], [0], color='r', label='Local min'),
                       Line2D([0], [0], color='blue', label='Average'),
                       Line2D([0], [0], color='black', label='Cohesion')]
    plt.xlabel("Sentences")
    plt.ylabel("Cohesion")
    plt.legend(handles=legend_elements)
    plt.show()
