def get_integer(promt):
    while True:
        try:
            number = int(input(promt))
            if number > 0: return number
            else: print("\033[31mPlease enter a positive number.\033[0m")
        except ValueError: print("\033[31mInvalid input. Please enter a positive number.\033[0m")
number = get_integer("Enter a whole number <: ")
sum_number = 0
for i in str(number):
    sum_number += int(i)
print("The sum of digits is " +str(sum_number))