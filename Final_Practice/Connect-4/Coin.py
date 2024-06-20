class Coin:
    def __init__(self,row,column,state="-"):
        self.row=row
        self.column=column
        self.state=state

    def get_row(self):
        return self.row
    
    def get_column(self):
        return self.column
    
    def get_state(self):
        return self.state
    
    def set_row(self,row):
        self.row=row
    
    def set_column(self,column):
         self.column=column
    
    def set_state(self,state):
        self.state=state
