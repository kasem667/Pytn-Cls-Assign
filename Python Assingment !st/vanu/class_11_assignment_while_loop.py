# Write a program in Python to display the first 10 natural numbers.
i = 1
while i <= 10:
    print(i)
    i = i+1


# Write a Python program to find the sum of first 10 natural numbers.
print("The first 10 natural number is :")
suma = 0
i = 1
while i <= 10:
    suma = suma+i
    print(i)
    i = i+1
print("The sum is:", suma)


# Write a program in Python to display n terms of natural number and their sum.
terms = int(input())
i = 1
sum = 0
print(f"The first {terms} natural number is :")
while i <= terms:
    sum = sum + i
    print(i)
    i = i+1
print(f"The Sum of Natural Number upto {terms} terms : {sum}")


# Write a program in Python to read 10 numbers from keyboard and find their sum and average.
sum = 0
i = 1
print("Input the 10 numbers :")
while i<=10:
    num = int(input())
    sum = sum + num
    i = i+1
print("The sum of 10 numbers is:",sum)
print("Avarege is:",(sum/10))


# Write a program in Python to display the cube of the number upto given an integer.
turn = int(input("Input number of terms : "))
start = 1
while start<=turn:
    print(f"Number is : {start} and cube of the {start} is :{start**3}")
    start = start+1


# Write a program in Python to display the pattern like right angle triangle using an asterisk.
close = int(input())
i = 1
while i<=close:
    print(i*"*")
    i = i+1


'''
Problem 01
2nd ass:-
1-20 even print korbe 
R 
19 break 
R odd print korbe na
'''
#Ans:
while True:
    num =int(input())
    if num%2==0:
        print(num)
    if num==19:
        break
    if num%2==1:
        continue
