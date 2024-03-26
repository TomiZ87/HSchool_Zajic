def get_integer(promt):
    while True:
        try:
            number = float(input(promt))
            if number % 1 == 0: return int(number)
            else: print("The number is decimal, try again!")
        except ValueError: print("\033[31mInvalid input. Please enter a number.\033[0m")
number = get_integer("Please enter the number: ")
if abs(number) > 2 and (abs(number) % 2 != 0):
    x = 3
    while (abs(number) > x):
        if abs(number) % x == 0:
            print("The number is not prime!")
            exit()
        x += 1
    else: print("The number is prime!")
elif abs(number) < 3: print("The number is prime!")
else: print("The number is not prime!")
