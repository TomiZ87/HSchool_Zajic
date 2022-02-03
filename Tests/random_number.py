import random
print("Number Guessing Game:");
attempts = int(input("Enter the number of attempt for this game: "));
max_number = int(input("Enter the max number you want to guess (have to be more than 0): "));
cur_attempt = 1;
guessing_num = random.randint(0, max_number);
numbers = []

if max_number > 0:
    while cur_attempt <= attempts:
        if cur_attempt == attempts:
            print("Warning!! Last Attempt no. " +str(cur_attempt));
        else:
            print("Attempt : " + str(cur_attempt));
        guess = int(input("Guess Number: "));
        if guess != guessing_num:
            numbers.append(guess);
            if guessing_num > guess:
                print("The number is higher!")
            else:
                print("The number is lower!")
        if guess == guessing_num:
            print("You won within the " +str(cur_attempt)+ " attempts, Guessed Number is indeed " + str(guessing_num));
            print("You entered these wrong guesses " + str(numbers));
            break;
        if cur_attempt == attempts:
            print("You lose, you used all your " + str(attempts) + " attempts. The correct answer was " + str(guessing_num));
            print("You entered these wrong guesses " + str(numbers));
            break;
        cur_attempt += 1;
