password = input("Enter your password: ")
if 8 <= len(password) <= 15:
    lowercase, uppercase, spacial, digit = 0, 0, 0, 0
    for x in password:
        if x.isalnum():
            if x.islower(): lowercase += 1
            if x.isupper(): uppercase += 1
            if x.isdigit(): digit += 1
        elif x in ["+", "*", "#", "&"]: spacial += 1
        else:
            print("Unknown characters")
            exit()
    if lowercase == uppercase:
        if 2 <= spacial <= 4:
            if digit >= 3: print("Password is valid")
            else: print("Not enough numbers")
        else: print("Too much or too many special characters")
    else: print("Lowercase != uppercase")
else: print("Invalid num of characters 8-15")