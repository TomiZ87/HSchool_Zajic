import random
special_characters = ["!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "]", "^", "_", "`", "{", "|", "}", "~"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
password_key = input("Enter the structure of the password C(Digit), M(small letters), V(capital letters, S(special characters)): ")
password_key = password_key.upper()
for i in password_key:
    if i == "C" or i == "S" or i == "M" or i == "V": pass
    else: exit()
password = []
for x in password_key:
    if x == "S": password.append(random.choice(special_characters))
    elif x == "C": password.append(random.choice(numbers))
    elif  x == "V": password.append(random.choice(letters))
    elif  x == "M": password.append(random.choice(letters).lower())
print("".join(password))