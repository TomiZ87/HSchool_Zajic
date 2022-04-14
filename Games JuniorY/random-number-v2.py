from decimal import Rounded
import numbers
import random
players_num = 0
while players_num < 1 or players_num > 5:
    players_num = int(input("How many players? 2-5 : "))

players = []

for x in range(0, players_num):
    nickname = input("Player "+str(x+1)+" Nickname: ")
    mode = -1
    while mode < 0 or mode > 3:
        mode = int(input(str(nickname)+ ": Is the player computer or another human? 1 for another player, 2 for computer: "))
    players.append({
    "nickname": nickname,
    "mode": mode,
    "numbers": []
})


num1 = int(input("Choose the number range. Number 1: "))
num2 = num1 - 1
while num2 < num1:
    num2 = int(input("Choose the number range. Has to be larger than Number 1, Number 2: "))
print("The range is " +str(num1) + "-" + str(num2))
attempts = int((num2-num1)/2)
guessing_num = random.randint(num1, num2)
round = 1

win = False
winwin = False
while round < attempts and not win:
    print("\n\nRound " +str(round))
    for x in range(0, players_num):
        if not winwin:
            if players[x]["mode"] == 1:
                players[x]["numbers"].append(int(input(str(players[x]["nickname"])+ " Guess: ")))
            else:
                players[x]["numbers"].append(random.randint(num1, num2))
                print(str(players[x]["nickname"])+ " Guess: " +str(players[x]["numbers"][round-1]))
            attempts -= 1
            if players[x]["numbers"][round-1] > guessing_num:
                print("The number is lower!")
                if num2 > players[x]["numbers"][round-1]:
                    num2 = players[x]["numbers"][round-1]
            elif players[x]["numbers"][round-1] < guessing_num:
                print("The number is higher!")
                if num1 < players[x]["numbers"][round-1]:
                    num1 = players[x]["numbers"][round-1]
            print(str(attempts) + " attempts left!")
            if players[x]["numbers"][round-1] == guessing_num:
                players[x]["numbers"][round-1] = str(players[x]["numbers"][round-1]) + " <-- Guessed Number"
                print("\n\nWow, " +str(players[x]["nickname"])+ " You are right, the correct number is " +str(guessing_num))
                winwin = True
        else:
            if players[x]["mode"] == 1:
                players[x]["numbers"].append(str("n/a"))
            else:
                players[x]["numbers"].append((str("n/a")))
    if winwin:
        win = True
    round += 1
    

if attempts == 0:
    print("\n\nYou all lost")
print("The correct answer was " +str(guessing_num))
print("Here is your history:")
for x in range(1, round):
    for y in range(0, players_num):
        print("Round " +str(x) + " " +players[y]["nickname"]+ ": " +str(players[y]["numbers"][x-1]))
print("You had " +str(attempts)+ " attempts left!")