
def compute_similarity(value_table: dict):
    for elem in value_table:

        for i, definition1 in enumerate(value_table[elem]):
            for _, definition2 in enumerate(value_table[elem], start=i+1):
                min_len = min(len(definition1), len(definition2))
                intersection_len = len(definition1.intersection(definition2))
                similarity = intersection_len/min_len
                if intersection_len > 0:
                    print(similarity)
