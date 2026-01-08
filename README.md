Assignment for Module - 2, Python Basics

Task 1:

Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition, Subtraction, Multiplication, Division
3.  Displays the results of each operation on the screen.

Code for Task 1 is  :

x = float(input("Enter 1st number :"))
y = float(input("Enter 2nd number :"))

print("The results are as follows:")
print("Addition :", x + y)
print("Sutraction :", x - y)
print("Multiplication :", x * y)
print("Division :", round(x / y, 2))


Task 2 :

Task 2: Create a Personalized Greeting
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.


Code for Task 2 is : 

x = input("Enter your first name : ")
y = input("Enter your 2nd name : ")

print("Hello,", x +' '+ y +",", "Have a Nice Day!")
