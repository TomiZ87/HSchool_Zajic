from datetime import datetime
def get_integer(promt):
    while True:
        try:
            number = int(input(promt))
            if number > 0: return number
        except ValueError: print("\033[31mInvalid input. Please enter a valid number.\033[0m")
def load(file):
    input_text = open("./Super Senior Maturita Year/files/" + file + ".txt", "r")
    lines = input_text.readlines()
    for line in lines:
        birth_numbers.append(line.strip("\n"))
    input_text.close()
def save(saveing_material, file):
    f = open("./Super Senior Maturita Year/files/" + file + ".txt", "a")
    f.write("Birth Number Program: "+str(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n"))
    for x in saveing_material: f.write(x)
    f.close()
while True:
    birth_numbers = [] 
    output = []
    choice = get_integer("1 -> To Birth Number to Date, 2 -> Date to Birth Number, 3 Quit the program: ")
    if choice == 1:
        load("08112023-BirthNumber-Input-1")
        for x in range(len(birth_numbers)):
            birth_number = birth_numbers[x]
            gender = ""
            if (len(birth_number) == 11 or len(birth_number) == 10) and birth_number[6] == "/":
                year = birth_number[0:2]
                month = birth_number[2:4]
                if month[0] == "5":
                    month = month.lstrip(month[0])
                    month = '0' + month
                if month[0] == "6": 
                    month = month.lstrip(month[0])
                    month = '1' + month
                day = birth_number[4:6]
                if month != "00" and "01" <= month <= "12":
                    if month[0] == "0": month = month.lstrip(month[0])
                    if day != "00" and "01" <= day <= "31":
                        if birth_number[2] == "0" or birth_number[2] == "1": gender = "Male"
                        else: gender = "Female"
                        if year[0] == "0" or year[0] == "1" or year[0] == "2": year = "20" + year
                        else: year = "19" + year
                        output.append(str(x+1) + ". - " + birth_number + "; Date of birth is: " + day + "." + month + "." + year + "; Gender: " + gender + "\n")
                        print(str(x+1) + ". - " + birth_number + "; Date of birth is: " + day + "." + month + "." + year + "; Gender: " + gender)
                    else: output.append(str(x+1) + ". - Invalid Day: '" + day + "' = " + birth_number + "\n")
                else: output.append(str(x+1) + ". - Invalid Month: '" + month + "' = " + birth_number + "\n")
            else: output.append(str(x+1) + ". - Invalid Birth number Format - yymmdd/xxxx - " + birth_number + "\n")
        save(output, "08112023-BirthNumber-Output")
    elif choice == 2:
        load("08112023-BirthNumber-Input-2")
        for x in range(len(birth_numbers)):
            birth_number = birth_numbers[x]
            gender = 0
            if len(birth_number) == 12:
                day = int(birth_number[0:2])
                month = int(birth_number[3:5])
                year = birth_number[8:10]
                if 1 <= month <= 12:
                    if birth_number[-1] == 'M': gender = 1
                    elif birth_number[-1] == 'F': gender = 2
                    else: gender = 0
                    if gender == 2: month += 50
                    if gender != 0:
                        if month < 10: 
                            month = str(month)
                            month = '0' + str(month)
                        else: month = str(month)
                        if 1 <= day <= 31:
                            output.append(str(x+1) + ". - " + birth_number + "; Date of birth number is: " + str(year) + month + str(day) + "/xxxx\n")
                            print(str(x+1) + ". - " + birth_number + "; Date of birth number is: " + str(year) + month + str(day) + "/xxxx")
                        else: output.append(str(x+1) + ". - Invalid Day: '" + str(day) + "' = " + birth_number + "\n")
                    else: output.append(str(x+1) + ". - Invalid Gender: '" + birth_number[-1] + "' = " + birth_number + "\n")
                else: output.append(str(x+1) + ". - Invalid Month: '" + str(month) + "' = " + birth_number + "\n")
            else: output.append(str(x+1) + ". - Invalid Date Format - DD.MM.YYYY M/F - " + birth_number + "\n")
        save(output, "08112023-BirthNumber-Output")
    elif choice == 3: break
    else: print("\033[31mInvalid choice. Please enter 1, 2, or 3.\033[0m")