def get_good_set(n):
    i = 1
    good_set = set()
    sum_sets = set()
    print_exp = ""
    while len(good_set) < n:
        if i not in sum_sets:
            sum_sets.update({e + i for e in good_set})
            good_set.add(i)
            print_exp += ("%s " % i)
        i += 1

    print print_exp.strip()

if __name__ == '__main__':
    T = input()
    for _ in xrange(T):
        n = input()
        get_good_set(n)


