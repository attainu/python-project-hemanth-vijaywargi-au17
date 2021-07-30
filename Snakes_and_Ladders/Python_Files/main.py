import dice
import board
import art


def createBoard():
    Size = int(input("Size of the Board (20-100): "))
    if Size < 20:
        Size = 20
        print("Minimum Board Size is 20 ! Your Board Size has been set to 20.")

    Tsnakes = int(input("Number of Snakes (2-8): "))
    if Tsnakes < 2:
        Tsnakes = 2
        print("Minimum Number of Snakes is 2 ! Snakes have been set to 2")
    elif Tsnakes > 8:
        Tsnakes = 8
        print("Maximum Number of Snakes is 8 ! Snakes have been set to 8")

    Tladders = int(input("Number of Ladders (2-8): "))
    if Tladders < 2:
        Tsnakes = 2
        print("Minimum Number of Ladders is 2 ! Ladders have been set to 2")
    elif Tladders > 8:
        Tsnakes = 8
        print("Maximum Number of Ladders is 8 ! Ladders have been set to 8")

    Tplayers = int(input("Number of Players (Minimum 2): "))
    while Tplayers < 2:
        print("Minimum Number of Players is 2, Please Try Again ! ")
        Tplayers = int(input("Number of Players (Minimum 2): "))

    players = {}
    for i in range(1, Tplayers+1):
        players[input(f"Player {i} Name : ")] = 0

    return board.Board(Size, Tsnakes, Tladders, players)


def game():
    print(art.logo)
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
    i = input("Press Enter to Play Again or q to Quit: ")
    while i != "q":
        game()
