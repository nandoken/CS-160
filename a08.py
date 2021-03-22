'''This program will colect a list of numbers until the users digit the number 0 to quit and then the list of numbers will be added.
Created by Fernando Ames
Date Created: 03/05/2019'''

name = input("Please enter your name")
print("Hello, ", name + ' ' "!! Welcome to my eighth Python Program.")

def read_list():
    lst = []
    while True:
        num = int(input('Please enter a number: '))
        if num == 0:
            break
        lst.append(num)
    return lst


def get_total(lst):
    total = 0
    for num in lst:
        total += num
    return total


def print_results(lst):
    for i, num in enumerate(lst):
        print(num, end='')
        if i != len(lst) - 1:
            print(' + ', end='')
    print(' = ' + str(get_total(lst)))


def main():
    lst = read_list()
    print_results(lst)


main()

print("Thanks", name+ ' ' "for using my program.")

