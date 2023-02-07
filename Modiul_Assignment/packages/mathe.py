from math import sqrt


def sum_1_to_n(value):
    if value == 0:
        return 0
    else:
        return value + sum_1_to_n(value - 1)


def even_1_to_n(num):
    value_list = []
    for x in range(1, num+1):
        if x % 2 == 0:
            value_list.append(x)
    numbers = " ".join(map(str, value_list))
    return numbers


def check_prime(num):
    if num == 2:
        return "Prime Number."
    else:
        for x in range(2, int(sqrt(num)) + 1):
            if num % x == 0:
                return "Not Prime."
            else:
                return "Prime Number."


