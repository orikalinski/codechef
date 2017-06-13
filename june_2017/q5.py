import copy
from collections import defaultdict


def get_number_of_union_pairs(K, list_of_elements_set):
    full_set = {i for i in xrange(1, K + 1)}
    item_to_set = defaultdict(set)
    number_of_pairs = 0
    for i in xrange(len(list_of_elements_set)):
        elements_set_length, elements_set = list_of_elements_set[i]
        for element in elements_set:
            item_to_set[element].add(i)

    min_set = min(item_to_set.iteritems(), key=lambda x: len(x[1]))
    relevant_indexes = copy.deepcopy(min_set[1])
    processed = set()
    for i in relevant_indexes:
        elements_set_length, elements_set = list_of_elements_set[i]
        complete_set = full_set - elements_set
        intersect = {j for j in xrange(len(list_of_elements_set)) if j not in processed and j != i}
        list_of_indexes_set = [item_to_set[j] for j in complete_set]
        intersect = intersect.intersection(*list_of_indexes_set)
        if intersect:
            number_of_pairs += len(intersect)
        for j in full_set:
            try:
                item_to_set[j].remove(i)
            except KeyError:
                pass
        processed.add(i)

    print number_of_pairs


if __name__ == '__main__':
    T = input()
    for _ in xrange(T):
        N, K = map(int, raw_input().split())
        list_of_elements_set = list()
        for _ in xrange(N):
            row = map(int, raw_input().split())
            length, elements = row[0], set(row[1:])
            list_of_elements_set.append((length, elements))
        get_number_of_union_pairs(K, list_of_elements_set)
