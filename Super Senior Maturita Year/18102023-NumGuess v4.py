import random
range1 = 0
range2 = 100
x = range2 + 1
guess = random.randint(range1, range2)
print(guess)
while x != guess:
    if x == (range2 + 1):
        x = 50
        if guess > x: print("The number is higher. Current attempt:", x)
        if guess < x: print("The number is lower. Current attempt:", x)
    else:
        if guess > x:
            range1 = x
            print("The number is higher. Current attempt:", x)
            x = x + round((range2 - x) / 2)
        elif guess < x:
            range2 = x
            print("The number is lower. Current attempt:", x)
            x = x - round((x - range1) / 2)
        elif x == guess:
            print("Indeed! The number was:", x)
            break