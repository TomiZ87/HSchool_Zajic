import random
print("Rock - Paper - Scissors")
print("Game configuration:")
players = [{
    "mode": 1,
    "score": 0,
    "roll": ''
},{
    "mode": 1,
    "score": 0,
    "roll": ''
}]
winning_rounds = int(input("How many rounds is needed for a win? Number: "))
players[1]["mode"] = int(input("Who you want to play with? 1 - Another Player, 2 - Computer : "))
print("Tutorial: You enter the letters for each option")
print("r - Rock, p - Paper, s - Scissors")
roll = ['r','p','s']
history = []
roundnum = 1
roundwinner = 0
roundwinner_text = ""
score_text = ""
guessing = False

def display_roll(roll):
    if roll == 'r':
        roll_result = "Rock"
    elif roll == 'p':
        roll_result = "Paper"
    elif roll == 's':
        roll_result = "Scissors"
    else:
        roll_result = "Unknown"
    return roll_result

print("Play honestly!")
while players[0]["score"] < winning_rounds and players[1]["score"] < winning_rounds:
    roundwinner = 0
    print("Round "+str(roundnum))
    guessing = True
    while guessing:
        players[0]["roll"] = str(input("Player 1 Roll: "))
        players[0]["roll"] = players[0]["roll"].lower()
        if players[0]["roll"] == 'r' or players[0]["roll"] == 'p' or players[0]["roll"] == 's':
            guessing = False
        else:
            print("Invalid character. Please enter r for rock, p for paper, or s for scissors.")
    if players[1]["mode"] == 1:
        guessing = True
        while guessing:
            players[1]["roll"] = str(input("Player 2 Roll: "))
            players[1]["roll"] = players[1]["roll"].lower()
            if players[1]["roll"] == 'r' or players[1]["roll"] == 'p' or players[1]["roll"] == 's':
                guessing = False
            else:
                print("Invalid character. Please enter r for rock, p for paper, or s for scissors.")
    elif players[1]["mode"] == 2:
        players[1]["roll"] = random.choice(roll)
        print("Player 2 Roll: " +str(players[1]["roll"]))

    if players[0]["roll"] == 'r':
        if players[1]["roll"] == 's':
            players[0]["score"] += 1
            roundwinner = 1
        elif players[1]["roll"] == 'p':
            players[1]["score"] += 1
            roundwinner = 2
    elif players[0]["roll"] == 'p':
        if players[1]["roll"] == 's':
            players[1]["score"] += 1
            roundwinner = 2
        elif players[1]["roll"] == 'r':
            players[0]["score"] += 1
            roundwinner = 1
    elif players[0]["roll"] == 's':
        if players[1]["roll"] == 'p':
            players[0]["score"] += 1
            roundwinner = 1
        elif players[1]["roll"] == 'r':
            players[1]["score"] += 1
            roundwinner = 2
    elif players[0]["roll"] == players[1]["roll"]:
        roundwinner = 3
    rollplayer1 = display_roll(players[0]["roll"])
    rollplayer2 = display_roll(players[1]["roll"])

    if roundwinner == 1 or roundwinner == 2:
        roundwinner_text = "Player " +str(roundwinner)+ " Won!"
    else:
        roundwinner_text = "Its a Draw!"
    score_text = " Score: "+str(players[0]["score"])+ ":" +str(players[1]["score"])
    result_round = "Round " +str(roundnum)+ "! " +str(rollplayer1)+ " vs " +str(rollplayer2)+ "! " +str(roundwinner_text)+ "" +str(score_text) + ""
    print(result_round)
    history.append(result_round)
    
    roundnum += 1
print("\n\nFinal score: "+str(score_text)+" Player " +str(roundwinner)+ " won!")
print("History of rounds:")
for x in history:
    print(x)