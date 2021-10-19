import datetime

print("Exercise 1: Positive/negative/zero")
myNumber = int(input("Enter any number: "))
if myNumber > 0 :
    print("The number you entered is positive")
elif myNumber < 0 :
    print("The number you entered is negative")
else:
    print("The number you entered is zero")

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

print("Exercise 3: Multiplying")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Multiple of " + str(num1) + " and " + str(num2) + " is " + str(num1 * num2))

print("Exercise 4: The days of the week")
numberDay = str(input("Write the number from 1 to 7, this numbers represent the days in week: "))

weekday = {
  "1": "Monday",
  "2": "Tuesday",
  "3": "Wednesday",
  "4": "Thursday",
  "5": "Friday",
  "6": "Saturday",
  "7": "Sunday"
}
if numberDay in weekday:
    print("This number corresponds with " +str(weekday[numberDay]))
else:
    print ("Invalid day")

print("Exercise 5: Mini dictionary")
entered_word = input("Enter one of these words (apple, dog, cat, horse): ")
dictionary = {
  "english": "slovak",
  "apple": "jablko",
  "cat": "mačka",
  "dog": "pes",
  "horse": "kôň"
}
if entered_word in dictionary:
    print("The english translation is " + str(dictionary[entered_word])) 
else:
    print("Invalid word")