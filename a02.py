'''This program will show the product, difference, quotient and remainder of two numbers.
Created by Fernando Ames
Date Created: 01/20/2019 '''

name = input("Please enter your name")
subject = input("What are studying?")
print("Hello, ", name + ' ' "!!!!! Welcome to my Second Python Program. You will do very well in", subject + ' ' "if you work hard!")

number1 = int(input("Enter the first Number: ") )
number2 = int(input("Enter the second Number: ") )

addition = number1 + number2
print('The sum of {0} and {1} is {2} '.format(number1, number2, addition))


subtraction = number1 - number2
print('The subtraction of {0} and {1} is {2} '.format(number1, number2, subtraction))


product = number1 * number2
print('The product of {0} and {1} is {2} '.format(number1, number2, product))

quotient = number1 / number2
print('The quotient of {0} and {1} is {2} '.format(number1, number2, quotient))

remainder = number1 % number2
print('The remainder of {0} and {1} is {2} '.format(number1, number2, remainder))

print("Thanks for using my program.")


