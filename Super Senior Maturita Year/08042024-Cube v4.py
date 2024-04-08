import random
combinations = {}
history = 0
while history < 1000:
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    if history + (roll1 + roll2) > 1000: break
    else:
        history = history + (roll1 + roll2)
        combination = "".join(sorted([str(roll1), str(roll2)]))
        if combination in combinations: combinations[combination] += 1
        else: combinations[combination] = 1
print("Stats:")
print("Sum:", history)
for x, y in combinations.items():
    print(f'"{x}": {y}')