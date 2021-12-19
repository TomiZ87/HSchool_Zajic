print("Exercise 5: Is it prime number?")
isPrime = True
number = int(input("Enter the number: "))
for x in range(2, number//2):
    if (number % x == 0):
        isPrime = False
        break
if (isPrime):
    print("The number " +str(number) + " is prime!")
else:
    print("The number " +str(number) + " is not prime!")