import random
from datetime import datetime
def display_roll(roll):
    rolls = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    return rolls.get(roll, 'Unknown')
def save(saveing_material):
    f = open("./Super Senior Maturita Year/files/13092023.txt", "a")
    f.write("\nGame: "+str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
    for x in saveing_material: f.write(x)
    f.close()
def main():
    player_score = [0, 0]  # 0 is player, 1 is computer 
    roll = ['r', 'p', 's']
    p_win = {'rs': 'Rock Scissors', 'pr': 'Paper Rock', 'sp': 'Scissors Paper'}
    round_num = 0
    history, player_moves, outcome_counts = [], [{'r': 0, 'p': 0, 's': 0}, {'r': 0, 'p': 0, 's': 0}], [{'r': 0, 'p': 0, 's': 0}, {'r': 0, 'p': 0, 's': 0}, {'r': 0, 'p': 0, 's': 0}] # 0 = WINS, 1 = LOSES, 2 = DRAWS
    while True:
        winning_rounds = input("How many rounds are needed for a win? Number: ")
        if winning_rounds.isdigit():
            winning_rounds = int (winning_rounds)
            if winning_rounds > 0: break
        else: print("\033[31mInvalid number/character, it has to be a number and be positive.\033[0m")
    while player_score[1] < winning_rounds and player_score[0] < winning_rounds:
        while True:
            player = input("Player Roll: ").lower()
            if player in roll: break
            else: print("\033[31mInvalid character. Please enter 'r' for rock, 'p' for paper, or 's' for scissors.\033[0m")
        computer = random.choice(roll)
        print("Computer Roll:", display_roll(computer))
        if player == computer:
            result = "It's a draw!"
            outcome_counts[2][player] =+ 1
        elif player + computer in p_win:
            result = "Player wins this round!"
            player_score[0] += 1
            outcome_counts[0][player] =+ 1
            outcome_counts[1][computer] =+ 1
        else:
            result = "Computer wins this round!"
            player_score[1] += 1
            outcome_counts[1][player] =+ 1
            outcome_counts[0][computer] =+ 1
        round_num += 1
        player_moves[0][player] += 1
        player_moves[1][computer] += 1
        history.append(f"\nRound {round_num} -- Player: {player_score[0]} {display_roll(player)}; Computer: {player_score[1]} {display_roll(computer)} {result}\n Statistics: Player: [r: {player_moves[0]['r']}; p: {player_moves[0]['p']}; s: {player_moves[0]['s']}]; Computer: [r: {player_moves[1]['r']}; p: {player_moves[1]['p']}; s: {player_moves[1]['s']}]")
        print(f"{result} Player: {player_score[0]}; Computer: {player_score[1]}")
    if player_score[0] == winning_rounds: print("Player WINS!")
    else: print("COMPUTER WINS!")
    for x in history: print(x)
    print(f"The most games were won with: {max(outcome_counts[0], key=outcome_counts[0].get).upper()}: {max(outcome_counts[0].values())}; lost with {max(outcome_counts[1], key=outcome_counts[1].get).upper()}: {max(outcome_counts[1].values())}; and draws with {max(outcome_counts[2], key=outcome_counts[2].get).upper()}: {max(outcome_counts[2].values())}")
    history.append(f"\nThe most games were won with: {max(outcome_counts[0], key=outcome_counts[0].get).upper()}: {max(outcome_counts[0].values())}; lost with {max(outcome_counts[1], key=outcome_counts[1].get).upper()}: {max(outcome_counts[1].values())}; and draws with {max(outcome_counts[2], key=outcome_counts[2].get).upper()}: {max(outcome_counts[2].values())}\n")
    save(history)
if __name__ == "__main__": main()