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

        while len(snakes) < Tsnakes:
            SnakeTail = randint(2, self.size-11)
            c1 = SnakeTail not in snakes.values()
            c2 = SnakeTail not in snakes.keys()

            if c1 and c2:
                n = SnakeTail
                while str(n)[-1] != "0":
                    n += 1
                temp = (n+1) - SnakeTail

                SnakeHead = randint(SnakeTail+temp, self.size-1)
                con1 = SnakeHead not in snakes.keys()
                con2 = SnakeHead not in snakes.values()

                while not(con1 and con2):
                    SnakeHead = randint(SnakeTail+temp, self.size-1)
                    con1 = SnakeHead not in snakes.keys()
                    con2 = SnakeHead not in snakes.values()

                snakes[SnakeHead] = SnakeTail

        return snakes

    def generateLadders(self, Tladders):
        ladders = {}

        while len(ladders) < Tladders:
            ladderBottom = randint(2, self.size-11)
            c1 = ladderBottom not in ladders.keys()
            c2 = ladderBottom not in ladders.values()
            c3 = ladderBottom not in self.snakes.values()
            c4 = ladderBottom not in self.snakes.keys()

            if c1 and c2 and c3 and c4:
                n = ladderBottom
                while str(n)[-1] != "0":
                    n += 1
                temp = (n+1) - ladderBottom

                ladderTop = randint(ladderBottom+temp, self.size-1)
                con1 = ladderTop not in ladders.keys()
                con2 = ladderTop not in ladders.values()
                con3 = ladderTop not in self.snakes.keys()
                con4 = ladderTop not in self.snakes.values()

                while not(con1 and con2 and con3 and con4):
                    ladderTop = randint(ladderBottom+temp, self.size-1)
                    con1 = ladderTop not in ladders.keys()
                    con2 = ladderTop not in ladders.values()
                    con3 = ladderTop not in self.snakes.keys()
                    con4 = ladderTop not in self.snakes.values()

                ladders[ladderBottom] = ladderTop

        return ladders
