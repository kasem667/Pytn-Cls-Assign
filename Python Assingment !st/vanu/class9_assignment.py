#1. Write a Python program to find maximum between two numbers.
num1 = 45
num2 = 54
if num1>num2:
    print(num1)
else:
    print(num2)


#2. Write a Python program to find maximum between three numbers.
num1 = 45
num2 = 54
num3 = 65
if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)


#3. Write a Python program to check whether a number is divisible by 5 and 50 or not.
num = 60
if num%5==0:
    print("The number is Divisible by 5")
if num%50==0:
    print("The number is Divisible by 50")
else:
    print("The number is Not Divisible by 5 and 50")


#4. Write a Python program to check whether a number is negative, positive or zero.
number = 23
if number<0:
    print("Negetive")
elif number>0:
    print("Positive")
else:
    print("Zero")


#5. Write a Python program to check whether a number is even or odd.
x = 13
if x%2==0:
    print("even")
else:
    print("odd")


#6. Write a Python program to check whether a year is leap year or not.
year = 2021
if year%4==0:
    print("Leap Year")
else:
    print("Not Leap year")


#7. Write a Python program to check whether a character is alphabet or not.
cha = "t"
if (cha >= "a" and cha <= "z") or (cha >= "A" and cha <= "Z"):
    print("Alphabet")
else:
    print("Not Alphabet")


#8. Write a Python program to input any alphabet and check whether it is vowel or consonant.
ch = "f"
if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
    print("Vowel")
else:
    print("Consonent")


#9. Write a Python program to input any character and check whether it is alphabet, digit or special character.
charecter = "%"
if (charecter >= "a" and charecter <= "z") or (charecter >= "A" and charecter <= "Z"):
    print("Alphabet")
elif charecter >= "0" and charecter <= "9":
    print("Digit")
else:
    print("special")


#10. Write a Python program to check whether a character is uppercase or lowercase alphabet.
borno = "G"
if borno >= "a" and borno <= "z":
    print("lowercase")
elif borno >= "A" and borno <= "Z":
    print("Uppercase")


