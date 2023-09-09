board = [
    0, 0, 0,
    0, 0, 0,
    0, 0, 0
]

gameRunning = True


def main():
    while gameRunning:
        currentPlayer = 1
        showBoard(board)
        updateBoard(getPlayerMove(board), currentPlayer, board)
        currentPlayer = changeCurrentPlayer(currentPlayer)


def showBoard(board):
    for i in range(0, len(board)):
        print(f"| {board[i]} ", end="")

        if ((i + 1) % 3 == 0):
            print("|")


def changeCurrentPlayer(currentPlayer):
    if (currentPlayer == 1):
        return 2
    else:
        return 1


def getPlayerMove(board):
    move = 0
    while not isValidPlayerMove(move, board):
        move = input("Input a number between [1 and 9]")

    return int(move)


def isValidPlayerMove(move, board):
    newMove = None

    try:
        newMove = int(move)
    except ValueError:
        return False

    if newMove < 1 or newMove > 9:
        return False

    if board[toBoardIndex(newMove)] == 1 or board[toBoardIndex(newMove)] == 2:
        return False

    return True


def updateBoard(moveIndex, currentPlayer, board):
    board[toBoardIndex(moveIndex)] = currentPlayer


def toBoardIndex(number):
    return number - 1


main()
