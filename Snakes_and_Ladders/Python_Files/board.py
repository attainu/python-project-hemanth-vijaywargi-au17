from random import randint
from os import system
import art


class Board:
    def __init__(self, size, Tsnakes, Tladders, players):
        self.size = size
        self.snakes = self.generateSnakes(Tsnakes)
        self.ladders = self.generateLadders(Tladders)
        self.players = players

    def printPositions(self):
        system("cls")
        print(art.logo)
        for p in self.players:
            print(f"{p}'s Position : {self.players[p]} ", end="\n\n")

    def updatePos(self, player, diceVal):
        newPos = self.players[player]+diceVal
        if newPos <= self.size:

            print(f"{player} rolled a {diceVal}",
                  f"and moved from {self.players[player]} to {newPos}")
            
            if newPos in self.snakes:
                print(art.snakeArt)
                print(f"{player} got Bitten by a Snake at {newPos} !",
                      f"{player} goes down to {self.snakes[newPos]}.")
                self.players[player] = self.snakes[newPos]

            elif newPos in self.ladders:
                print(art.ladderArt)
                print(f"{player} found a Ladder at {newPos} !",
                      f"{player} goes up to {self.ladders[newPos]}.")
                self.players[player] = self.ladders[newPos]

            else:
                self.players[player] = newPos
        else:
            print(f"Too many Steps ! Try again next Time {player}")

    def generateSnakes(self, Tsnakes):
        snakes = {}
        i = 0
        while i < Tsnakes:
            snakeHead = randint(11, self.size-1)
            if (snakeHead not in snakes):
                if (snakeHead not in snakes.values()):
                    snakes[snakeHead] = randint(2, snakeHead-6)
                    i += 1
        return snakes

    def generateLadders(self, Tladders):
        ladders = {}
        i = 0
        while i < Tladders:
            ladderTop = randint(11, self.size-1)
            if (ladderTop not in ladders):
                if (ladderTop not in ladders.values()):
                    if (ladderTop not in self.snakes):
                        ladders[randint(2, ladderTop-6)] = ladderTop
                        i += 1
        return ladders

