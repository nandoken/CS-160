'''This program will mimic a calculator.
Created by Fernando Ames
Date Created: 02/06/2019'''

name = input("Please enter your name")
print("Hello, ", name + ' ' "!!!!! Welcome to my Fourth Python program!")

''' This function adds two number'''
def add(x, y):
    return x + y

''' This function substracts two numbers'''
def subtract(x, y):
    return x - y

''' This function multiplies two numbers'''
def multiply(x, y):
    return x * y

''' THis function divides two numbers'''
def divide(x, y):
    if y == 0:
        print("Error!! Cannot divide by 0!!")
        return 0 
    return x / y

print("Please Select an Operation.")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")


''' Take input from the user '''
choice = input("Enter choice(1/2/3/4):")

number1 = int(input("Enter the First Number: "))
number2 = int(input("Enter the Second Number: "))

if choice == '1':
   print(number1,"+",number2,"=", add(number1,number2))

elif choice == '2':
   print(number1,"-",number2,"=", subtract(number1,number2))

elif choice == '3':
   print(number1,"*",number2,"=", multiply(number1,number2))

elif choice == '4':
   print(number1,"/",number2,"=", divide(number1,number2))
else:
   print("Invalid input")





            
    
