from collections import Counter


def concept_similarity(value_table: dict):
    for elem in value_table:
        n_elem = average = 0
        for i, definition1 in enumerate(value_table[elem]):
            for j, definition2 in enumerate(value_table[elem], start=i+1):
                min_len = min(len(definition1), len(definition2))
                intersection_len = len(definition1.intersection(definition2))
                similarity = intersection_len/min_len
                n_elem += 1
                average += similarity
        average /= n_elem
        print(f'{elem} with average {average}')


def compute_similarity(sentences_as_counter: list) -> tuple:
    global_average = 0
    local_average = []
    for i, group in enumerate(sentences_as_counter):
        if len(group) >= 0:
            prev_similarity = follow_similarity = 0
            if i > 0:
                prev_similarity = counter_intersection_similarity(group, sentences_as_counter[i-1])
            if i < len(sentences_as_counter) - 1:
                follow_similarity = counter_intersection_similarity(group, sentences_as_counter[i+1])

            group_average = (prev_similarity + follow_similarity)/2
            local_average.append(group_average)
            global_average += group_average
            # print(f'Group number {i} with average {group_average}')

    global_average /= len(sentences_as_counter)
    # print(f'Global average {global_average}')
    return local_average, global_average


def counter_intersection_similarity(counter1: Counter, counter2: Counter):
    cohesion = counter_intersection_length(counter1, counter2)
    min_length = min_counter_length(counter1, counter2)
    # Preventing division by 0
    if min_length > 0:
        return cohesion/min_length
    else:
        return 0


def counter_intersection_length(counter1: Counter, counter2: Counter):
    return sum((counter1 & counter2).values())


def min_counter_length(counter1: Counter, counter2: Counter):
    return min(sum(counter1.values()), sum(counter2.values()))