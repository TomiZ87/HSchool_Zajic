print("Exercise 1: Advanced Counting")
chosen_numbers = []
numbers = []
chosen_numbers.append(int(input("Enter First Number: ")))
chosen_numbers.append(int(input("Enter Second Number: ")))
chosen_numbers.sort()
for x in range(chosen_numbers[0], chosen_numbers[1] + 1):
    numbers.append(x)
print("Result array: " + str(numbers))