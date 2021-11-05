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

if bool(valid_months) and current_month > birth_month:
    age = current_year - birth_year
elif bool(valid_months) and current_month < birth_month:
    age = current_year - birth_year - 1
elif bool(valid_months) and current_month == birth_month and current_day >= birth_day:
    age = current_year - birth_year

if bool(valid_months) and age < 0:
    age_error = "Error: The User Was not born yet!"
"""
if current_month > 13 or current_month < 0:
    error_c_month = 1
if birth_month > 12 or birth_month < 0:
    error_b_month = 1

if current_month > birth_month and error_c_month == 0 and error_b_month == 0:
    age += 1
if current_month == birth_month and error_c_month == 0 and error_b_month == 0:
    same_month = 1
if bool(same_month) and current_day >= birth_day:
    age += 1

if age < 0 and error_c_month == 0 and error_b_month == 0:
    age_error = age_error + "Error: The User Was not born yet! "
if error_b_month == 1 or error_c_month == 1:
    age = str(age)
    age = "Unknown"
    age_error = "Error: Invalid Month! "
"""
if error_c_month == 0:
    current_date = str(current_day) + "." + str(current_month) + "." + str(current_year)
else:
    current_date = "Unknown"
if error_b_month == 0:
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
# 1.1 Age problems
if not bool(valid_months):
    age = str(age)
    age = "Unknown"

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
