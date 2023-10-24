import random
import math
range1, range2 = 0, 100
x = round((range2 - range1) / 2)
guess = random.randrange(range1, range2+1)
while x != guess:
    if guess > x:
        range1 = x
        print("The number is higher. Current attempt:", x)
        x = x + math.ceil((range2 - x) / 2)
    elif guess < x:
        range2 = x
        print("The number is lower. Current attempt:", x)
        x = x - math.ceil((x - range1) / 2)
if x == guess: print("Indeed! The number was:", x)