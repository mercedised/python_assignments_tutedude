''' Assignment 1, Module 2 : Basic Python Concepts'''
'''Write a python program that does following :
       1) Takes two numbers as input from user
       2) Performs a) Addition, b) Subtraction, c) Multiplication, d) Division
       3) Displays the result of each operation on the screen all at once'''

x = float(input("Enter 1st number :"))
y = float(input("Enter 2nd number :"))

print("The results are as follows:")
print("Addition :", x + y)
print("Sutraction :", x - y)
print("Multiplication :", x * y)
print("Division :", round(x / y, 2))

