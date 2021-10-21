print("Exercise 1: Division of Numbers")
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
if(first_num % second_num == 0):
    result = first_num/second_num
    print("The number is divisible by " + str(second_num) + ". Equation: " + str(first_num) + "/" + str(second_num) + "=" + str(result))
else:
    result = first_num/second_num
    print("The number is not divisible by " + str(second_num) + ". Equation: " + str(first_num) + "/" + str(second_num) + "=" + str(result) + " Remainder: " + str(first_num % second_num))