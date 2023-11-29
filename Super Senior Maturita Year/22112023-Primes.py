def get_float(promt):
    while True:
        try:
            number = float(input(promt))
            if number % 1 == 0: return number 
            else: print("The number is decimal, try again!")
        except ValueError: print("\033[31mInvalid input. Please enter a number.\033[0m")
number = get_float("Please enter the number: ")
number = int(number)
if number != 0:
    for i in range(2, abs(number)):
        if abs(number) % i == 0:
            print("The number is not prime!")
            break
        elif (abs(number) % i != 0 and i == abs(number)-1):
            print("The number is prime!")
    if number == 2: print("The number is prime!")
else:
    print("The number is 0, try again!")