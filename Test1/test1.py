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

age = current_year - birth_year - 1

if current_month > 12 or current_month < 0:
    error_c_month = 1
if birth_month > 12 or current_month < 0:
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
    first_name_error = first_name_error + "Error: No first name was entered"
    first_name = "Unknown"
if last_name == "":
    last_name_error = last_name_error + "Error: No last name was entered"
    last_name = "Unknown"

# 1.3 Job logic
if age < 18 and not age == "Unknown":
    job = "Student"
if age < 18 and not age == "Unknown" and not job == "Student" and not job == "student":
    job = "Unknown"
    job_error = "Error: The Student has got a job!!"
if job == "":
    job_error = "Error: No job was entered"
    last_name = "Unknown"

# 1.4 Printing Data
print("User Data:")
print("First Name: " + str(first_name))
print("Number of names: " + str(first_name_count))
print("Last Name: " + str(last_name))
print("Current Date: " + str(current_date))
print("Birth Date: " + str(birth_date))
print("Age: " + str(age))
print("Job: " + str(job))
if first_name == "Unknown":
    print(first_name_error)
if last_name == "Unknown":
    print(last_name_error)
if age == "Unknown":
    print(age_error)
if job == "Unknown":
    print(job_error)
