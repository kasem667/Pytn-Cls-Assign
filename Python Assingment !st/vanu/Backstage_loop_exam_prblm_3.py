test_case = int(input())
i = 1
while i <= test_case:
    chocolates = int(input())
    if chocolates % 2 == 0:
        print("Yes")
    else:
        print("No")
    i += 1
