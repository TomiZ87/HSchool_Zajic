from datetime import datetime
input_text = open("./Super Senior Maturita Year/files/08112023-BirthNumber-Input.txt", "r")
lines = input_text.readlines()
birth_numbers, output = [], []
for line in lines:
    birth_numbers.append(line.strip())
input_text.close()
def save(saveing_material):
    f = open("./Super Senior Maturita Year/files/08112023-BirthNumber-Output.txt", "a")
    f.write("Birth Number Program: "+str(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n"))
    for x in saveing_material: f.write(x)
    f.close()
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
                output.append(str(x) + ". - " + birth_number + "; Date of birth is: " + day + "." + month + "." + year + "; Gender: " + gender + "\n")
                print(str(x) + ". - " + birth_number + "; Date of birth is: " + day + "." + month + "." + year + "; Gender: " + gender)
            else: output.append(str(x) + ". - Invalid Day: '" + day + "' = " + birth_number + "\n")
        else: output.append(str(x) + ". - Invalid Month: '" + month + "' = " + birth_number + "\n")
    else: output.append(str(x) + ". - Invalid Birth number Formatt - yymmdd/xxxx - " + birth_number + "\n")
save(output)