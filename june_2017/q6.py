from bisect import bisect_left, bisect_right

small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211,
                223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337,
                347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461,
                463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601,
                607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739,
                743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881,
                883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]


def find_exp(number, prime, lower_bound, upper_bound):
    while upper_bound - lower_bound > 1:
        center = (lower_bound + upper_bound) // 2
        if number % (prime ** center) == 0:
            lower_bound = center
        else:
            upper_bound = center
    return lower_bound


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
            res = 0
            num = a[i]
            if num % prime != 0:
                res = 0
            else:
                exp = 1
                pexp = prime
                while num % pexp == 0:
                    exp *= 2
                    pexp *= pexp
                exp = find_exp(num, prime, exp // 2, exp)
                res += exp
                a[i] //= prime ** exp

            small_prime_dict[prime][i] = (res + small_prime_dict[prime][i - 1]) if i > 0 else res
    return small_prime_dict


if __name__ == '__main__':
    result_arr = []
    N = input()
    a = map(int, raw_input().split())
    Q = input()

    small_primes_dict = get_primes_dict(a)

    indexes = []
    numbers = []
    for i in xrange(len(a)):
        if a[i] > 1:
            indexes.append(i)
            numbers.append(a[i])

    for _ in xrange(Q):
        L, R, X, Y = map(int, raw_input().split())
        result = 0
        for prime in small_primes:
            if X <= prime <= Y:
                result += small_primes_dict[prime][R - 1] - (small_primes_dict[prime][L - 2] if L > 1 else 0)

        if Y > 1000:
            l = binary_search(indexes, L - 1)
            r = binary_search(indexes, R - 1, is_left=False)
            # if r != len(numbers) and numbers[r] == R - 1:
            #     R = r + 1
            # else:
            #     R = r
            #
            for i in xrange(l, r):
                if X <= numbers[i] <= Y:
                    result += 1

        print result
        #result_arr.append(result)
    # for x in result_arr:
    #     print x