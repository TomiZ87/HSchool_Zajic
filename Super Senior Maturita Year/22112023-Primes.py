def get_integer(promt):
    while True:
        try:
            number = float(input(promt))
            return number
        except ValueError: print("\033[31mInvalid input. Please enter a number.\033[0m")
true = True
while true:
    number = get_integer("Please enter the number: ")
    if number % 1 == 0:
        number = int(number)
        if number != 0:
            for i in range(2, abs(number)):
                if number % i == 0:
                    print("The number is not prime!")
                    break
                elif (number % i != 0 and i == (abs(number)-1)):
                    print("The number is prime!")
            break
        else:
            print("The number is 0, try again!")
    else:
        print("The number is decimal, try again!")