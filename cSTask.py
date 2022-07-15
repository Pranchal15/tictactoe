"""
Dear rEtiReD sENiOrS ,
This is a tic-tac-toe game which I implemented in Python. 
I don't really like this task because it is boring. 
rEpLiCatE a login page or bUilD a game!
However, I finished this and I hope you like it.
Will you give me brownie points if I say that I finished this in less than 60 mins?
If yes, thankyou! *heart eyes*
If no, whatever! *eyeroll*
bye bye
love, 
Me!
"""
#global vars
global gameOn
gameOn = True
# create board or reset board or clear board
def createBoard():
    global board
    board = ['-','-','-','-','-','-','-','-','-']
    global currentToken
    currentToken = 'X'
    global currentPlayer
    currentPlayer = '1'


#change Token 
def changeToken():
    global currentToken
    if currentToken == 'X':
        currentToken = 'O'
    elif currentToken == 'O':
        currentToken = 'X'

# change Player 
def changePlayer():
    global currentPlayer
    if currentPlayer == '1':
        currentPlayer = '2'
    elif currentPlayer =='2':
        currentPlayer = '1'

#displaying board
def displayBoard():
    for i in range(0,9,3):
        print(board[i]+'|'+board[i+1]+'|'+board[i+2])

#checking if there is a winner
def checkWin():
    #first checking rows 
    for j in range(0,9,3):
        if board[j]==board[j+1]==board[j+2]!='-' :
            return True
    #now checking columns
    for k in range(0,3,1):
        if board[k]==board[k+3]==board[k+6]!='-':
            return True
    #checking diagonals
    
    if board[0]==board[4]==board[8]!='-':
            return True 
    elif board [2]==board[4]==board[6]!='-':
            return True
    return False

def checkDraw():
    for j in range(0,9):
        
        if board[j]=='-':
            return False
    return True
    
#play game 
def playGame():
    global gameOn
    gameOn = False
    displayBoard()
    newGame = 'y'
    print("It's "+currentToken+"'s"+" turn.")
    position = input("Enter a position from 1 to 9 :")
    #using try and except to see if the user entered a number or not
    try :
        position = int(position)-1
    except ValueError :
        print("Invalid input!")
    if isinstance(position,int) and position >= 0 and position <=8:
        #check is that position is empty or not
        if board[position] == '-':
            board[position] = currentToken
            #check if the currentPlayer won
            if checkWin():
                displayBoard()
                print("Player "+currentPlayer+" wins!")
                createBoard()
                newGame = input("Do you want to play again? (Y/N): ")
                if newGame =='Y' or newGame == 'y' :
                    gameOn = True
                    return gameOn
                if newGame == 'N' or newGame == 'n':
                    gameOn = False 
                    return gameOn
            #check for draw
            elif checkDraw():
                displayBoard()
                print("It's a draw")
                createBoard()
                newGame = input("Do you want to play again? (Y/N): ")
                if newGame =='Y' or newGame == 'y' :
                    gameOn = True
                    return gameOn
                if newGame == 'N' or newGame == 'n':
                    gameOn = False 
                    return gameOn
                else :
                    return False
            # if it isn't win or draw, then flip player and token and then continue
            changePlayer()
            changeToken()
            gameOn = True
        #if the position is not empty
        else :
            print("Position already filled, choose another number")
            playGame()
            gameOn = True
    # if position is out of bounds i.e. position < 0 or position >8
    else :
        print("Entered position is not valid")
        playGame()
        gameOn=True
    return gameOn

#main
createBoard()
while gameOn :
    playGame()