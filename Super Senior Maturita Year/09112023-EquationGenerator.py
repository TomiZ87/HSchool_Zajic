import random
def get_integer(promt, mode, ranges):
    while True:
        try:
            number = int(input(promt))
            if mode == 1:
                if number > ranges: return number
            else: return number
        except ValueError: print("\033[31mInvalid input. Please enter a valid number.\033[0m")
num_of_equations = get_integer("Please enter the number: ", 1, 0)
ranges = [0, 0]
while ranges[0] < ranges[1]:
    ranges[0] = get_integer("Please enter the lower range: ", 0, None)
    ranges[1] = get_integer("Please enter the higher range: ", 0, None)
    if ranges[0] >= ranges[1]: print("\033[31mFirst number has to be larger than the second one/\033[0m")
history = {'c': 0, 'w': 0}
operation = ['+', '-', '*']
for x in range(num_of_equations):
    current_operator = random.choice(operation)
    number1 = random.randint(ranges[0], ranges[1])
    number2 = random.randint(ranges[0], ranges[1])
    player_answer = get_integer(str(x+1) + ". ///  " + str(number1) + " " + str(current_operator) + " " + str(number2) + " = ", 0, None)
    if current_operator == '+': result = number1 + number2
    elif current_operator == '-': result = number1 - number2
    elif current_operator == '*': result = number1 * number2
    if result == player_answer: 
        history['c'] += 1
        print(str(x+1) + ". /// Correct ///  " + str(number1) + " " + str(current_operator) + " " + str(number2) + " = " + str(result))
    else:
        history['w'] += 1
        print(str(x+1) + ". /// Incorrect ///  " + str(number1) + " " + str(current_operator) + " " + str(number2) + " = " + str(result))
print("You answered correctly " + str(history['c']) + "-times (" + str(round(history['c']/num_of_equations*100)) + "%) and incorrectly "  + str(history['w']) + "-times. The ratio is "  + str(history['c']) + ":" + str(history['w']))