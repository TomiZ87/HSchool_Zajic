import random
import string
while True:
    try:
        length = int(input("Enter the lenght of the password (8-15 char.) : "))
        if 8 <= length <= 15:
            while True:
                symbols = random.randint(2, 4)
                digits = random.randint(3, length - symbols)
                print((length - symbols - digits) % 2 == 0)
                if ((length - symbols - digits) % 2 == 0):
                    letters = (length - symbols - digits) / 2
                    letters = int(letters)
                    break
            
            password_chars = (
                random.choices(string.ascii_lowercase, k=letters) +
                random.choices(string.ascii_uppercase, k=letters) +
                random.choices(string.digits, k=digits) +
                random.choices("+*#&", k=symbols)
            )
            random.shuffle(password_chars)
            password = ''.join(password_chars)
            print("Generated password:", password)
        else: print("Try again!")
    except ValueError:
        print("Please enter a valid integer.")