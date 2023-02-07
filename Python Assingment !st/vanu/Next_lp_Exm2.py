numbers = [1, 2, 3, 4]
running_sum = []
sum = 0
for i in range(0,len(numbers)):
    sum += numbers[i]
    running_sum.append(sum)
print(running_sum)
