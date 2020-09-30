def compute_similarity(value_table: dict):
    for elem in value_table:
        n_elem = 0
        average = 0
        for i, definition1 in enumerate(value_table[elem]):
            for j, definition2 in enumerate(value_table[elem], start=i+1):
                min_len = min(len(definition1), len(definition2))
                intersection_len = len(definition1.intersection(definition2))
                similarity = intersection_len/min_len
                n_elem += 1
                average += similarity
        average /= n_elem
        print(f'{elem} with average {average}')


# def compute_similarity(value_table: dict):
#     for elem in value_table:
#         n_elem = 0
#         average = 0
#         for i, definition1 in enumerate(value_table[elem]):
#             for _, definition2 in enumerate(value_table[elem], start=i+1):
#                 min_len = min(sum(definition1.values()), sum(definition2.values()))
#                 intersection_len = sum((definition1 & definition2).values())
#                 similarity = intersection_len/min_len
#                 n_elem += 1
#                 average += similarity
#         average /= n_elem
#         print(f'{elem} with average {average}')
