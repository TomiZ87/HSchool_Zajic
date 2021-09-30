import datetime
print("Exercise 1: Sum of 2 numbers")
num1 = int(input("Enter any number: "))
num2 = int(input("Enter second any number: "))
print(num1 + num2)

print("Exercise 2: Input + Years")
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
date = datetime.datetime.now()
age100 = int(date.year - age + 100)
print("Your name is " + name + ", you were born in " + str(age) + ". You will be 100 years old in " + str(age100))

print("Exercise 3: Mathematical formula: Area of Trapezoid")
a = int(input("Enter parameter A (length of parallel side): "))
c = int(input("Enter parameter C (length of parallel side): "))
v = int(input("Enter height: "))
area_trapezoid = int(((a+c)*v)/2)
print("The area of the given trapezoid is: " + str(area_trapezoid))
