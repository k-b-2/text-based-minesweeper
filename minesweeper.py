import random


class Board():

    def __init__(self,x,y,mines):
        self.__x = x
        self.__y = y
        self.__mines = mines
        
        self.__board = BoardGenerator.RandomBoard(x,y,mines)
        self.__displayBoard = [["[ ]" for i in range(x)] for j in range(y)]

    def GetBoard(self):
        return self.__board
    
    def PrintBoard(self,board):

        print((" A  B  C  D  E  F  G  H  I  J "))
        #print("","-" * (len(board[0])*2+1) )

        for i in range(len(board)):
            
            for j in range(len(board[i])):
                print(str(board[i][j]) + "", end = '')
                
            print(" ",chr(65+i))

        
    def GenerateDisplayBoard(self, xGuess, yGuess, board, xLen, yLen, displayBoard):#for printing


        displayBoard[xGuess][yGuess] = " " + str(board[xGuess][yGuess]) + " "

        allDisplayed = False
        
        if board[xGuess][yGuess] == 0:

            displayBoard[xGuess][yGuess] = "   " #blank space for 0

            currentX = xGuess
            currentY = yGuess
            emptySquares = []
            checkedSquares = [(currentX,currentY)]
            
            while not allDisplayed: #when landing on an empty square, all adjacent squares must also be displayed
                
                for x in range(max(0,currentX-1),min(currentX+2,xLen)): # min/max ensures no index out of range error
                    for y in range(max(0,currentY-1),min(currentY+2,yLen)):
                        
                        if board[x][y] == 0: #if adjacent square is empty, all squares adjacent to it are also checked

                            if (x,y) not in checkedSquares and (x,y) not in emptySquares:
                                
                                emptySquares.append((x,y)) #ADDS to list to expand board so no empty values on border
                                displayBoard[x][y] = "   "
                            
                        elif board[x][y] != "X":
                            
                            displayBoard[x][y] = " " + str(board[x][y]) + " " #displays regular number value
                            
                if not emptySquares:
                    allDisplayed = True
                    break

                if len(emptySquares) == 1:
                    index = 0
                else:
                    index = random.randint(0,len(emptySquares)-1) #gets a random tuple from squares to be checked, could be made more efficient
                currentX, currentY = emptySquares[index]
                checkedSquares.append(emptySquares.pop(index))
                

        return displayBoard

             
            
        
    def SetDisplayBoard(self,value):
        self.__displayBoard = value

    def GetDisplayBoard(self):
        return self.__displayBoard
    
    def CheckGuess(self,xGuess,yGuess):
        
        if self.__board[xGuess][yGuess] == "X":
            self.PrintBoard(self.__board)
            GameController.GameOver(self.__board, False) #Game Over.
        else:
            dB = self.GenerateDisplayBoard(xGuess, yGuess, self.GetBoard(), self.__x, self.__y, self.GetDisplayBoard()) #generates the board to be displayed (this is different from the actual values in the game board)
            
            self.SetDisplayBoard(dB)
            
            self.PrintBoard(dB)
            
    def CheckWin(self):
        board = self.__board
        displayBoard = self.__displayBoard
        win = True
        
        for i in range(self.__x):
            for j in range(self.__y):
                disp = displayBoard[i][j]
                bd = str(board[i][j])
                if disp.strip() == bd:
                    continue
                elif disp == "   " and bd == '0':
                    continue
                elif disp == "[ ]" and bd == "X":
                    continue
                else:
                    win = False
        if win:
            GameController.GameOver(board,True)
                
        

#i suck at oop lol
class BoardGenerator():

    def RandomBoard(x,y,mines):
        
        board = [[0 for i in range(x)] for j in range(y)]
        minePositions = {} #MUST BE CHANGED - accidentally used dictionary here - doesn't store all mine positions, currently doesn't cause any problems but may do so in future.
        
        for i in range(mines):
            xpos = random.randint(0,x-1)
            ypos = random.randint(0,y-1)
            if xpos in minePositions and minePositions[xpos] == ypos:
                i -= 1
            else:
                minePositions[xpos] = ypos
                board[xpos][ypos] = "X"

        #loop for getting and writing to board num. of adjacent mines in each square
        for i in range(x):
            for j in range(y):
                
                if board[i][j] == "X":
                    continue
                else:
                    mineCount = 0
                    for k in range(max(0,i-1),min(i+2,x)): # min/max ensures no index out of range error
                        for l in range(max(0,j-1),min(j+2,y)):
                            
                            if board[k][l] == "X": #needs to be optimised so dont have to check itself maybe
                               mineCount+= 1
                               
                    board[i][j] = mineCount
        return board


class GameController():

    def GameOver(Board,win,):
        if win:
            print("You win!")
            
        else:
            print("You lose.")
        
        board.PrintBoard(Board)
        global game
        game = False
        input()

    def MakeGuess(guess):
        y = ord(guess[0])-65
        x = ord(guess[1])-65
        print(x,y)
        board.CheckGuess(x,y)
        board.CheckWin()
        

print("Syntax: Enter letters of the co-ordinatese of where you'd like to guess, column then row. E.g 'BG'")
x = 10
y = 10

#Gen = BoardGenerator()

#○■∙∙∙∙∙∙∙∙∙∙
board = Board(10,10,10)
game = True

board.PrintBoard(board.GetDisplayBoard())

while game:
    GameController.MakeGuess(input("Coordinate: ").upper())


