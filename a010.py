'''This program will read a 32-bit integer and will output its corresponding value in dotted decimal notation.
Created by Fernando Ames
Date Created: 03/16/2019'''

nameUser = input ("Please enter your name")
print("Hello, ", nameUser + ' ' "!! Welcome to my nineth Python Program.")

def getInt(binary):
 out = 0
 power = 0

 for b in binary[::-1]:
  if b == '1':
   out += 2**power
  power += 1
 return out

a = input("Enter 32 bit string: ")
i=8
result = str(getInt(a[0:8]))


while i<32:
 result += "."+str(getInt(a[i:i+8]))
 i=i+8


print("Dotted decimal notation =",result)



print("Thanks", nameUser+ ' ' "for using my program.")
