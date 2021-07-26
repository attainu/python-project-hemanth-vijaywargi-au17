from random import randint, sample
from os import system
from time import sleep


def rollDice():
    diceStates = [
        """
     ___________
    |           |
    |           |
    |     ⬤     |
    |           |
    |___________|
    """,
        """
     ___________
    |           |
    |  ⬤        |
    |           |
    |        ⬤  |
    |___________|
    """,
        """
     ___________
    |           |
    |  ⬤        |
    |     ⬤     |
    |        ⬤  |
    |___________|
    """,
        """
     ___________
    |           |
    |  ⬤    ⬤   |
    |           |
    |  ⬤    ⬤   |
    |___________|
    """,
        """
     ___________
    |           |
    |  ⬤     ⬤  |
    |     ⬤     |
    |  ⬤     ⬤  |
    |___________|
    """,
        """
     ___________
    |           |
    |  ⬤  ⬤  ⬤  |
    |           |
    |  ⬤  ⬤  ⬤  |
    |___________|
    """
    ]

    for i in range(6):
        print(diceStates[i])
        sleep(0.17)
        system("cls")
    val = randint(0, 5)

    print(diceStates[val])
    return val+1


def createBoard():
    snakes = {8: 4, 18: 1, 26: 10, 39: 5, 51: 6, 54: 36, 56: 1,
              60: 23, 75: 28, 83: 45, 85: 59, 90: 48, 92: 25, 97: 87, 99: 6}

    ladders = {3: 20, 6: 14, 11: 28, 15: 34, 17: 74, 22: 37,
               38: 59, 49: 67, 57: 76, 61: 78, 73: 86, 81: 98, 88: 91}

    # Creating Snakes
    Tsnakes = int(input("Number of Snakes : "))
    if Tsnakes < 3:
        Tsnakes = 3
        print("Minimum Number of snakes is 3")
    elif Tsnakes > 8:
        Tsnakes = 8
        print("Maximum Number of snakes is 8")
    Snakes = dict(sample(snakes.items(), Tsnakes))

    # Creating Ladders
    Tladders = int(input("Number of Ladders : "))
    if Tladders < 3:
        Tladders = 3
        print("Minimum Number of Ladders is 3")
    elif Tladders > 8:
        Tladders = 8
        print("Maximum Number of Ladders is 8")
    Ladders = dict(sample(ladders.items(), Tladders))

    # Creating Players
    Tplayers = int(input("Number of Players : "))
    Players = {}
    for i in range(1, Tplayers+1):
        Players[input(f"Player {i} Name : ")] = 0

    return Players, Snakes, Ladders


def game():
    Players, Snakes, Ladders = createBoard()
    while 100 not in Players.values():
        for player in Players:
            system("cls")
            for p in Players:
                print(f"{p}'s Position : {Players[p]} ")
            print()
            print(f"----- {player}'s Turn -----")
            input("Press any key to Roll Dice : ")

            diceVal = rollDice()
            newPos = Players[player]+diceVal
            if newPos <= 100:
                print(
                    f"{player} rolled a {diceVal} and moved from {Players[player]} to {newPos}")
                if newPos in Snakes:
                    print(
                        f"{player} got Bitten by a Snake at {newPos} ! {player} goes down to {Snakes[newPos]}.")
                    Players[player] = Snakes[newPos]
                elif newPos in Ladders:
                    print(
                        f"{player} found a Ladder at {newPos} ! {player} goes up to {Ladders[newPos]}.")
                    Players[player] = Ladders[newPos]
                else:
                    Players[player] = newPos
            else:
                print(f"Too many Steps ! Try again next Time {player}")

            if Players[player] == 100:
                print(
                    f"**************** {player} Wins the Game ! ****************")
                break
            else:
                input("Press any key to Continue : ")


if __name__ == "__main__":
    game()
    i = input("Press Enter to Play Again or e to Exit : ")
    while i != "e":
        game()
