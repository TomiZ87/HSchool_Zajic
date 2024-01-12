from tinydb import TinyDB, Query
tournament_array = []
def get_integer(promt):
    while True:
        try:
            number = int(input(promt))
            return number
        except ValueError: print("\033[31mInvalid input. Please enter a positive whole number.\033[0m")

db = TinyDB("./Super Senior Maturita Year/files/22112023-FootBallTournament.txt")

def enter_new_result():
    print("Enter New Results:")
    team1 = input("Enter the name of Team 1: ")
    score1 = get_integer("Enter the score of Team 1: ")
    team2 = input("Enter the name of Team 2: ")
    score2 = get_integer("Enter the score of Team 2: ")
    db.insert({'Team 1': team1, 'Score 1': score1, 'Team 2': team2, 'Score 2': score2})
    return

def view_all_results():
    if len(db) == 0:
        print("There are no results to modify")
        return
    else:
        print("Printing all results:")
        x = 1
        for y in db:
            print("ID " + str(y.doc_id) + ". - " + str(y))
            x += 1 
    return

def view_by_team():
    if len(db) == 0:
        print("There are no results to view")
        return
    else:
        team = input("Thich team do you want to view? ")
        search = Query()
        db.search(search['Team 1'] == team | search['Team 2'] == team)
        for y in db:
            print("ID " + str(y.doc_id) + ". - " + str(y))
        while True:
            try:
                line = get_integer("Enter the ID: ")
                if db.contains(doc_id = line):
                    db.remove(doc_ids=[line])
                else: print("ID Not Found")
                return
            except ValueError: print("\033[31mThe ID does Not exist.\033[0m")

def view_by_line():
    if len(db) == 0:
        print("There are no results to view")
        return
    else:
        print("Which result do you want to view? Choose the line between 1 and " + str(len(db))) 
        while True:
            try:
                line = get_integer("Enter the line: ")
                if 1 >= line >= (len(db)):
                    print(db.all()[line - 1])
                return
            except ValueError: print("\033[31mThe Line does Not exist.\033[0m")

def delete_result():
    if len(db) == 0:
        print("There are no results to modify")
        return
    else:
        print("Which result do you want to delete? Choose the ID")
        for y in db:
            print("ID " + str(y.doc_id) + ". - " + str(y))
        while True:
            try:
                line = get_integer("Enter the ID: ")
                if db.contains(doc_id = line):
                    print("Line")
                    db.get(doc_id = line)
                else: print("ID Not Found")
                return
            except ValueError: print("\033[31mThe ID does Not exist.\033[0m")

def modify_result():
    if len(db) == 0:
        print("There are no results to modify")
        return
    else:
        print("Choose the ID to change")
        for y in db:
            print("ID " + str(y.doc_id) + ". - " + str(y))
        while True:
            try:
                line = get_integer("Enter the ID: ")
                if db.contains(doc_id = line):
                    db.get(doc_id = line)
                    team1 = input("Enter the name of Team 1: ")
                    score1 = get_integer("Enter the score of Team 1: ")
                    team2 = input("Enter the name of Team 2: ")
                    score2 = get_integer("Enter the score of Team 2: ")
                    db.update({'Team 1': team1, 'Score 1': score1, 'Team 2': team2, 'Score 2': score2}, doc_ids=[line])
                else: print("ID Not Found")
                return
            except ValueError: print("\033[31mThe ID does Not exist.\033[0m")

def choose_option():
    while True:
        print("1 - Enter New Football result")
        print("2 - View all Football results")
        print("3 - View all Football results by Country/Team")
        print("4 - View the result by number of line")
        print("5 - Delete a result")
        print("6 - Modify a result")
        choose = input("Choose bewteen 1-6 or Q to quit the program: ")
        match choose:
            case "1": enter_new_result()
            case "2": view_all_results()
            case "3": view_by_team()
            case "4": view_by_line()
            case "5": delete_result()
            case "6": modify_result()
            case "Q": exit()
            case "q": exit()
            case _: print("You have chosen an option outside of this program. Please try again!")

choose_option()