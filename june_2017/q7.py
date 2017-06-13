from collections import defaultdict

import math
from random import randint


def get_score(j_to_sum, j_to_log, a, b, c, d, random_number):
    diff_sum_a = j_to_sum[d - 1] - (j_to_sum[c - 2] if c > 1 else 0)
    diff_sum_b = j_to_sum[b - 1] - (j_to_sum[a - 2] if a > 1 else 0)
    diff_log_a = j_to_log[d - 1] - (j_to_log[c - 2] if c > 1 else 0)
    diff_log_b = j_to_log[b - 1] - (j_to_log[a - 2] if a > 1 else 0)
    if diff_log_a == diff_log_b and diff_sum_a == diff_sum_b:
        return "YES"
    elif abs(diff_log_b - diff_log_a) > (6.55 if random_number else 6.0):
        return "NO"
    # elif abs(diff_sum_b - diff_sum_a) < 5:
    #     return "YES"


def get_matching(A, a, b, c, d, value_to_count, j_to_sum, j_to_log, random_number):
    score = get_score(j_to_sum, j_to_log, a, b, c, d, random_number)
    if score:
        return score
    diff_dict = defaultdict(int)
    if a == c and b == d:
        return "YES"
    if c < a:
        tmp1, tmp2 = a, b
        a, b = c, d
        c, d = tmp1, tmp2
    lower_bound = 0
    upper_bound = -1
    if c <= b:
        lower_bound = c
        upper_bound = b
        c = upper_bound + 1
        b = lower_bound - 1
    counter = 0
    for i in xrange(a - 1, b):
        value = A[i]
        diff_dict[value] += 1
        current_count = diff_dict[value]
        number_count = value_to_count.get(value)
        if number_count:
            if number_count % 2 == 0 and current_count > number_count / 2:
                return "NO"
            elif number_count % 2 == 1 and current_count > (number_count + 1) / 2:
                return "NO"
            elif number_count % 2 == 1 and current_count > number_count // 2:
                counter += 1
                if counter > 1:
                    return "NO"

    for i in xrange(c - 1, d):
        diff_dict[A[i]] -= 1
        value = diff_dict[A[i]]
        if value == 0:
            diff_dict.pop(A[i])
        if value < -1:
            return "NO"

    if len(diff_dict) > 2:
        return "NO"
    if len(diff_dict) == 0:
        return "YES"

    for n, diff in diff_dict.iteritems():
        if diff > 0:
            a_prob = n
        if diff < 0:
            b_prob = n

    max_prob = max(a_prob, b_prob)
    min_prob = min(a_prob, b_prob)

    for i in xrange(a - 1, b):
        if min_prob < A[i] < max_prob:
            return "NO"

    for i in xrange(lower_bound, upper_bound + 1):
        if min_prob < A[i] < max_prob:
            return "NO"
    return "YES"

# A = [0, 1, 2, 3, 4, 30, 6, 7, 8, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# get_matching(A, 1, 10, 11, 20)
#


def get_value_to_counter_blow_100(A):
    value_to_count = defaultdict(int)
    values_to_ignores = set()
    for e in A:
        if e not in values_to_ignores:
            value_to_count[e] += 1
            if value_to_count[e] > 7:
                value_to_count.pop(e)
                values_to_ignores.add(e)
    return value_to_count


def get_j_to_log_and_sum(A):
    j_to_sum = [0] * len(A)
    j_to_sum[0] = A[0]
    j_to_log = [0.] * len(A)
    j_to_log[0] = math.log(A[0])
    for j in xrange(1, len(A)):
        j_to_log[j] = j_to_log[j - 1] + math.log(A[j])
        j_to_sum[j] = j_to_sum[j - 1] + A[j]
    return j_to_sum, j_to_log


if __name__ == '__main__':
    T = input()
    random_number = randint(0, 1)
    for _ in xrange(T):
        N, Q = map(int, raw_input().split())
        A = map(int, raw_input().split())
        value_to_count = get_value_to_counter_blow_100(A)
        j_to_sum, j_to_log = get_j_to_log_and_sum(A)
        for _ in xrange(Q):
            a, b, c, d = map(int, raw_input().split())
            result = get_matching(A, a, b, c, d, value_to_count, j_to_sum, j_to_log,
                                  random_number)
            print result
# import numpy as np
# from random import randint
# from datetime import datetime
#
# MAX_N = 10 ** 5
# MAX_Q = 10 ** 2
#
#
# def test():
#     now = datetime.now()
#     A = list(np.random.choice(MAX_N, MAX_N, replace=True))
#     value_to_count = get_value_to_counter_blow_100(A)
#     for i in xrange(MAX_Q):
#
#         length = randint(1, MAX_N)
#         a = randint(1, MAX_N - length)
#         b = a + length
#         c = randint(1, MAX_N - length)
#         d = c + length
#         result = get_matching(A, a, b, c, d, value_to_count)
#         print result
#     print (datetime.now() - now).total_seconds()
#
# if __name__ == '__main__':
#     test()
