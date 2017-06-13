T = input()
for _ in xrange(T):
    u, v = map(int, raw_input().split())
    s = u + v
    print ((s + 1) * s / 2 + u + 1)
