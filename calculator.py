# calculator project in python 
# version 1.2

import math

class Calculator:

    def addition(self,number1,number2):
        return number1 + number2
        
    def subtraction(self,number1,number2):
        return number1 - number2

    def multiplication(self,number1,number2):
        return number1 * number2
      
    def division(self,number1,number2):
        return number1 / number2
       
    def sqroot(self,number1):
        return math.isqrt(number1)

    def exponential(self,number1,number2):
        return number1 ** number2
        
    def division_rest(self,number1,number2):
        return number1 % number2
        
    def logarithm(self,number1):
        return math.log(number1)
        

# creating Calculator Instance
calculator = Calculator()

while True:
    # getting the values and operation from the user
    print("====================== Calculator ================================")
    print("================= Operations available ===========================")
    print("== addition '+' subtraction '-' multiplication '*' division '/' ==")
    print("== sqr root 'sqr' exponential 'exp' div rest 'rest' logarithm 'log'")
    print("================== To Quit press Q ===============================")
    try:
        number1 = int(input("type the first number: "))
    except ValueError:
        print("No letters allowed, only numbers!!")
        number1 = int(input("type the first number: "))

    operator_list = ['+','-','*','/','sqr','exp','rest','log']
    operation = input("type the operation symbol: ")
    if operation in operator_list:
        pass
    else:
        print("invalid operator")
        operation = input("type the operation symbol: ")

    try:
        number2 = int(input("type the second number: "))
    except ValueError:
        print("No letters allowed, only numbers!!")
        number2 = int(input("type the second number: "))

    # associating operation symbol with specific function
    if operation == '+':
        print(calculator.addition(number1,number2))
    elif operation == '-':
        print(calculator.subtraction(number1,number2))
    elif operation == '*':
        print(calculator.multiplication(number1,number2))
    elif operation == '/':
        try:
            conta = calculator.division(number1,number2)
        except ZeroDivisionError:
            print("Division by zero Not Allowed!")
        else:    
            print(conta)
    elif operation == 'sqr':
        print(calculator.sqroot(number1))
    elif operation == 'exp':
        print(calculator.exponential(number1,number2))
    elif operation == 'rest':
        try:
            conta = calculator.division_rest(number1,number2)
        except ZeroDivisionError:
            print("Division by zero Not Allowed!")
        else:
            print(conta)
    elif operation == 'log':
        try:
            conta = calculator.logarithm(number1)
        except ValueError:
            print("Number must be bigger than zero!")
        else:
            print(conta)

    var = input("continue or quit?")
    if var == 'q':
        break




