# calculator project in python 
# version 1.1

class Calculator:

    def addition(self,number1,number2):
        addition = number1 + number2
        return addition

    def subtraction(self,number1,number2):
        subtraction = number1 - number2
        return subtraction

    def multiplication(self,number1,number2):
        multiplication = number1 * number2
        return multiplication

    def division(self,number1,number2):
        division = number1 / number2
        return division

# creating Calculator Instance
calculator = Calculator()

while True:
    # getting the values and operation from the user
    print("====================== Calculator ================================")
    print("================= Operations available ===========================")
    print("== addition '+' subtraction '-' multiplication '*' division '/' ==")
    print("================== To Quit press Q ===============================")
    number1 = int(input("type the first number: "))
    operation = input("type the operation symbol: ")
    number2 = int(input("type the second number: "))

    
    # associating operation symbol with specific function
    if operation == '+':
        print(calculator.addition(number1,number2))
    elif operation == '-':
        print(calculator.subtraction(number1,number2))
    elif operation == '*':
        print(calculator.multiplication(number1,number2))
    elif operation == '/':
        print(calculator.division(number1,number2))
    
    
    var = input("continue or quit?")
    if var == 'q':
        break




# Some tests

#calculadora1 = Calculator()

#calculadora1.addition(7,2)
#...
#print(calculadora1.display)
#calculadora1.multiplication(9,7)
#...
#print(calculadora1.display)
#calculadora1.subtraction(875,256)
#...
#print(calculadora1.display)
#calculadora1.division(575,20)
#...
#print(calculadora1.display)