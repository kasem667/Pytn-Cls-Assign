count = int(input())
message = input()


def print_this_message(n):
    if n == 0:
        return
    else:
        print(message)
        return print_this_message(n-1)


print_this_message(count)
