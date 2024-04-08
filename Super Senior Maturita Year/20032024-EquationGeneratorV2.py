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
while ranges[0] <= ranges[1]:
    ranges[0] = get_integer("Please enter the lower range: ", 0, None)
    ranges[1] = get_integer("Please enter the higher range: ", 0, None)
    if ranges[0] >= ranges[1]: print("\033[31mFirst number has to be larger than the second one\033[0m")
    else: break
history = {'c': 0, 'w': 0}
operation = '+'
equations = {}
equation = ""
for x in range(num_of_equations):
    number1 = random.randint(ranges[0], ranges[1])
    number2 = random.randint(ranges[0], ranges[1])
    equation = str(number1) + str(operation) + str(number2)
    player_answer = get_integer(str(x+1) + ". ///  " + str(number1) + " " + str(operation) + " " + str(number2) + " = ", 0, None)
    result = number1 + number2
    equations[equation] = player_answer
    if result == player_answer: 
        history['c'] += 1
        print(str(x+1) + ". /// Correct ///  " + str(number1) + " " + str(operation) + " " + str(number2) + " = " + str(result))
    else:
        history['w'] += 1
        print(str(x+1) + ". /// Incorrect ///  " + str(number1) + " " + str(operation) + " " + str(number2) + " = " + str(result))
print("Totally, " + str(history['c']+history['w']) + " equations. You answered correctly " + str(history['c']) + "-times (" + str(round(history['c']/num_of_equations*100)) + "%) and incorrectly "  + str(history['w']) + "-times. The ratio is "  + str(history['c']) + ":" + str(history['w']))
num = 1
print("History:")
for x, y in equations.items():
    if int(eval(x)) == y: temp = "Correct"
    else: temp = "Wrong"
    print(f'{num}  ---  "{x}": {y} /// {temp} /// {int(eval(x))}')
    num += 1