import random

class Board():

    def __init__(self,x,y,mines):
        self.__x = x
        self.__y = y
        self.__mines = mines
        
        self.__board = BoardGenerator.randomBoard(self,x,y,mines)
        self.__displayBoard = [["[ ]" for i in range(x)] for j in range(y)]
    
    def printBoard(self):
        board = self.__displayBoard
        print(("  A  B  C  D  E  F  G  H  I  J "))
        #print("","-" * (len(board[0])*2+1) )

        for i in range(len(board)):
    
            #print("|", end = '')
            print(u"\u202F", end = '')
            for j in range(len(board[i])):
                print(str(board[i][j]) + "", end = '')
        
            #print("|")
            print(" ",chr(65+i))
        #print("","-" * (len(board[0])*2+1) )
        

    def generateDisplayBoard(board):
        print("") 
        

#i suck at oop lol
class BoardGenerator():

    def randomBoard(self,x,y,mines):
        
        board = [[0 for i in range(x)] for j in range(y)]
        minePositions = {}
        
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
        

print("Syntax: Enter letters of the co-ordinatese of where you'd like to guess, column then row. E.g 'BG'")
x = 10
y = 10

Gen = BoardGenerator()
board = Gen.randomBoard(10,10,12)
#○■∙∙∙∙∙∙∙∙∙∙
board = Board(10,10,12)

board.printBoard()
guess = input("Co-ords")


