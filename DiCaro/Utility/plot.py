import matplotlib.pyplot as plt
from collections import Counter
from DiCaro.Utility import resources


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


