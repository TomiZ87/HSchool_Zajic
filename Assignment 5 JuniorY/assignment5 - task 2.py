print("Exercise 2: Multiplying numbers")
print("All numbers between the first two input numbers will be multiplyed by the third entered number.")
chosen_numbers = []
numbers = []
chosen_numbers.append(int(input("Enter First Number: ")))
chosen_numbers.append(int(input("Enter Second Number: ")))
number3 = int(input("Enter Third Number: "))
chosen_numbers.sort()
for x in range(chosen_numbers[0], chosen_numbers[1] + 1):
    numbers.append(x * number3)
print("Result array: " + str(numbers))