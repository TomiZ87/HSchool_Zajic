import random
special_characters = ["!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "]", "^", "_", "`", "{", "|", "}", "~"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
def get_integer(promt):
    while True:
        try:
            number = int(input(promt))
            if number > 0: return number
            else: print("\033[31mPlease enter a positive number.\033[0m")
        except ValueError: print("\033[31mInvalid input. Please enter a positive number.\033[0m")
lenght = get_integer("Enter the lenght of your password: ")
password = []

for x in range(0, lenght):
    y = random.randint(0, 3)
    if y == 0:
        password.append(random.choice(special_characters))
    elif y == 1:
        password.append(random.choice(numbers))
    elif  y == 2:
        password.append(random.choice(letters))
    elif  y == 3:
        upper_letter = random.choice(letters)
        password.append(upper_letter.lower())
print("".join(password))