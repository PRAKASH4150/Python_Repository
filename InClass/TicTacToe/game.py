from square import *

#tic-tac toe game class - user square class
class Game():

    #constructor
    def __init__(self):
        self.resetBoard()
    
    #play!
    def playGame(self):
        while(True):
            #get user input
            userInput=input("Enter row-col of move > ")
            #get index of square
            idx=self.getSquareIndex(userInput)
            #non neg index - valid move
            if(idx>=0):
                #same update
                self.board[idx].setState(self.Player)
                #is this the end of the game
                result=self.check4End()
                #print the result
                print(result)

                #end of the game accept continue
                if(result=="GAME OVER!\r\n" or result=="TIE!\r\n"):
                    self.renderBoard()
                    print(result+" Player "+self.PlayerNum+" Wins!")
                    if(input("Play Again (Y/N)? >").upper()=='Y'):
                        self.resetBoard()
                    else:
                        print("Exit!\r\n")
                        break
                
                #alternate player on each move
                elif(result=="PLAYING!\r\n"):
                    if(self.Player=='X'):
                        self.Player='O'
                        self.PlayerNum='2'
                    else:
                        self.Player='X'
                        self.PlayerNum='1'
                    #render the board
                    self.renderBoard()
                    print("Player "+self.PlayerNum+" is Up!\r\n")
                else:
                    print(result)
            #signal user invalid input!
            else:
                print("Invalid Input!\r\n You Entered: "+userInput)

    #reset the board for a new game
    def resetBoard(self):
        self.board=[]
        self.row_header="ABC"
        self.col_header="123"
        self.Player='X'
        self.PlayerNum='1'
        n=0
        for row in self.row_header: 
            for col in self.col_header:
                sq=Square()
                self.board.append(sq)
                self.board[n].setCol(col)
                self.board[n].setRow(row)
                self.board[n].setState('-')
                n+=1      
        print("Welcome to Tic-Tac-Toe!")
        print("Player 1 = X")
        print("Player 2 = O")
        self.renderBoard()
        print("Player 1 Up!")

    #method to check for the end of the game
    def check4End(self):
        ret="PLAYING!\r\n"

        #check for a full row of same pieces
        for j in range(0,3,7):
            if(self.board[j].getState()==self.board[j+1].getState() and self.board[j+1].getState()==self.board[j+2].getState() and self.Player==self.board[j+2].getState()):
                ret="GAME OVER!\r\n"
            break

        #check for a full col of same pieces
        for i in range(0,3):
            if(self.board[i].getState()==self.board[i+3].getState() and self.board[i+6].getState()==self.board[i].getState() and self.Player==self.board[i].getState()):
                ret="GAME OVER!\r\n"
                break

        #check diags
        if(self.board[0].getState()==self.Player and self.board[0].getState()==self.board[4].getState() and self.board[0].getState()==self.board[8].getState()):
            ret="GAME OVER!\r\n"
        elif(self.board[6].getState()==self.Player and self.board[6].getState()==self.board[4].getState() and self.board[6].getState()==self.board[2].getState()):
            ret="GAME OVER!\r\n"
        
        #check for a tie! - all squares are full
        if(ret=="PLAYING!\r\n"):
            ret="TIE!\r\n"
            for i in range(0,len(self.board)):
                if(self.board[i].getState()=='-'):
                    ret="PLAYING!\r\n"
                    break
                
        return ret

    #method to return the Square index and to check for a valid input
    def getSquareIndex(self,UserInput):
        ret=-1 #invalid input
        #is input in format row-col where row=A to C and col is 1 to 3?
        if(len(UserInput)>2):
            if(UserInput[1]=='-' and UserInput[0] in self.row_header and UserInput[2] in self.col_header):
                #get rol col
                row=UserInput[0]
                col=UserInput[2]
                #decode row to index
                if(row=='A'):
                    ret=0
                elif(row=='B'):
                    ret=3
                else:
                    ret=6
                #decode col to index
                ret+=(int(col)-1)

                #if populated then this is not a legal move!
                if(self.board[ret].getState()!="-"):
                    ret=-1

        return ret #-1 inidcates illegal move otherwise the index of the square is returned
    
    #method to render the board
    def renderBoard(self):
        #print col header
        print(" "+"|"+" "+self.col_header[0]+' '+self.col_header[1]+' '+self.col_header[2])
        print("______")
        n=0
        #populate each row
        for row in self.row_header:
            rowString=row+"|"
            for col in self.col_header:
                rowString+=" "+self.board[n].getState()
                n+=1
            print(rowString)

#instantiate object
o=Game()

#play the game!
o.playGame()