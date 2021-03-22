'''This program will create and store a list of 20 student names and their corresponding scores.
Created by Fernando Ames
Date Created: 03/16/2019'''

nameUser = input ("Please enter your name")
print("Hello, ", nameUser + ' ' "!! Welcome to my nineth Python Program.")


names = ['Jim', 'Sarah', 'Jason', 'Lynne', 'Ginny', 'Joe', 'Susan', 'Daniel',
         'Paul','Hagen', 'Srikar', 'Ali', 'Omar', 'Julie', 'Michelle',
         'Vipul','Atul','Garima','Urvi','Jia']

scores = [88, 92, 95, 84, 85, 92, 89, 56, 76, 78, 88, 99, 45, 55, 77, 65, 75, 87, 88, 98] 


for i in range(0,20):
    print(names[i],':',scores[i])


name=input('Please enter the name: ')

while name!='q':
    ind=names.index(name)
    print(name,'scored',scores[ind])
    name=input('Please enter the name: ')

print("Thanks", nameUser+ ' ' "for using my program.")
