import time
def get_integer(promt):
    while True:
        try:
            number = float(input(promt))
            if number % 1 == 0: return int(number)
            else: print("The number is decimal, try again!")
        except ValueError: print("\033[31mInvalid input. Please enter a number.\033[0m")
number = get_integer("Please enter the number: ")
start_time = time.time()
if abs(number) > 2 and (abs(number) % 2 != 0):
    x = 3
    while (abs(number) > x):
        if abs(number) % x == 0:
            print("The number is not prime! Last prime " + str(x))
            break
        x += 1
    else: print("The number is prime!")
elif abs(number) < 3 and abs(number) > 1: print("The number is prime!")
elif abs(number) == 1: print("Idk, just 1")
else: print("The number is not prime! Last prime 2")
end_time = time.time()
print("Execution time:", (end_time - start_time), "seconds")