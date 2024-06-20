from Coin import *
class Connect4:

    def __init__(self):
         self.boardRows=4
         self.boardColumns=4
         self.boardCoinValues=[]

    def startGame(self):
            print("Welcome to Connect-4 Game")
            self.renderEmptyBoard()
            i=1
            while(True):
                 if i%2 != 0:
                      player="X"
                      print("Player-1 turn")
                 else:
                      player="O"
                      print("Player-2 turn")
                 while(True):
                      colValue=int(input("Enter the col value"))
                      if(colValue or colValue==0):
                           if(colValue<self.boardColumns):
                                break
                           else:
                                print(f"Column value should be less than {self.boardColumns}")
                      else:
                           print("Column value cannot be empty")
                 winPlayer=self.fillCoinOnBoard(colValue,player)
                 if(winPlayer):
                      print(f"{winPlayer} is the winner")
                      break
                 i+=1
                

    def renderEmptyBoard(self):
        value=" |"
        for label in range(self.boardColumns):
             value+=f"{label} |"
        print(value)
        for row in range(self.boardRows):
            boardColumValues=[]
            for col in range(self.boardColumns):
                myCoin=Coin(row,col,"-")
                boardColumValues.append(myCoin)
            value=f"{row}|"
            for val in boardColumValues:
                 value+=f"{val.get_state()} |"
            print(value)
            print("-------------")
            self.boardCoinValues.append(boardColumValues)

    def renderFilledBoard(self):
        value=" |"
        for label in range(self.boardColumns):
             value+=f"{label} |"
        print(value)
        for row in range(self.boardRows):
            boardColumValues=[]
            for col in range(self.boardColumns):
                myCoin=self.boardCoinValues[row][col]
                boardColumValues.append(myCoin)
            value=f"{row}|"
            for val in boardColumValues:
                 value+=f"{val.get_state()} |"
            print(value)
            print("-------------")
            self.boardCoinValues.append(boardColumValues)
    
    def fillCoinOnBoard(self,column,player):
         columnFillState=False
         for row in range(self.boardRows-1,-1,-1):
              if self.boardCoinValues[row][column].get_state()=="-":
                   columnFillState=True
                   if player=="X":
                        self.boardCoinValues[row][column].set_state("X")
                   elif player=="O":
                        self.boardCoinValues[row][column].set_state("O")
                   break

         if(not columnFillState):
              print("Column is full. You wasted your try.")          
         self.renderFilledBoard() 
         return self.determinePlayer()

    def determinePlayer(self):
         playerWon=""
         for row in range(self.boardRows):
              for col in range(self.boardColumns):
                   player = self.boardCoinValues[row][col]
                   #Horizontal check
                   if(col+3 <self.boardColumns):
                        if(self.boardCoinValues[row][col+1].get_state()==player and
                           self.boardCoinValues[row][col+2].get_state()==player and
                           self.boardCoinValues[row][col+3].get_state()==player):
                             playerWon=player
                             break
         return playerWon  
         

if __name__=="__main__":
     myGameObject=Connect4()
     myGameObject.startGame()
            

