def get_sum_f(A, B, C):
    s = 0
    A = sorted(A)
    C = sorted(C)
    B = sorted(B)
    a_length = len(A)
    c_length = len(C)
    sum_a = 0
    sum_c = 0
    k = 0
    m = 0
    for b in B:
        for i in xrange(k, a_length):
            if b < A[i]:
                break
            k += 1
            sum_a += A[i]
        for i in xrange(m, c_length):
            if b < C[i]:
                break
            m += 1
            sum_c += C[i]
        x = b * b
        s += (k * m * x) + (b * m * sum_a) + (b * k * sum_c) + (sum_a * sum_c)
        if s > 1000000007:
            s %= 1000000007

    print s

if __name__ == '__main__':
    T = input()
    for _ in xrange(T):
        lengths = map(int, raw_input().split())
        A = map(int, raw_input().split())
        B = map(int, raw_input().split())
        C = map(int, raw_input().split())
        get_sum_f(A, B, C)
