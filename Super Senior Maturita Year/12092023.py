import random
player_score = [0, 0] # Zero is player, one is computer 
roll = ['r','p','s']
p_win = ["Rock Scissors","Paper Rock","Scissors Paper"]
history = []
round = 0
winning_rounds = int(input("How many rounds is needed for a win? Number: "))
def display_roll(roll):
    if roll == 'r': roll_result = "Rock"
    elif roll == 'p': roll_result = "Paper"
    elif roll == 's': roll_result = "Scissors"
    else:roll_result = "Unknown"
    return roll_result
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
    elif (display_roll(player) + " " + display_roll(computer)) in p_win:
        print ("Player wins this round!")
        player_score[0] += 1
    else:
        print ("Computer wins this round!")
        player_score[1] += 1
    round = round + 1
    history.append("Round " +str(round)+ "Player: "+str(player_score[0]) + " " +str(display_roll(player))+"; Computer: " +str(player_score[1])+ " " +str(display_roll(computer)))
    print ("Player: "+str(player_score[0]) + "; Computer: " +str(player_score[1]))
if player_score[0] == winning_rounds: print ("Player WINS")
else: print ("COMPUTER WINS!")
for x in history: print(x)