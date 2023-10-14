num_legs=1
list1 = []
list2 = []
while num_legs != 0:
    num_legs = int(input("How many legs does the animal have? Num: "))
    if num_legs % 2 == 0 and num_legs != 0:
        list1.append(num_legs)
    elif num_legs % 2 == 1:
        list2.append(num_legs)
        list1.append(num_legs-1)
print("The number of legs of all animals: ")
for x in list1: print(x)
print("The number of legs of all mutated animals before the operation: ")
for x in list2: print(x)
print("The number of all animals: "+str(len(list1)))
print("The number of all mutated animals before the operation: "+str(len(list2)))