import dice
import board


def createBoard():
    Size = int(input("Size of the Board (20-100): "))
    if Size < 20:
        Size = 20
        print("Minimum Board Size is 20 ! Your Board Size has been set to 20.")
    Tsnakes = int(input("Number of Snakes (3-8): "))
    Tladders = int(input("Number of Ladders (3-8): "))
    Tplayers = int(input("Number of Players (2-4): "))
    players = {}
    for i in range(1, Tplayers+1):
        players[input(f"Player {i} Name : ")] = 0

    return board.Board(Size, Tsnakes, Tladders, players)


def game():
    board = createBoard()

    while True:
        for player in board.players:

            board.printPositions()

            print(f"----- {player}'s Turn -----")
            input("Press any key to Roll Dice : ")

            diceVal = dice.roll()
            board.updatePos(player, diceVal)

            if board.players[player] == board.size:
                print("*"*16, f"{player} Wins the Game !", "*"*16)
                return
            else:
                input("Press any key to Continue : ")


if __name__ == "__main__":
    game()
    i = input("Press Enter to Play Again or e to Exit : ")
    while i != "e":
        game()
