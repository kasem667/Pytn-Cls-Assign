test_case = int(input("Enter your test case number: "))
numbers = []
for x in range(test_case):
    num = int(input())
    numbers.append(num)

for i in numbers:
    if i>120:
        break
    else:
        if i%10==0:
            print(i)

