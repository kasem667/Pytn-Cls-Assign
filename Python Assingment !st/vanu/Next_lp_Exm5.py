test_case = int(input())
i = 1
while i <= test_case:
    num = int(input())
    if num > 0:
        print("even positiv") if num % 2 == 0 else print("odd positive")
    elif num < 0:
        print("even negative") if num % 2 == 0 else print("odd negative")
    elif num == 0:
        print("null")
    i += 1
