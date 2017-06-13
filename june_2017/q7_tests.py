import numpy as np
from random import randint

MAX_N = 10 ** 5
MAX_Q = 10 ** 4


def test():
    for i in xrange(MAX_Q):
        A = np.random.choice(MAX_N, MAX_N, replace=True)
        length = randint(1, MAX_N)
        a = randint(MAX_N - length)
        b = a + length
        c = randint(MAX_N - length)
        d = c + length


