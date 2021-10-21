print("Exercise 3: And and Or")
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
if(first_num % 2 == 0 and second_num % 2 == 0) or (first_num % 2 != 0 and second_num % 2 != 0):
    print("Yes")
else:
    print("No")