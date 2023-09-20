import random
range = [0, 0]
ranges = 0
while ranges < 2:
    range[ranges] = input("Please select range " +str(ranges+1)+ ": ")
    if range[ranges].lstrip('-').isdigit():
            range[ranges] = int (range[ranges])
            if ranges == 1:
                if range[1] > range[0]: break
                else: print("The second range element has to be bigger than the first one. Try again!")
            ranges += 1
            if ranges == 0: continue
    else: print("\033[31mInvalid number/character, it has to be a number.\033[0m")
while True:
    choice = input("1 = Player, 2 = Computer Choice: ")
    if choice == '1' or choice == '2': break
    else: print("\033[31mInvalid number/character, it has to be 1 or 2.\033[0m")
guesses = round(((range[1]-range[0])/4))
guess = int(random.randrange(range[0], range[1]))
while guesses > 0:
    while True:
        if choice == '1': player = input("Guess the number: ")
        elif choice == '2':
            player = int(random.randrange(range[0], range[1]))
            print("Computer guesses: " +str(player))
        else: print("\033[31mInvalid choice. Please enter 1 or 2.\033[0m")
        if choice == '1' and player.lstrip('-').isdigit():
                player = int (player)
                if player >= range[0] and player <= range[1]: break
                else: print("You are out of range. Try again!")
        elif choice == '2': break
        else: print("\033[31mInvalid number/character, it has to be a number.\033[0m")
    guesses -= 1
    if player > guess: 
        print("The number is lower! Guesses left:", guesses)
        if choice == '2': range[1] = player
    elif player < guess:
         print("The number is higher! Guesses left:", guesses)
         if choice == '2': range[0] = player
    elif player == guess or guesses > 0: break 
if player == guess: print("Player has won!")
else: print("Out of guesses. The correct number was:", guess)