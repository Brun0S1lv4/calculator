# calculator project in python 
# version 1.0

class Calculator:
    def __init__(self):
        self.display:0

    def addition(self,number1,number2):
        addition = number1 + number2
        self.display = addition

    def subtraction(self,number1,number2):
        subtraction = number1 - number2
        self.display = subtraction

    def multiplication(self,number1,number2):
        multiplication = number1 * number2
        self.display = multiplication

    def division(self,number1,number2):
        division = number1 / number2
        self.display = division

# Some tests

calculadora1 = Calculator()

calculadora1.addition(7,2)
#...
print(calculadora1.display)
calculadora1.multiplication(9,7)
#...
print(calculadora1.display)
calculadora1.subtraction(875,256)
#...
print(calculadora1.display)
calculadora1.division(575,20)
#...
print(calculadora1.display)