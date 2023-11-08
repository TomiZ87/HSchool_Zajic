def get_integer(promt):
    while True:
        try:
            number = int(input(promt))
            if number > 0: return number
        except ValueError: print("\033[31mInvalid input. Please enter a valid number.\033[0m")
animals_to_buy, owned_animals = [], []
money, number_of_animals = get_integer("Please enter the amount of money: "), get_integer("Please enter the number of animals (species) that will be available: ")
for x in range(1, number_of_animals+1): 
    animals_to_buy.append(get_integer("Please enter the price for animal num. " +str(x) + ": "))
animals_to_buy_copy = animals_to_buy
while True:
    choice = get_integer("1 -> Buy the cheapest, 2 -> Buy the most expensive, 3 Quit the program: ")
    if choice <= 3: break
    else: print("\033[31mInvalid choice. Please enter 1, 2, or 3.\033[0m")
if choice == 1 or choice == 2:
    while money > 0 and len(animals_to_buy_copy) > 0:
        if choice == 1: chosen_animal = min(animals_to_buy_copy)
        else: chosen_animal = max(animals_to_buy_copy)
        if money >= chosen_animal:
            owned_animals.append(chosen_animal)
            money -= chosen_animal
            animals_to_buy_copy.remove(chosen_animal)
        else: break
    owned_animals.sort()
    print("Remaining animals to buy " + str(animals_to_buy_copy) + "; Animals you own " + str(owned_animals) + "; Remaining money " + str(money))