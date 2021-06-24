import random


class Board():

    def __init__(self,x,y,mines):
        self.__x = x
        self.__y = y
        self.__mines = mines
        
        self.__board = BoardGenerator.RandomBoard(x,y,mines)
        self.__displayBoard = [["[ ]" for i in range(x)] for j in range(y)]
    
    def PrintBoard(self,board):

        print((" A  B  C  D  E  F  G  H  I  J "))
        #print("","-" * (len(board[0])*2+1) )

        for i in range(len(board)):
    
            #print("|", end = '')
            #print(u"\u202F", end = '')
            for j in range(len(board[i])):
                print(str(board[i][j]) + "", end = '')
        
            #print("|")
            print(" ",chr(65+i))
        #print("","-" * (len(board[0])*2+1) )
        
    def GenerateDisplayBoard(self, xGuess, yGuess, board, xLen, yLen, displayBoard):


        displayBoard[xGuess][yGuess] = " " + str(board[xGuess][yGuess]) + " "

        allDisplayed = False
        
        if board[xGuess][yGuess] == 0:

            displayBoard[xGuess][yGuess] = "   "

            currentX = xGuess
            currentY = yGuess
            emptySquares = []
            checkedSquares = [(currentX,currentY)]
            while not allDisplayed:
                
                for x in range(max(0,currentX-1),min(currentX+2,xLen)): # min/max ensures no index out of range error
                    for y in range(max(0,currentY-1),min(currentY+2,yLen)):
                        
                        if board[x][y] == 0:

                            if (x,y) not in checkedSquares and (x,y) not in emptySquares:
                                
                                emptySquares.append((x,y)) #ADDS to list to expand board so no empty values on border
                                displayBoard[x][y] = "   "
                            
                        elif board[x][y] != "X":
                            
                            displayBoard[x][y] = " " + str(board[x][y]) + " "
                            
                if not emptySquares:
                    allDisplayed = True
                    break

                if len(emptySquares) == 1:
                    index = 0
                else:
                    index = random.randint(0,len(emptySquares)-1)
                currentX, currentY = emptySquares[index]
                checkedSquares.append(emptySquares.pop(index))
                

        return displayBoard

             
            
        
    def GetDisplayBoard(self):
        return self.__displayBoard
    
    def CheckGuess(self,xGuess,yGuess):
        
        if self.__board[xGuess][yGuess] == "X":
            GameController.GameOver(self.__board)
        else:
            boardToPrint = self.GenerateDisplayBoard(xGuess, yGuess, self.__board, self.__x, self.__y, self.__displayBoard)
            self.PrintBoard(boardToPrint)
            


#i suck at oop lol
class BoardGenerator():

    def RandomBoard(x,y,mines):
        
        board = [[0 for i in range(x)] for j in range(y)]
        minePositions = {}#NEEDS TO BE CHANGED. DICTIONARY NEEDS UNIQUE KEYS - ONLY ALLOWS ONE MINE PER X VALUE!!!!!!!!
        
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

    def GameOver(board):
        print("You lose.")

    def MakeGuess(guess):
        x = ord(guess[0])-65
        y = ord(guess[1])-65
        print(x,y)
        board.CheckGuess(x,y)
        

print("Syntax: Enter letters of the co-ordinatese of where you'd like to guess, column then row. E.g 'BG'")
x = 10
y = 10

#Gen = BoardGenerator()
board = BoardGenerator.RandomBoard(10,10,12)
#○■∙∙∙∙∙∙∙∙∙∙
board = Board(10,10,12)


GameController.MakeGuess(input("Coordinate: "))


