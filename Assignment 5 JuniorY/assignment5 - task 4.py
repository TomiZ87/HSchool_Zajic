print("Exercise 4: All divisors of entered number")
result = []
number = int(input("Enter the number: "))
for x in range(1, number):
    if (number % x == 0):
        numbers = number / x
        result.append(numbers)
result.append(1.0)
print("Dividers of number "+ str(number) + " is " +str(result))