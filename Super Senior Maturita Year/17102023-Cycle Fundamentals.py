import random
#For loop and while exercises
fruits = ["apple ", "cherry ", "watermellon ", "apricot ", "grape ", "fig ", "date "]

# 1 - Print the individual elemtents from the list(max. 2 lines) using for loop
for i in fruits: print("Fruit: " + str(i))

# 2 - Print the individual elements with the position in the list, startin from 1 (max. 2 lines) using for loop
for i in range(1, len(fruits)): print("Fruit Num. " +str(i)+ " : " + str(fruits[i]))

# 3 - Print the elements in range (2nd - 5th position) from the list (max. 2 lines) using for loop
for i in range(1, 5): print("Fruit: " + str(fruits[i]))

# 4 - Print every 3rd element of the list (max. 2 lines) using for loop
for i in range(0, len(fruits), 3): print("Fruit: " + str(fruits[i]))

print("Test")
# 5 - Print the individual elemtents from the list using while cycle
index = 0
while index < len(fruits):
    print("Fruit: " + str(fruits[index]))
    index += 1

# 6 - Print the elements in range (2nd - 5th position) from the list (max. 2 lines) using while cycle
print("Test")
index = 1
while index < 5:
    print("Fruit: " + str(fruits[index]))
    index += 1

# 7 - Print every 3rd element of the list using while cycle
print("Test")
index = 0
while index < len(fruits):
    print("Fruit: " + str(fruits[index]))
    index += 3

# 8 - Print the individual elements with the position in the list, startin from 1 using while cycle
print("Test")
index = 1
while index < len(fruits):
    print("Fruit Num. " +str(index)+ " : " + str(fruits[index]))
    index += 1

number=int(input("Add number: "))
number_list = []
number_list.append(number)

# 9 - Enter a number in range 0 and 100 using while cycle
number = 0
while (0 <= number <= 100):
    number=int(input("Add number: "))
    number_list.append(number)

# 10 - Enter a number in range 0 and 100 using while cycle (the last entered element is not in the list)
number = 0
while (0 <= number <= 100):
    number=int(input("Add number: "))

# 11 - Enter a number in range that you set using while cycle
start = int(input("Add start: "))
end = int(input("Add end: "))
number = random.randint(start, end)
while (start <= number <= end):
    number=int(input("Add number: "))
    number_list.append(number)