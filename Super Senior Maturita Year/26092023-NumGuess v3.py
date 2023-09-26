import random
from datetime import datetime
print(datetime.now())
def generate_rand_num(range1, range2):
    current_time = datetime.now()
    random.seed(current_time.second * 1000 + round(current_time.microsecond // 1000))
    return random.randint(range1, range2)
def get_player_guess(min_value, max_value):
    while True:
        guess = get_integer_input(f"Guess the number ({min_value}-{max_value}): ")
        if min_value <= guess <= max_value: return guess
        else: print("Your guess is out of range. Try again!")
def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError: print("\033[31mInvalid input. Please enter a valid number.\033[0m")
def game_mechanics(guess, guesses, range1, range2, array):
    while guesses > 0:
        if array is None: player = get_player_guess(range1, range2)
        guesses -= 1
        if player > guess: print("The number is lower! Guesses left:", guesses)
        elif player < guess: print("The number is higher! Guesses left:", guesses)
        elif player == guess or guesses > 0: return True
    if guesses > 1: return False
def set_both_ranges_mode(choice): 
    if choice == 1: range = [get_integer_input("Please select the first range: "), get_integer_input("Please select the second range: ")]
    elif choice == 2: range = [get_integer_input("Please select the range (the max or min is 0 for the second element of range): "), 0]
    range.sort()
    guesses = round(((range[1]-range[0])/4)+1)
    guess = generate_rand_num(range[0], range[1])
    result = game_mechanics(guess, guesses, range[0], range[1], None)
    return result, guess
def set_num_from_array():
    while True: 
        choices = input("Please enter the array in the following form: num1,num2,num3... : ")
        if choices.lstrip('-').lstrip(',').isdigit(): break
        else: print("Wrong format. Try again!")
    choice_array = choices.split(',')
    for i in range(0, len(choice_array)): choice_array[i] = int(choice_array[i])
    # return result, guess
def main():
    choice = get_integer_input("1 = Mode set Range, 2 = Mode set Range and 0, 3 = Range from array -- Choice: ")
    while choice not in (1, 2, 3):
        print("\033[31mInvalid choice. Please enter 1, 2 or 3.\033[0m")
        choice = get_integer_input("1 = Mode set Range, 2 = Mode set Range and 0, 3 = Range from array -- Choice: ")
    match choice:
        case 1:
            result = set_both_ranges_mode(1)
        case 2:
            result = set_both_ranges_mode(2)
        case 3:
            result = set_num_from_array()
        case _:
            print("1 = Mode set Range, 2 = Mode set Range and 0, 3 = Range from array")
    if result[0]: print("Player has won!")
    else: print("Out of guesses. The correct number was: ", result[1])
if __name__ == "__main__":
    main()