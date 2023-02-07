# Write a program in Python to display the first 10 natural numbers.
for start in range(1,11,1):
    print(start,end=" ")


print()
# Write a Python program to find the sum of first 10 natural numbers.
print("\nThe first 10 natural number is :")
lista = []
for start in range(1,11,1):
    print(start,end=" ")
    lista.append(start)
print(f"\nThe Sum is : {sum(lista)}")


print()
# Write a program in Python to display n terms of natural number and their sum.
n = int(input("Enter a Test Data: "))
suma = 0
print("The first 7 natural number is :")
for x in range(1,n+1,1):
    print(x,end=" ")
    suma +=x
print()
print(f"The Sum of Natural Number upto {n} terms : {suma}")


print()
# Write a program in Python to read 10 numbers from keyboard and find their sum and average.
print("Input the 10 numbers :")
lista2 = []
for a in range(10):
    num = int(input())
    lista2.append(num)
print(f"The sum of 10 no is : {sum(lista2)}")
print(f"The Average is : {sum(lista2)/10}")


print()
# Write a program in Python to display the cube of the number upto given an integer.
number = int(input("Input number of terms: "))
for y in range(1,number+1,1):
    print(f"Number is : {y} and cube of the {y} is : {y**3}")


print()
# Write a program in Python to display the pattern like right angle triangle using an asterisk.
print("The pattern like :")
turn = int(input("Enter a number for make pattern: "))
for N in range(1,turn+1,1):
    print(N*"*")