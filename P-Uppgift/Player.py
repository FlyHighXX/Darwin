class Player:
    def __init__(self, name, chance, wins, played):
        self.name = name
        self.chance = chance
        self.wins = wins
        self.played = played

    def wonGame(self):
        self.wins = self.wins + 1
        self.played = self.played + 1

    def looseGame(self):
        self.played = self.played + 1
