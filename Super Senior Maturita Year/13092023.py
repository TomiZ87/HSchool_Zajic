import random
def display_roll(roll):
    rolls = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    return rolls.get(roll, 'Unknown')
def main():
    player_score = [0, 0]  # 0 is player, 1 is computer 
    roll = ['r', 'p', 's']
    p_win = {'rs': 'Rock Scissors', 'pr': 'Paper Rock', 'sp': 'Scissors Paper'}
    history = []
    round_num = 0
    player_moves = [{'r': 0, 'p': 0, 's': 0}, {'r': 0, 'p': 0, 's': 0}]
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
        if player == computer: print("It's a draw this round!")
        elif player + computer in p_win:
            print("Player wins this round!")
            player_score[0] += 1
        else:
            print("Computer wins this round!")
            player_score[1] += 1
        round_num += 1
        player_moves[0][player] += 1
        player_moves[1][computer] += 1
        history.append(f"Round {round_num} -- Player: {player_score[0]} {display_roll(player)}; Computer: {player_score[1]} {display_roll(computer)}\n Statistics: Player: [r: {player_moves[0]['r']}; p: {player_moves[0]['p']}; s: {player_moves[0]['s']}]; Computer: [r: {player_moves[1]['r']}; p: {player_moves[1]['p']}; s: {player_moves[1]['s']}]")
        print(f"Player: {player_score[0]}; Computer: {player_score[1]}")
    if player_score[0] == winning_rounds: print("Player WINS!")
    else: print("COMPUTER WINS!")
    for x in history: print(x)
if __name__ == "__main__": main()