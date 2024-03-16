from termcolor import colored
from random import randrange
from time import sleep
from os import system, name as osName

board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

winningPositions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]

gameRunning = True


def main():
    currentPlayer = 1
    while gameRunning:
        showBoard(board)
        updateBoard(getPlayerMove(board, currentPlayer), currentPlayer, board)
        checkForWin(board, winningPositions, currentPlayer)
        currentPlayer = changeCurrentPlayer(currentPlayer)

    showBoard(board)


def showBoard(board):
    sleep(1)
    clearScreen()
    for i in range(0, len(board)):
        if board[i] == 1:
            print(f"| {colored('X', 'light_blue')} ", end="")
        elif board[i] == 2:
            print(f"| {colored('O', 'green')} ", end="")
        else:
            print(f"| {i + 1} ", end="")

        if (i + 1) % 3 == 0:
            print("|")


def changeCurrentPlayer(currentPlayer):
    if currentPlayer == 1:
        return 2
    else:
        return 1


def getPlayerMove(board, currentPlayer):
    print(f"Player {currentPlayer}'s turn")

    move = 0
    while not isValidPlayerMove(move, board):
        if currentPlayer == 1:
            move = input("Input a number between [1 and 9] ")
        else:
            move = randrange(1, 10)  # Get AI move

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


def checkForWin(board, winningPositions, currentPlayer):
    global gameRunning

    for positions in winningPositions:
        if (
            board[positions[0]] == currentPlayer
            and board[positions[1]] == currentPlayer
            and board[positions[2]] == currentPlayer
        ):
            print(f"Player {currentPlayer} wins!")
            gameRunning = False
            return


def toBoardIndex(number):
    return number - 1


def clearScreen():
    system("cls" if osName == "nt" else "clear")


main()
