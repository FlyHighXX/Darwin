import Player

playerList = []

file = open("data.txt","r")
lineCount = 0
for x in file:
    lineCount = lineCount + 1
file.close()

file = open("data.txt","r")
temp = file.read().splitlines()
count=2
while count < lineCount:
    name = temp[count-2]
    wins = int(temp[count-1])
    played = int(temp[count])
    playerList.append(Player.Player(name, wins, played))
    count = count + 3
file.close()

print("Data before game")
for player in playerList:
    print("%15s %3s %3s" % (player.name, player.wins, player.played))

playerList[0].wonGame()
playerList[1].looseGame()

print("Data after game1")
for player in playerList:
    print("%15s %3s %3s" % (player.name, player.wins, player.played))

playerList[0].looseGame()
playerList[1].wonGame()

print("Data after game2")
for player in playerList:
    print("%15s %3s %3s" % (player.name, player.wins, player.played))

file = open("data.txt", "w")
for player in playerList:
    file.write("%s\n" % (player.name))
    file.write("%s\n" % (str(player.wins)))
    file.write("%s\n" % (str(player.played)))
