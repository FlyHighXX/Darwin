import Player

def read_data():
    player_list = []

    file = open("data.txt","r")
    lines = file.read().splitlines()
    file.close()

    line_count = 0
    for l in lines:
        line_count = line_count + 1

        count=0
    while count<line_count:
        name = lines[count]
        chance = float(lines[count + 1])
        wins = int(lines[count + 2])
        played = int(lines[count + 3])
        player1 = Player.Player(name,chance,wins,played)
        player_list.append(player1)
        count = count + 4
    return player_list

def write_data(player_list):
    file = open("data.txt","w")
    for player in player_list:
        name = player.name
        chance = player.chance
        wins = player.wins
        played = player.played
        file.write(name + '\n')
        file.write(str(chance) + '\n') 
        file.write(str(wins)+ '\n')
        file.write(str(played)+ '\n')
    file.close()
def new_game():
    x = 1
def show_table():
    x = 2
def main():
    player_list = read_data()


    while True:
         print("*** Welcome to tennis game ***")
         print("1. New Game\n2. Show Table\n3. Exit")
         try:
            x = input()
            x = int(x)
            if x == 1:
                new_game()
            elif x == 2:
                show_table()
            elif x == 3:
                write_data(player_list)
                exit()
            else:
                print("Number must be between 1 and 3!")
         except NameError:
             print("Input was not a number! Please try again")

main()
