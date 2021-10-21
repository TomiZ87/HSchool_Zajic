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