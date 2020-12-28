import random
import time

def drawBoard(board):

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # if random.randint(0, 1) == 0:
    #     return 'computer'
    # else:
    #     return 'player'

    return 'computer'

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getBoardCopy(board):
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)


    return dupeBoard
def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
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

def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

def rule():
    print('It seems you have some Trouble while play game, now worry i will help you.')
    print('In Tic-Tac-Toe you have to make a straight line out of 3-O or 3-X')
    print('For example:')
    print(" X | O | X \n ---------- \n X | X | O \n ----------\n X | O | O \n")

def play_with_human():
    global u_name, u2_name, theBoard
    game_on = True
    print('Hello, I am A.I. robot and i am your umpire today.')
    u_name = input('What should i call you player 1(X)? ')
    u2_name = input('What should i call you player 2(O)? ')
    print("let's see who wins today.")
    print("let's start with the game now", u_name.upper(), 'vs', u2_name.upper(), '\n\n')
    print("Type 'Rule' to see Rules.")
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
                    print(f'Hooray! {u_name} have won the game!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
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
                    print(f'Hooray! {u2_name} have won the game!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = u_name

        if not playAgain():
            break

print('Welcome to Tic Tac Toe!')
time.sleep(0.5)
print('Start the game be typing * start or game * or\n')
print('type * -h or help * to see how to play this Game...\n')
time.sleep(0.5)
while True:
    input_1 = input('>Tic-Tac-Toe> ').lower()
    if input_1 == '-h' or input_1 == 'help' or input_1 == 'options':
        print('Welcome to Help box:)')
        print('Here are all options and everything you can do with this Game.\n')
        print('-----------------------------------------------------------------------')
        print('| Options                 | Use                                       |')
        print('-----------------------------------------------------------------------')
        print('| -h or help              | To see all available options for the game.|')
        print('''| about                   | To see information about the developer of |
|                         | this Game                                 |''')
        print('| start or play           | To start a new game.                      |')
        print('| rule                    | To Know rules of the game.                |')
        print('| clear                   | To Clear the Terminal Screen.             |')
        print('| exit or quit            | To Quit/Exit the game.                    |')
        print('-----------------------------------------------------------------------\n')
    elif input_1 == 'about':
        print('Hello,')
        print('      I an Tic-Tac-Toe game which is created by Imran')
        print('Check out my Insta: @unknown.domination')
    elif input_1 == 'exit' or input_1 == 'quit':
        exit()
    elif input_1 == 'clear':
        print(chr(27) + "[2J")
    elif input_1 == 'start' or input_1 == 'play' or input_1 == 'game' or input_1 == 'run':
        duo_ai = input('Would you link to play with your friend or bot(f/b): ')
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
                            print('Hooray! You have won the game!')
                            gameIsPlaying = False
                        else:
                            if isBoardFull(theBoard):
                                drawBoard(theBoard)
                                print('The game is a tie!')
                                break
                            else:
                                turn = 'computer'

                    else:
                        # Computer's turn.
                        move = getComputerMove(theBoard, computerLetter)
                        makeMove(theBoard, computerLetter, move)

                        if isWinner(theBoard, computerLetter):
                            drawBoard(theBoard)
                            print('The computer has beaten you! You lose.')
                            gameIsPlaying = False
                        else:
                            if isBoardFull(theBoard):
                                drawBoard(theBoard)
                                print('The game is a tie!')
                                break
                            else:
                                turn = 'player'

                if not playAgain():
                    break
    elif input_1 == 'rule' or input_1 == 'rules':
        rule()
    else:
        print("It's seems some error occurred, please check your spellings.")