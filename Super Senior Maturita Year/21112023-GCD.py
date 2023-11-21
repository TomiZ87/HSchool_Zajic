import math;
def get_integer(promt):
    while True:
        try:
            number = int(input(promt))
            if number > 0: return number
        except ValueError: print("\033[31mInvalid input. Please enter a positive number.\033[0m")
num1 = get_integer("Enter the first number ")
num2 = get_integer("Enter the second number ")
for x in range(1, min(num1, num2)+1):
    if num1 % x == 0 and num2 % x == 0: gcd_number = x
print("Greatest Common divisor of the above-mentioned numbers is " +str(gcd_number))