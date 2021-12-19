def task1():
    print("Exercise 1: Advanced Counting")
    chosen_numbers = []
    numbers = []
    chosen_numbers.append(int(input("Enter First Number: ")))
    chosen_numbers.append(int(input("Enter Second Number: ")))
    chosen_numbers.sort()
    for x in range(chosen_numbers[0], chosen_numbers[1] + 1):
       numbers.append(x)
    print("Result array: " + str(numbers))

def task2():
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

def task3():
    print("Exercise 3: Vowels in word")
    letters = []
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    word = str(input("Enter some word: "))
    for x in word.lower():
        if x in vowels:
            letters.append(x)
    print(letters)

def task4():
    print("Exercise 4: All divisors of entered number")
    result = []
    number = int(input("Enter the number: "))
    for x in range(1, number):
        if (number % x == 0):
            numbers = number / x
            result.append(numbers)
    result.append(1.0)
    print("Dividers of number "+ str(number) + " is " +str(result))

def task5():
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

#When you star this program you can chose the function from 1 to 5. Each task number corresponds to the number of function you can choose.
task_num = int(input("Enter the number of the task (1-5): "))
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
else:
    print("The selected task doesn't exist! (Try again in interval of 1-5)")