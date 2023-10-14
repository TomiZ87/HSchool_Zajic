import random
history = []
while sum(history) < 1000:
    roll = random.choice([1, 2, 3, 4, 5, 6])
    history.append(roll)
    print (f"Round {len(history)}: The throw is: {roll}")
print("Stats:")
for number in range(1, 7):
    roll_num = 0
    for i, roll in enumerate(history):
        if roll == number: roll_num += 1
    print(f"Number {number} was rolled {roll_num} times.")
print(f"The sum of all rolls is: {sum(history)}. The average is {round(sum(history) / len(history), 2)}")