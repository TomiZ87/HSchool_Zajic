import random
player_score = [0, 0] # Zero is player, one is computer 
roll = ['r','p','s']
p_win = ['rs','pr','sp']
history = []
winning_rounds = int(input("How many rounds is needed for a win? Number: "))
while player_score[1] < winning_rounds and player_score[0] < winning_rounds:
    guessing = True
    while guessing:
        player = str(input("Player  Roll: "))
        player = player.lower()
        if player in roll: guessing = False
        else: print("Invalid character. Please enter r for rock, p for paper, or s for scissors.")
    computer = random.choice(roll)
    print ("Computer Roll: " +str(computer))
    if player == computer: print ("It is a draw this round!")
    elif (player + computer) in p_win:
        print ("Player wins this round!")
        player_score[0] += 1
    else:
        print ("Computer wins this round!")
        player_score[1] += 1
    history.append(player + computer)
    print ("Player: "+str(player_score[0]) + "; Computer: " +str(player_score[1]))
if player_score[0] == winning_rounds: print ("Player WINS")
else: print ("COMPUTER WINS!")
for x in history: print(x)