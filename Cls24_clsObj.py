class Calculator:

    def __init__(self):
        pass

    def addition(self, *numbers):
        sum = 0
        for number in numbers:
            sum += number
        print(f"The sum is: {sum}")

    def subtraction(self, num1, num2, num3):
        result = num1 - (num2 + num3)
        print(f"Subtraction result is: {result}")

    def divition(self, num1, num2):
        try:
            print(f"The divided result is: {(num1 / num2):.2f}")
        except Exception as ex:
            print("Pound Error, Please try again.")

    def multiplication(self, num1, num2):
        result = num1 * num2
        print(f"Multiplication result is: {result}")

    def __del__(self):
        print("Closed the programme.")


Multi1 = Calculator()
Multi1.multiplication(12, 10)

Div1 = Calculator()
Div1.divition(12, 5)

Sub1 = Calculator()
Sub1.subtraction(23, 3, 10)

ADD = Calculator()
ADD.addition(2, 3, 4, 5, 6, 7)