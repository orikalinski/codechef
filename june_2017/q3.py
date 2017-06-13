def get_best_feast(list_of_numbers):
    positive_feast = list()
    adding_feast = 0
    negative_feast = list()
    for num in list_of_numbers:
        if num >= 0:
            positive_feast.append(num)
        else:
            negative_feast.append(num)
    negative_feast = sorted(negative_feast, key=lambda x: -x)
    current_sum = sum(positive_feast)
    num_of_items = len(positive_feast)

    for num in negative_feast:
        if num <= current_sum + (num_of_items + 1) * num:
            num_of_items += 1
            current_sum += num
        else:
            adding_feast += num

    print current_sum * num_of_items + adding_feast

if __name__ == '__main__':
    T = input()
    for _ in xrange(T):
        N = input()
        list_of_nums = [int(num) for num in raw_input().split()]
        get_best_feast(list_of_nums)

