from bisect import bisect_left, bisect_right

BATCH_SIZE = 5000
MAX_SMALL_PRIME = 1000
MAX_NUMBER = 10 ** 6

small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211,
                223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337,
                347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461,
                463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601,
                607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739,
                743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881,
                883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]


def binary_search(a, x, is_left=True):
    if is_left:
        pos = bisect_left(a, x, 0, len(a))
    else:
        pos = bisect_right(a, x, 0, len(a))
    return pos


def get_primes_dict(a):
    small_prime_dict = {}
    for prime in small_primes:
        small_prime_dict[prime] = [0] * N
        for i in xrange(N):
            num = a[i]
            exp = 0
            pexp = 1
            next_pexp = pexp * prime
            while num % next_pexp == 0:
                exp += 1
                pexp = next_pexp
                next_pexp *= prime
            if exp:
                a[i] //= pexp
            small_prime_dict[prime][i] = (exp + small_prime_dict[prime][i - 1]) if i > 0 else exp
    return small_prime_dict


def get_primes_lists(processed_a):
    num_of_batches = MAX_NUMBER / BATCH_SIZE
    indexes_per_batch = [list() for _ in xrange(num_of_batches)]
    full_indexes_per_batch = [[0] * len(processed_a) for _ in xrange(num_of_batches)]
    primes_per_batch = [list() for _ in xrange(num_of_batches)]
    for i, prime in enumerate(processed_a):
        batch = prime // BATCH_SIZE
        for j in xrange(num_of_batches):
            full_indexes_per_batch[j][i] = (full_indexes_per_batch[j][i - 1] + 1) if prime != 1 and batch == j \
                else full_indexes_per_batch[j][i - 1]
        if prime == 1:
            continue
        indexes_per_batch[batch].append(i)
        primes_per_batch[batch].append(prime)
    return full_indexes_per_batch, indexes_per_batch, primes_per_batch


if __name__ == '__main__':
    N = input()
    a = map(int, raw_input().split())
    Q = input()

    small_primes_dict = get_primes_dict(a)

    full_indexes_per_batch, indexes_per_batch, primes_per_batch = get_primes_lists(a)

    for _ in xrange(Q):
        L, R, X, Y = map(int, raw_input().split())
        result = 0
        if X < MAX_SMALL_PRIME:
            for prime in small_primes:
                if X <= prime <= Y:
                    result += small_primes_dict[prime][R - 1] - (small_primes_dict[prime][L - 2] if L > 1 else 0)

        if Y > MAX_SMALL_PRIME:
            slice_X = X // BATCH_SIZE
            slice_Y = Y // BATCH_SIZE
            large_X = ((slice_X + (1 if X % BATCH_SIZE != 0 else 0)) * BATCH_SIZE)
            small_Y = ((slice_Y * BATCH_SIZE) - 1) if ((Y + 1) % BATCH_SIZE != 0) else Y

            large_x_slice = large_X // BATCH_SIZE
            for i in xrange(large_X, small_Y, BATCH_SIZE):
                current_indexes_list = full_indexes_per_batch[large_x_slice]
                large_x_slice += 1
                result += current_indexes_list[R - 1] - (current_indexes_list[L - 2] if L > 1 else 0)

            if X != large_X:
                lower_bound_indexes_list = indexes_per_batch[slice_X]
                lower_bound_primes_list = primes_per_batch[slice_X]
                l = binary_search(lower_bound_indexes_list, L - 1)
                r = binary_search(lower_bound_indexes_list, R - 1, is_left=False)
                for i in xrange(l, r):
                    if X <= lower_bound_primes_list[i] <= Y:
                        result += 1

            if slice_X != slice_Y and Y != small_Y and Y != MAX_NUMBER:
                upper_bound_indexes_list = indexes_per_batch[slice_Y]
                upper_bound_primes_list = primes_per_batch[slice_Y]
                l = binary_search(upper_bound_indexes_list, L - 1)
                r = binary_search(upper_bound_indexes_list, R - 1, is_left=False)
                for i in xrange(l, r):
                    if X <= upper_bound_primes_list[i] <= Y:
                        result += 1

        # if result == 0:
        #     print L, R, X, Y
        print L, R, X, Y, result
