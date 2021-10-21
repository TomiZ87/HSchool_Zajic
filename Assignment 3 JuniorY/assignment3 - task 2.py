import datetime

print("Exercise 2: Date of birth and 100 years")
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
date = datetime.datetime.now()
date_birth = int(date.year - age)
age100 = int(date_birth + 100)

if age < 0 :
    print("Your name is " + name + ", you will be born in " + str(date_birth) + ". You will be 100 years old in " + str(age100))
elif age == 0 :
    print("Your name is " + name + ", you were born " + str(date.year) + ". You will be 100 years old in " + str(age100))
else:
    print("Your name is " + name + ", you were born in " + str(date_birth) + ". You will be 100 years old in " + str(age100))
