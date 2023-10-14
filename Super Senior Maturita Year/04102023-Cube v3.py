import random
def dice_roll(rollSum, max_rolls):
    current_roll, history, stats = 0, [], {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6}
    while current_roll < max_rolls and sum(history) < rollSum:
        roll = random.choice([1, 2, 3, 4, 5, 6])
        if roll == 6 or (current_roll > 1 and history[-1] == roll): max_rolls += 1
        if current_roll > 1 and history[-1] == roll: print("Invalid roll!")
        else: history.append(roll)
        current_roll, stats[str(roll)] = current_roll + 1, stats[str(roll)] + 1
        print (f"Round {current_roll}: The throw is: {roll}")
    print(f"The sum of all rolls is: {sum(history)}. The average is {round(sum(history) / len(history), 2)}\n These are the statistics: " + ', '.join(f"{key}: {value}" for key, value in stats.items()))
def main():
    while True:
        choice = input("Enter 1 for 100 throws, 2 for other (idk the name), 3 to quit the app: ")
        if choice == '1': dice_roll(rollSum=float('inf'), max_rolls=100)
        elif choice == '2': dice_roll(rollSum=1000, max_rolls=float('inf'))
        elif choice == '3': break
        else: print("\033[31mInvalid choice. Please enter 1, 2, or 3.\033[0m")
if __name__ == "__main__": main()