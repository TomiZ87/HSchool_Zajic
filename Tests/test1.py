current_year = int(input("Enter the current year: "))
current_month = int(input("Enter the current month: "))
current_day = int(input("Enter the current day: "))

birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

first_name = str(input("Enter your first name(also Middle name if you have): "))
last_name = str(input("Enter your last name: "))
job = str(input("Enter your occupation/job: "))

age_error = ""
first_name_error = ""
last_name_error = ""
job_error = ""

# 1.1 Age and Date Logic
error_c_month = 0
error_b_month = 0
same_month = 0

valid_current_month = 1
valid_birth_month = 1
valid_months = 1
valid_current_day = 1
valid_birth_day = 1
valid_days = 1

# 1.1.1 Checking if the entered months are valid
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
if bool(valid_current_month) and current_month == 1 and current_day > 0 and current_day <= 31:
    valid_current_day = 1
elif bool(valid_current_month) and current_month == 2 and current_day > 0 and (current_day <= 28 or (current_year % 4 == 0 and current_day <= 29)):
    valid_current_day = 1
elif bool(valid_current_month) and current_month == 3 and current_day > 0 and current_day <= 31:
    valid_current_day = 1
elif bool(valid_current_month) and current_month == 4 and current_day > 0 and current_day <= 30:
    valid_current_day = 1
elif bool(valid_current_month) and current_month == 5 and current_day > 0 and current_day <= 31:
    valid_current_day = 1
elif bool(valid_current_month) and current_month == 6 and current_day > 0 and current_day <= 30:
    valid_current_day = 1
elif bool(valid_current_month) and current_month == 7 and current_day > 0 and current_day <= 31:
    valid_current_day = 1
elif bool(valid_current_month) and current_month == 8 and current_day > 0 and current_day <= 31:
    valid_current_day = 1
elif bool(valid_current_month) and current_month == 9 and current_day > 0 and current_day <= 30:
    valid_current_day = 1
elif bool(valid_current_month) and current_month == 10 and current_day > 0 and current_day <= 31:
    valid_current_day = 1
elif bool(valid_current_month) and current_month == 11 and current_day > 0 and current_day <= 30:
    valid_current_day = 1
elif bool(valid_current_month) and current_month == 12 and current_day > 0 and current_day <= 31:
    valid_current_day = 1
else:
    valid_current_day = 0

if bool(valid_birth_month) and birth_month == 1 and birth_day > 0 and birth_day <= 31:
    valid_birth_day = 1
elif bool(valid_birth_month) and birth_month == 2 and birth_day > 0 and (birth_day <= 28 or (birth_year % 4 == 0 and birth_day <= 29)):
    valid_birth_day = 1
elif bool(valid_birth_month) and birth_month == 3 and birth_day > 0 and birth_day <= 31:
    valid_birth_day = 1
elif bool(valid_birth_month) and birth_month == 4 and birth_day > 0 and birth_day <= 30:
    valid_birth_day = 1
elif bool(valid_birth_month) and birth_month == 5 and birth_day > 0 and birth_day <= 31:
    valid_birth_day = 1
elif bool(valid_birth_month) and birth_month == 6 and birth_day > 0 and birth_day <= 30:
    valid_birth_day = 1
elif bool(valid_birth_month) and birth_month == 7 and birth_day > 0 and birth_day <= 31:
    valid_birth_day = 1
elif bool(valid_birth_month) and birth_month == 8 and birth_day > 0 and birth_day <= 31:
    valid_birth_day = 1
elif bool(valid_birth_month) and birth_month == 9 and birth_day > 0 and birth_day <= 30:
    valid_birth_day = 1
elif bool(valid_birth_month) and birth_month == 10 and birth_day > 0 and birth_day <= 31:
    valid_birth_day = 1
elif bool(valid_birth_month) and birth_month == 11 and birth_day > 0 and birth_day <= 30:
    valid_birth_day = 1
elif bool(valid_birth_month) and birth_month == 12 and birth_day > 0 and birth_day <= 31:
    valid_birth_day = 1
else:
    valid_birth_day = 0
if bool(valid_current_day) and bool(valid_birth_day):
    valid_days = 1
# 1.1.3 Checking the age

if bool(valid_months) and bool(valid_days) and current_month > birth_month:
    age = current_year - birth_year
elif bool(valid_months) and bool(valid_days) and current_month < birth_month:
    age = current_year - birth_year - 1
elif bool(valid_months) and bool(valid_days) and current_month == birth_month and current_day >= birth_day:
    age = current_year - birth_year

if bool(valid_months) and bool(valid_days) and age < 0:
    age_error = "Error: The User Was not born yet!"

if bool(valid_current_month) and bool(valid_current_day):
    current_date = str(current_day) + "." + str(current_month) + "." + str(current_year)
else:
    current_date = "Unknown"
if bool(valid_birth_month) and bool(valid_birth_day):
    birth_date = str(birth_day) + "." + str(birth_month) + "." + str(birth_year)
else:
    current_date = "Unknown"

# 1.2 Names logic
first_name_count = 1
if " " in first_name:
    first_name_count += 1
if first_name == "":
    first_name_error = "Error: No first name was entered!"
    first_name = "Unknown"
if last_name == "":
    last_name_error = "Error: No last name was entered!"
    last_name = "Unknown"

# 1.3 Job logic
if age < 18 and not age == "Unknown":
    job = "Student"
if age < 18 and not age == "Unknown" and not job == "Student" and not job == "student":
    job = "Unknown"
    job_error = "Error: The Student has got a job!!"
if job == "":
    job_error = "Error: No job was entered"
    job = "Unknown"

# 1.1 Age errors for 
if not bool(valid_months):
    age = str(age)
    age = "Unknown"
    age_error = "Error: The entered month/s are not valid!"
if not bool(valid_months):
    age = str(age)
    age = "Unknown"
    age_error = "Error: The entered month/s are not valid!"

# 1.4 Printing Data
print("User Data:")
print("First Name: " + str(first_name))
print("First Name Count: " + str(first_name_count))
print("Last Name: " + str(last_name))
print("Current Date: " + str(current_date))
print("Birth Date: " + str(birth_date))
print("Age: " + str(age))
print("Job: " + str(job))
if first_name == "Unknown":
    print("First Name Error: " + first_name_error)
if last_name == "Unknown":
    print("Last Name Error: " + last_name_error)
if age == "Unknown":
    print("Age Error: " + age_error)
if job == "Unknown":
    print("Job Error: " + job_error)