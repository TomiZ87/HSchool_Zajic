def animal_input():
    animal = " "
    while animal.lower() != "yes" or animal.lower() != "no":
        animal = input("All Legs -> yes, otherwise no: ")
        if animal.lower() == "yes" or animal.lower() == "y": return "yes"
        elif animal.lower() == "no" or animal.lower() == "n": return "no"
        else: print("Please enter yes or no.!!!!")
def get_integer(promt):
    while True:
        try:
            number = int(input(promt))
            if number > 0: return number
            else: print("\033[31mPlease enter a positive number.\033[0m")
        except ValueError: print("\033[31mInvalid input. Please enter a positive number.\033[0m")
number_or_animals = get_integer("Please enter the number of hours/rounds: ")
monkeys = []
pinguins = []
for x in range(1, number_or_animals+1):
    print("Round " + str(x))
    monkeys.append(animal_input())
    pinguins.append(animal_input())
monkey_helped = 0
pinguin_helped = 0
for y in range(0, number_or_animals):
    if monkeys[y] == pinguins[y]: pass
    elif monkeys[y] == "yes" and pinguins[y] == "no":
        monkey_helped += 1
    elif monkeys[y] == "no" and pinguins[y] == "yes":
        pinguin_helped += 1
print("Finally, Animals helped " + str(monkey_helped+pinguin_helped) + "-times each other, monekey helped"+ str(monkey_helped) + "-times, pinguin helped"+ str(pinguin_helped) + "-times.")
