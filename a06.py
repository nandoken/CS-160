'''This program will show the sum of even and odd number.
Created by Fernando Ames
Date Created: 02/23/2019 '''

name = input("Please enter your name")
print("Hello, ", name + ' ' "!! Welcome to my sixth Python Program.")

n = int(input("Enter the value of n : "))
                                                
m = int(input("Enter the value of m : "))
sumEven = 0                                     
sumOdd = 0                                      
for i in range(n,m+1):                          
                                              
    rem = i%2                                   
                                                
    if(rem==0):
        sumEven+=i                              
    else:
        sumOdd+=i                               
print("Sum of odd numbers is : ",sumOdd)
print("Sum of even numbers is : ",sumEven) 

print("Thanks for using my program.")

