import math
banknotes = [500, 200, 100, 50, 20, 10, 5]
change = []
def get_integer(promt):
    while True:
        try:
            number = float(input(promt))
            if number > 0: return number
        except ValueError: print("\033[31mInvalid input. Please enter a positive whole number.\033[0m")
num1 = get_integer("Enter the money ")
for x in range(len(banknotes)):
    current_change = 0
    while num1 >= banknotes[x]:
        current_change += 1
        num1 -= banknotes[x]
    if current_change != 0: print("You will have " +str(current_change) + " of " +str(banknotes[x]) + "€ bankones.")
if num1 != 0: print("You will have " +str(round(num1, 2)) + " euro coins.") 