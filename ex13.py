#tells program to take input and save to plug into scirpt (scirpt being the actual program)
from sys import argv

#tells program the first input will be the script name, 1,2,3 will all ve inputs
script, first, second, third = argv

#shows what the name of the .py is
print("This script is called:", script)

#read the WYSS section for how to run this
#each of these will display what the user entered for the three inputs
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

#defines var, aks user for name, prints name
name = input
input("enter a name: ")
print(name)