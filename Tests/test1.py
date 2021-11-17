current_year = int(input("Enter the current year: "))
current_month = int(input("Enter the current month: "))
current_day = int(input("Enter the current day: "))

birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

first_name = input("Enter your first name(also Middle name if you have): ")
last_name = input("Enter your last name: ")
job = input("Enter your occupation/job: ")

age_error = ""
first_name_error = ""
last_name_error = ""
job_error = ""


# 1.1 Age and Date Logic

valid_current_month = 1
valid_birth_month = 1
valid_months = 1
valid_current_day = 1
valid_birth_day = 1
valid_days = 1
valid_date = 1

# 1.1.2 Checking if the entered months are valid
if current_month >= 1 and current_month <= 12:
    valid_current_month = 1
else:
    valid_current_month = 0
if birth_month >= 1 and birth_month <= 12:
    valid_birth_month = 1
else:
    valid_birth_month = 0
if bool(valid_current_month) and bool(valid_birth_month):
    valid_months = 1
else:
    valid_months = 0

# 1.1.2 Checking if the entered days are valid
if valid_current_month == 1 and current_month == 1 and current_day > 0 and current_day <= 31:
    valid_current_day = 1
elif valid_current_month == 1 and current_month == 2 and current_day > 0 and (current_day <= 28 or (current_year % 4 == 0 and current_day <= 29)):
    valid_current_day = 1
elif valid_current_month == 1 and current_month == 3 and current_day > 0 and current_day <= 31:
    valid_current_day = 1
elif valid_current_month == 1 and current_month == 4 and current_day > 0 and current_day <= 30:
    valid_current_day = 1
elif valid_current_month == 1 and current_month == 5 and current_day > 0 and current_day <= 31:
    valid_current_day = 1
elif valid_current_month == 1 and current_month == 6 and current_day > 0 and current_day <= 30:
    valid_current_day = 1
elif valid_current_month == 1 and current_month == 7 and current_day > 0 and current_day <= 31:
    valid_current_day = 1
elif valid_current_month == 1 and current_month == 8 and current_day > 0 and current_day <= 31:
    valid_current_day = 1
elif valid_current_month == 1 and current_month == 9 and current_day > 0 and current_day <= 30:
    valid_current_day = 1
elif valid_current_month == 1 and current_month == 10 and current_day > 0 and current_day <= 31:
    valid_current_day = 1
elif valid_current_month == 1 and current_month == 11 and current_day > 0 and current_day <= 30:
    valid_current_day = 1
elif valid_current_month == 1 and current_month == 12 and current_day > 0 and current_day <= 31:
    valid_current_day = 1
else:
    valid_current_day = 0

if valid_birth_month == 1 and birth_month == 1 and birth_day > 0 and birth_day <= 31:
    valid_birth_day = 1
elif valid_birth_month == 1 and birth_month == 2 and birth_day > 0 and (birth_day <= 28 or (birth_year % 4 == 0 and birth_day <= 29)):
    valid_birth_day = 1
elif valid_birth_month == 1 and birth_month == 3 and birth_day > 0 and birth_day <= 31:
    valid_birth_day = 1
elif valid_birth_month == 1 and birth_month == 4 and birth_day > 0 and birth_day <= 30:
    valid_birth_day = 1
elif valid_birth_month == 1 and birth_month == 5 and birth_day > 0 and birth_day <= 31:
    valid_birth_day = 1
elif valid_birth_month == 1 and birth_month == 6 and birth_day > 0 and birth_day <= 30:
    valid_birth_day = 1
elif valid_birth_month == 1 and birth_month == 7 and birth_day > 0 and birth_day <= 31:
    valid_birth_day = 1
elif valid_birth_month == 1 and birth_month == 8 and birth_day > 0 and birth_day <= 31:
    valid_birth_day = 1
elif valid_birth_month == 1 and birth_month == 9 and birth_day > 0 and birth_day <= 30:
    valid_birth_day = 1
elif valid_birth_month == 1 and birth_month == 10 and birth_day > 0 and birth_day <= 31:
    valid_birth_day = 1
elif valid_birth_month == 1 and birth_month == 11 and birth_day > 0 and birth_day <= 30:
    valid_birth_day = 1
elif valid_birth_month == 1 and birth_month == 12 and birth_day > 0 and birth_day <= 31:
    valid_birth_day = 1
else:
    valid_birth_day = 0
if bool(valid_current_day) and bool(valid_birth_day):
    valid_days = 1
else:
    valid_days = 0
if bool(valid_months) and bool(valid_days):
    valid_date = 1
else:
    valid_date = 0

# 1.1.3 Checking the age
if valid_date == 1 and current_month > birth_month or (current_month == birth_month and current_day >= birth_day):
    age = current_year - birth_year
elif valid_date == 1 and current_month < birth_month or (current_month == birth_month and current_day < birth_day):
    age = current_year - birth_year - 1
if valid_date == 1 and age < 0:
    age_error = "The user hasn't been born yet" 

if not bool(valid_birth_day) or not bool(valid_current_day):
    age_error = "Entered birth or current day don't exist."
if not bool(valid_birth_month) or not bool(valid_current_month):
    age_error = "Entered birth or current month don't exist."

# 1.1.4 Dates
if bool(valid_current_month) and bool(valid_current_day):
    current_date = str(current_day) + "." + str(current_month) + "." + str(current_year)
else:
    current_date = "Unknown -> (" + str(current_day) + "." + str(current_month) + "." + str(current_year) + ")"
if bool(valid_birth_month) and bool(valid_birth_day):
    birth_date = str(birth_day) + "." + str(birth_month) + "." + str(birth_year)
else:
    birth_date = "Unknown -> (" + str(birth_day) + "." + str(birth_month) + "." + str(birth_year) + ")"

# 1.2 Names logic
first_name_count = 1
if " " in first_name:
    first_name_count += 1
if first_name == "":
    first_name_error = "Error: No first name was entered!"
    first_name = "Unknown"
    first_name_count = 0
if last_name == "":
    last_name_error = "Error: No last name was entered!"
    last_name = "Unknown"

# 1.3 Job logic
if valid_date == 1 and 0 < age < 18 and (job != "Student" or job != "student"):
    job = "Unknown"
    job_error = "Error: The Student has got a job!!"
elif valid_date == 1 and 0 < age < 18:
    job = "Student"
if job == "":
    job_error = "Error: No job was entered"
    job = "Unknown"

# 1.1.5 Age Error unknowns
if not age_error == "":
    age = str(age)
    age = "Unknown"

# 1.4.1 Printing Data
print("User Data:")
print("First Name: " + first_name)
print("First Name Count: " + str(first_name_count))
print("Last Name: " + last_name)
print("Current Date: " + current_date)
print("Birth Date: " + birth_date)
print("Age: " + str(age))
print("Job: " + job)

# 1.4.2 Printing Errors
if first_name_error != "":
    print("First Name: " + first_name_error)
if last_name_error != "":
    print("Last Name: " + last_name_error)
if age_error != "":
    print("Age Error: " + age_error)
if job_error != "":
    print("Job: " + job_error)