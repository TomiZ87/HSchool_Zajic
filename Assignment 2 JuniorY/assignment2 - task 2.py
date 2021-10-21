import datetime

print("Exercise 2: Input + Years")
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
date = datetime.datetime.now()
date_birth = int(date.year - age)
age100 = int(date_birth + 100)
print("Your name is " + name + ", you were born in " + str(date_birth) + ". You will be 100 years old in " + str(age100))