import random
def choice1():
    current_throws = 0
    throws = 100
    history = []
    stats = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6}
    while current_throws < throws:
        throw = random.randint(1, 6)
        if throw == 6 or (current_throws > 1 and history[-1] == throw):
            throws += 0 
            current_throws += 0
        else:
            stats[str(throw)] += 1
            current_throws += 1
        history.append(throw)
        print (f"Round {current_throws}: The throw is: {throw}")
    print(f"The sum of all throws is: {sum(history)}. The average is {round(sum(history) / len(history), 2)}")
    print("This the history " +str(stats))
def choice2():
    current_throws = 0
    throws = 100
    history = []
    stats = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6}
    while sum(history) < 1000:
        throw = random.randint(1, 6)
        if throw == 6 or (current_throws > 1 and history[-1] == throw):
            throws += 0 
            current_throws += 0
        else:
            stats[str(throw)] += 1
            current_throws += 1
        history.append(throw)
        print (f"Round {current_throws}: The throw is: {throw}")
    print(f"The sum of all throws is: {sum(history)}. The average is {round(sum(history) / len(history), 2)}")
    print("This the history " +str(stats))
def main():
    while True:
        choice = input("Enter 1 for 100 throws and 2 for other (idk the name): ")
        if choice.isdigit():
            choice = int (choice)
            if choice == 1: choice1()
            elif choice == 2: choice2()
            else: print("\033[31mInvalid number/character, 1 or 2.\033[0m")
        else: print("\033[31mInvalid number/character\033[0m")
if __name__ == "__main__": main()
