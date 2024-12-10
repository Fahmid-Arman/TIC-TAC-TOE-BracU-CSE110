from IPython.display import clear_output
import time

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
current_player_char = 'X'
next_player_char = 'O'
totalInputs = 9
winner = None

def checkHorizontal():
    for i in board:
        if i[0] == i[1] == i[2]:
            return True
    return False

def checkVertical():
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            return True
    return False

def checkDiagonal():
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        return True
    return False

def checkBoard():
    if checkHorizontal() or checkVertical() or checkDiagonal():
        return True
    return False

def placeCharacterOnBoard(pos):
    r = (pos - 1) // 3
    c = (pos - 1) % 3
    if board[r][c] in range(1, 10):
        board[r][c] = current_player_char
        return 1
    else:
        print("Invalid position. Please input a valid one.")
        return 0

def printCurrentBoard():
    print("-------------")
    for eachRow in board:
        print("|", end="")
        for eachCol in eachRow:
            print(f" {eachCol} ", end="|")
        print()
        print("-------------")

def runGame():
    global current_player_char
    global next_player_char
    global winner
    print("Welcome to the TIC-TAC-TOE game. The first player to place a character on the board will be Player 1 (Character X) and the other player will be Player 2 (Character O).")
    inputCount = 0
    while inputCount < totalInputs:
        printCurrentBoard()
        position = int(input(f"Player {(inputCount % 2) + 1}, enter a position that does not contain any X or O:"))
        validityofInput = placeCharacterOnBoard(position)
        inputCount += validityofInput
        if inputCount >= 5:
            if checkBoard():
                winner = "Player 1" if current_player_char == 'X' else "Player 2"
                clear_output()
                break
        if validityofInput:
            current_player_char, next_player_char = next_player_char, current_player_char
        clear_output()
    printCurrentBoard()
    if winner != None:
        print(f"Well done, {winner}. You have won the game.")
    else:
        print(f"The game ended in a draw.")

runGame()
