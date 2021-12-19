def task1():
    print("Exercise 1: Counting numbers (make sure the first entered number is lower than the second one)")
    numbers = []
    number1 = int(input("Enter First Number: "))
    number2 = int(input("Enter Second Number: "))
    if (number1 > number2):
       print("Error - The number 1 is bigger than number 2. Cannot Count from num1 to num2")
    else:
        for x in range(number1, number2 + 1):
           numbers.append(x)
        print("Result array: " + str(numbers))

def task2():
    print("Exercise 2: Advanced Counting")
    chosen_numbers = []
    numbers = []
    chosen_numbers.append(int(input("Enter First Number: ")))
    chosen_numbers.append(int(input("Enter Second Number: ")))
    chosen_numbers.sort()
    for x in range(chosen_numbers[0], chosen_numbers[1] + 1):
       numbers.append(x)
    print("Result array: " + str(numbers))

def task3():
    print("Exercise 3: Multiplying numbers")
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

def task4():
    print("Exercise 4: Vowels in word")
    letters = []
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    word = str(input("Enter some word: "))
    for x in word.lower():
        if x in vowels:
            letters.append(x)
    print(letters)

def task5():
    print("Exercise 5: All divisors of entered number")
    result = []
    number = int(input("Enter the number: "))
    for x in range(1, number):
        if (number % x == 0):
            numbers = number / x
            result.append(numbers)
    result.append(1.0)
    print("Dividers of number "+ str(number) + " is " +str(result))

def task6():
    print("Exercise 6: Is it prime number?")
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

def task7():
    print("Exercise 7: Every third number from 0 to 100")
    result = []
    for x in range(0, 101):
        if (x % 3 == 0):
            result.append(x)
    print("Result Array: " + str(result))

def task8():
    print("Exercise 8: Decreasing Counting")
    chosen_numbers = []
    numbers = []
    chosen_numbers.append(int(input("Enter First Number: ")))
    chosen_numbers.append(int(input("Enter Second Number: ")))
    chosen_numbers.sort()
    for x in range(chosen_numbers[0], chosen_numbers[1] + 1):
       numbers.append(x)
    numbers.sort(reverse=True)
    print("Result array: " + str(numbers))

#When you star this program you can chose the function from 1 to 8. Each task number corresponds to the number of function you can choose.
task_num = int(input("Enter the number of the task (1-8): "))
if task_num == 1:
    task1()
elif task_num == 2:
    task2()
elif task_num == 3:
    task3()
elif task_num == 4:
    task4()
elif task_num == 5:
    task5()
elif task_num == 6:
    task6()
elif task_num == 7:
    task7()
elif task_num == 8:
    task8()
else:
    print("The selected task doesn't exist! (Try again in interval of 1-8)")