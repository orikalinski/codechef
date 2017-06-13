from random import sample, randint

N = randint(1, 100000)
MAX_NUMBER = 10 ** 6
a = sample(range(2, MAX_NUMBER), N)
Q = randint(1, 100000)

with open("input.txt", "wb") as f:
    f.write("%s\n%s\n%s\n" % (N, " ".join(map(str, a)), Q))
    for _ in xrange(Q):
        L = randint(1, N)
        R = randint(L, N)
        X = randint(2, MAX_NUMBER)
        Y = randint(X, MAX_NUMBER)
        f.write("%s %s %s %s\n" % (L, R, X, Y))

