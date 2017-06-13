import math

e_after_dec_point = math.e % 1
a = 190435
a_value = int(a * math.e)
a_euler_sum = 49290073791
a_loss = a * e_after_dec_point % 1
num_of_valid_cycles = 1 // a_loss


def my_range(start, stop):
    i = start
    while i < stop:
        yield i
        i += 1


def get_euler_sum(n, starting_value=0):
    euler_sum = 0
    euler_param = starting_value
    for i in my_range(1, n + 1):
        euler_param += math.e
        euler_sum += math.floor(euler_param)
        # if i % 100000 == 0:
        #     print i // 100000
    return int(euler_sum)


def get_euler_sum_with_fixed_cycle(n):
    cycles = n // a
    cycles_added_value = (cycles * (cycles - 1) / 2) * a_value * a
    num_to_add = cycles // num_of_valid_cycles
    leftovers = n % a
    leftovers_off_set = cycles * a

    return cycles_added_value + cycles * a_euler_sum + num_to_add + get_euler_sum(leftovers, math.e * leftovers_off_set)


def get_euler_sum_with_converge(n):
    return (n * n * math.e) // 2


if __name__ == '__main__':
    n = input()
    # result1 = get_euler_sum_with_fixed_cycle(n)
    result1 = get_euler_sum_with_converge(n)
    print result1
    # result2 = get_euler_sum(n)
    # print result2 - result1
    # print result1
