""""""""""""""""""""""""""""""""" TicTacToe Game """""""""""""""""""""""""""""""""""""""
# Installing Modules
import random
import time
import colorama
from colorama import Fore
colorama.init(autoreset=True)

def drawBoard(board):
    # Board Design
    print("\n" + board[1] + " | " + board[2] + " | " + board[3] + "     1 | 2 | 3")
    print("--|---|--")
    print(board[4] + " | " + board[5] + " | " + board[6] + "     4 | 5 | 6")
    print("--|---|--")
    print(board[7] + " | " + board[8] + " | " + board[9] + "     7 | 8 | 9" + "\n")

def inputPlayerLetter():                        # Selecting the symbol to use in the game by the user
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print(Fore.BLUE + 'Do you want to by X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
0
def whoGoesFirst():
    # if random.randint(0, 1) == 0:             # Toss to select who plays first
    #     return 'computer'
    # else:
    #     return 'player'

    return 'computer'

def playAgain():                                # To ask user to play the game again
    print(Fore.GREEN + 'Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):              # Important Func = To enter the symbol in the position on board
    board[move] = letter

def isWinner(bo, le):                           # To see whether the user\computer have won the game or not
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getBoardCopy(board):                        # To show the board again and again on the terminal
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):                   # Check whether the space where user\computer chose is available
    return board[move] == ' '

def getPlayerMove(board):                       # To get the move from the player
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print(Fore.CYAN + 'What is your next move? (1-9)')
        move = input()

    return int(move)

def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Check if the player could win on his next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):                         # Check whether the board is full or not
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

def rule():
    print(Fore.GREEN  + 'It seems you have some Trouble while play game, no worry i will help you.')
    print(Fore.GREEN + 'In Tic-Tac-Toe you have to make a straight line out of 3-O or 3-X')
    print(Fore.GREEN + 'For example:')
    print(Fore.GREEN + " X | O | X \n ---------- \n X | X | O \n ----------\n X | O | O \n")

def play_tournament():
    duo_ai = input(Fore.BLUE + 'Would you link to play tournament with your friend or bot(f/b): ')
    if duo_ai == 'friend' or duo_ai == 'f' or duo_ai == 'my friend' or duo_ai == 'duo' or duo_ai == 'human':
        i = 1
        p = 0
        c = 0
        print(Fore.GREEN + 'Hello, I am A.I. robot and i am your umpire today.')
        u_name = input(Fore.GREEN + 'What should i call you player 1(X)? ')
        u2_name = input(Fore.GREEN + 'What should i call you player 2(O)? ')
        print(Fore.GREEN + "Let's see who wins today.")
        print(Fore.GREEN + "Let's start with the game now", u_name.upper(), 'VS', u2_name.upper(), '\n\n')
        while i <= 3:
            gameIsPlaying = True
            # Reset the board
            theBoard = [' '] * 10
            playerLetter, computerLetter = ['X', 'O']
            
            if random.randint(0, 1) == 0:
                turn = u_name
            else:
                turn =  u2_name
            print('The ' + turn + ' will go first.')
            

            while gameIsPlaying:
                if i > 3 : gameIsPlaying = False
                if turn == u_name:
                    # Player's turn.
                    drawBoard(theBoard)
                    print(u_name)
                    move = getPlayerMove(theBoard)
                    makeMove(theBoard, playerLetter, move)

                    if isWinner(theBoard, playerLetter):
                        drawBoard(theBoard)
                        print(f'Hurray! {u_name} have won the game!')
                        p += 1
                        gameIsPlaying = False
                    else:
                        if isBoardFull(theBoard):
                            drawBoard(theBoard)
                            print('Oh! the game is a tie!\nTry hard for next time')
                            break
                        else:
                            turn = u2_name

                else:
                    # Player's turn.
                    drawBoard(theBoard)
                    print(u2_name)
                    move = getPlayerMove(theBoard)
                    makeMove(theBoard, computerLetter, move)

                    if isWinner(theBoard, computerLetter):
                        drawBoard(theBoard)
                        print(f'Hurray! {u2_name} have won the game!')
                        c += 1
                        gameIsPlaying = False
                    else:
                        if isBoardFull(theBoard):
                            drawBoard(theBoard)
                            print('The game is a tie!\nTry hard for next time')
                            break
                        else:
                            turn = u_name

            i += 1

        if p > c: print("Congrats!!! "+u_name + " has won the tournament\n")
        elif p == c: print("The tournament is a tie\n")
        else: print("Congrats!!! "+u2_name + " has won the tournament\n")
    elif duo_ai == 'computer' or duo_ai == 'bot' or duo_ai == 'ai' or duo_ai == 'single' or duo_ai == 'b':
        i = 1
        p = 0
        c = 0
        while i <= 3:
            gameIsPlaying = True
            # Reset the board
            theBoard = [' '] * 10
            playerLetter, computerLetter = inputPlayerLetter()
            turn = whoGoesFirst()
            print('The ' + turn + ' will go first.')
            while gameIsPlaying:
                if i > 3 : gameIsPlaying = False
                if turn == 'player':
                    # Player's turn.
                    drawBoard(theBoard)
                    move = getPlayerMove(theBoard)
                    makeMove(theBoard, playerLetter, move)
                    if isWinner(theBoard, playerLetter):
                        drawBoard(theBoard)
                        print(Fore.GREEN + 'Hurray! You have won the game!')
                        p += 1
                        gameIsPlaying = False
                    else:
                        if isBoardFull(theBoard):
                            drawBoard(theBoard)
                            print(Fore.RED + 'The game is a tie!\nTry hard for next time')
                            break
                        else:
                            turn = 'computer'
                else:
                    # Computer's turn.
                    move = getComputerMove(theBoard, computerLetter)
                    makeMove(theBoard, computerLetter, move)
                    if isWinner(theBoard, computerLetter):
                        drawBoard(theBoard)
                        print(Fore.RED +  'The computer has beaten you!\nYou lose.')
                        c += 1
                        gameIsPlaying = False
                    else:
                        if isBoardFull(theBoard):
                            drawBoard(theBoard)
                            print(Fore.GREEN + 'The game is a tie!\nTry hard for next time')
                            break
                        else:
                            turn = 'player'
            i += 1
        if p > c: print("Player has won the tournament")
        elif p == c: print("The tournament is a tie\n")
        else: print("Computer has won the tournament")

def play_with_human():
    global u_name, u2_name, theBoard
    game_on = True
    print(Fore.GREEN + 'Hello, I am A.I. robot and i am your umpire today.')
    u_name = input(Fore.GREEN + 'What should i call you player 1(X)? ')
    u2_name = input(Fore.GREEN + 'What should i call you player 2(O)? ')
    print(Fore.GREEN + "Let's see who wins today.")
    print(Fore.GREEN + "Let's start with the game now", u_name.upper(), 'VS', u2_name.upper(), '\n\n')
    print(Fore.GREEN + "Type 'Rule' to see Rules.")
    while True:
        # Reset the board
        theBoard = [' '] * 10
        playerLetter, computerLetter = ['X', 'O']
        if random.randint(0, 1) == 0:
            turn = u_name
        else:
            turn =  u2_name
        print('The ' + turn + ' will go first.')
        gameIsPlaying = True
        while gameIsPlaying:
            if turn == u_name:
                # Player's turn.
                drawBoard(theBoard)
                print(u_name)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)
                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print(f'Hurray! {u_name} have won the game!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!\nTry hard for next time')
                        break
                    else:
                        turn = u2_name
            else:
                # Player's turn.
                drawBoard(theBoard)
                print(u2_name)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, computerLetter, move)

                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print(f'Hurray! {u2_name} have won the game!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!\nTry hard for next time')
                        break
                    else:
                        turn = u_name
        if not playAgain():
            break

print(Fore.YELLOW + 'Welcome to Tic Tac Toe !!!')
time.sleep(0.5)
print(Fore.MAGENTA + 'Start the game be typing * start or game * or play tournament * tour *\n')
print(Fore.MAGENTA + 'Type * -h or help * to see how to play this Game...\n')
time.sleep(0.5)
while True:
    input_1 = input('>Tic-Tac-Toe> ').lower()
    if input_1 == '-h' or input_1 == 'help' or input_1 == 'options':
        print(Fore.GREEN + 'Welcome to Help box:)')
        print(Fore.GREEN + 'Here are all options and everything you can do with this Game.\n')
        print('-----------------------------------------------------------------------')
        print('| Options                 | Use                                       |')
        print('-----------------------------------------------------------------------')
        print('| -h or help              | To see all available options for the game.|')
        print('''| about                   | To see information about the developer of |
|                         | this Game                                 |''')
        print('| tour                    | To play the tournament.                   |')
        print('| start or play           | To start a new game.                      |')
        print('| rule                    | To Know rules of the game.                |')
        print('| clear                   | To Clear the Terminal Screen.             |')
        print('| exit or quit            | To Quit/Exit the game.                    |')
        print('-----------------------------------------------------------------------\n')
    elif input_1 == 'about':
        print('Hello,')
        print('      This Tic-Tac-Toe game is created by Humayun Bajwa\nA newbie student of Comsats University Islamabad')
    elif input_1 == 'exit' or input_1 == 'quit':
        exit()
    elif input_1 == 'clear':
        print(chr(27) + "[2J")
    elif input_1 == 'tour':
        play_tournament()
    elif input_1 == 'start' or input_1 == 'play' or input_1 == 'game' or input_1 == 'run':
        duo_ai = input(Fore.BLUE + 'Would you link to play with your friend or dare to challenge our bot(f/b): ')
        if duo_ai == 'friend' or duo_ai == 'f' or duo_ai == 'my friend' or duo_ai == 'duo' or duo_ai == 'human':
            play_with_human()
        elif duo_ai == 'computer' or duo_ai == 'bot' or duo_ai == 'ai' or duo_ai == 'single' or duo_ai == 'b':
            while True:
                # Reset the board
                theBoard = [' '] * 10
                playerLetter, computerLetter = inputPlayerLetter()
                turn = whoGoesFirst()
                print('The ' + turn + ' will go first.')
                gameIsPlaying = True
                while gameIsPlaying:
                    if turn == 'player':
                        # Player's turn.
                        drawBoard(theBoard)
                        move = getPlayerMove(theBoard)
                        makeMove(theBoard, playerLetter, move)

                        if isWinner(theBoard, playerLetter):
                            drawBoard(theBoard)
                            print(Fore.GREEN + 'Hurray! You have won the game!')
                            gameIsPlaying = False
                        else:
                            if isBoardFull(theBoard):
                                drawBoard(theBoard)
                                print(Fore.RED + 'The game is a tie!\nTry hard for next time')
                                break
                            else:
                                turn = 'computer'
                    else:
                        # Computer's turn.
                        move = getComputerMove(theBoard, computerLetter)
                        makeMove(theBoard, computerLetter, move)

                        if isWinner(theBoard, computerLetter):
                            drawBoard(theBoard)
                            print(Fore.RED +  'The computer has beaten you! \n You lose.')
                            gameIsPlaying = False
                        else:
                            if isBoardFull(theBoard):
                                drawBoard(theBoard)
                                print(Fore.GREEN + 'The game is a tie!\nTry hard for next time')
                                break
                            else:
                                turn = 'player'
                if not playAgain():
                    break
    elif input_1 == 'rule' or input_1 == 'rules':
        rule()
    else:
        print(Fore.RED + "It's seems some error occurred, Please check your input.")