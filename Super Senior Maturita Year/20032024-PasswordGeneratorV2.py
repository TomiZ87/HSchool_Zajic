import random
import string
permutations = 1
while (permutations <= 1000000):
    password_key = input("Enter the structure of the password C(Digit), M(small letters), V(capital letters, S(special characters)): ")
    password_key = password_key.upper()
    for i in password_key:
        if i == "C" or i == "S" or i == "M" or i == "V": pass
        else: exit()
    permutations = 1
    password = []
    for x in password_key:
        if x == "S": 
            password.append(random.choice(str(string.punctuation)))
            permutations = permutations*len(string.punctuation)
        elif x == "C": 
            password.append(random.choice(str(string.digits)))
            permutations = permutations*len(string.digits)
        elif  x == "V": 
            password.append(random.choice(str(string.ascii_uppercase)))
            permutations = permutations*len(string.ascii_uppercase)
        elif  x == "M": 
            password.append(random.choice(str(string.ascii_lowercase)))
            permutations = permutations*len(string.ascii_lowercase)
    if (permutations <= 1000000): print("Try again :)")
else:
    print(permutations)
    print("".join(password))