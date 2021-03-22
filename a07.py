'''This program will convert an 8-bit binary number to a decimal number.
Created by Fernando Ames
Date Created: 02/28/2019 '''

name = input("Please enter your name")
print("Hello, ", name + ' ' "!! Welcome to my seventh Python Program.")

import sys


def read_binary_number():

    binary_string = input('Please enter 8-bit binary number: ')


    if len(binary_string) > 8:
        print('Binary string cannot be greater than 8-bits. '
              'Program will exit.')
        sys.exit(1)


    def check_binary_data(x):
        return x in ('0', '1')

 
    if all(map(check_binary_data, binary_string)) is not True:
        print('Binary string contains invalid data. Program will exit.')
        sys.exit(1)

    return binary_string


def binary_to_decimal(binary_string):

    decimal = 0
  
    for power, value in zip(range(8), reversed(binary_string)):
        decimal += (2**power) * int(value)
    return decimal



def main():
    binary_string = read_binary_number()
    decimal = binary_to_decimal(binary_string)
    print(decimal)


if __name__ == '__main__':
    main()
    
print("Thanks", name+ ' ' "for using my program.")
    
