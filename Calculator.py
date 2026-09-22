#creating a basic calculator program that takes input from user and performs a function/prints a result
from math import *

num1 = float(input("Enter a number: "))
operator = input("Enter the sign for the operation: ")
num2 = float(input("Enter another number: "))

#Get two numbers from input and using DMAS function
if operator == "+" :
    print (num1 + num2)
elif operator == "-" :
    print (num1 - num2)
elif operator == "/":
    print (round(num1 / num2))
elif operator == "*" :
    print (round(num1 * num2))
else:
    print("Error, invalid operator sign")


#its not showing when I round to 2 dp
#result = num1 + num2
#print(result)
#but this prints out the strings of those numbers
#instead we have to turn the strings to numbers 
#can use int to convert to a whole number
#result = int(num1 + num2)
#print(result)
#what if we want decimals?
"""
result = float(num1) + float(num2)
print(result)
#if you want to round to 2dp
print(round(result))
"""


