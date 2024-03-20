import math
import random
ranges = [0, 100]
guess = random.randint(ranges[0], ranges[1])
guessing = math.ceil((ranges[1] - ranges[0]) / 2)
while guessing != guess:
    if guess > guessing:
        ranges[0] = guessing
        guessing = guessing + math.ceil((ranges[1] - guessing) / 2)
    elif guess < guessing:
        ranges[1] = guessing
        guessing = guessing - math.ceil((guessing - ranges[0]) / 2)

print(guessing, ' ', guess)
