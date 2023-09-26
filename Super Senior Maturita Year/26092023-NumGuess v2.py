import random
def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError: print("\033[31mInvalid input. Please enter a valid number.\033[0m")
def get_player_guess(min_value, max_value):
    while True:
        guess = get_integer_input(f"Guess the number ({min_value}-{max_value}): ")
        if min_value <= guess <= max_value: return guess
        else: print("Your guess is out of range. Try again!")
def main():
    choice = get_integer_input("1 = Player, 2 = Computer Choice: ")
    while choice not in (1, 2):
        print("\033[31mInvalid choice. Please enter 1 or 2.\033[0m")
        choice = get_integer_input("1 = Player, 2 = Computer Choice: ")
    range = [get_integer_input("Please select the first range: "), get_integer_input("Please select the second range: ")]
    range.sort()
    guesses = round(((range[1]-range[0])/4)+1)
    guess = int(random.randrange(range[0], range[1]))
    while guesses > 0:
        if choice == 1: 
            player = get_player_guess(range[0], range[1])
        elif choice == 2:
            player = int(random.randrange(range[0], range[1]))
            print("Computer guesses: " +str(player))
        guesses -= 1
        if player > guess: 
            print("The number is lower! Guesses left:", guesses)
            if choice == 2: range[1] = player
        elif player < guess:
            print("The number is higher! Guesses left:", guesses)
            if choice == 2: range[0] = player
        elif player == guess or guesses > 0: break 
    if player == guess: print("Player has won!")
    else: print("Out of guesses. The correct number was: ", guess)
if __name__ == "__main__":
    main()