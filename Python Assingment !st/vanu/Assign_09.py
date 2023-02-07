numbers = list(map(int,input().split()))
numbers1 = "".join(map(str, numbers))
numbers2 = int(numbers1)
numbers3 = numbers2 + 1
numbers4 = str(numbers3)
update_numbers = []
for x in numbers4:
    x = int(x)
    update_numbers.append(x)
print(update_numbers)
