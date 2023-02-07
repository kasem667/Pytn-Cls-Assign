# 1. Write a python program to create a lambda function that takes one argument,
# and that argument will be multiplied with a number.
add = (lambda x: x * 5)
print(add(10))


# 2. Write a Python Program to count the even, odd numbers in a given list of integers using lambda function
# lst = [Comprehension]
# Total Even: Lambda function
# Total Odd: Lambda function
list1 = [number for number in range(1, 10, 1)]
print(list1)
count_even = len(list(filter(lambda x: x % 2 == 0, list1)))
print("Even numbers:", count_even)
count_odd = len([value for value in list1 if value % 2 != 0])
print("Odd numbers:", count_odd)


# 3. Write a python program to create a lambda function that add 15 to a given number passed in as an arguments.
# also create a lambda function that multiplies argument x with argument y and print the result. [Lambda Function]
new_numbers = (lambda x: x + 15)
print(new_numbers(50))

add_2_number = (lambda x, y: x + y)
print(add_2_number(12, 13))

