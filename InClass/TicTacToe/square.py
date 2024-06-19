class Square():
    def __init__(self,row='',col='',state='-'):
        self.row=row
        self.col=col
        self.state=state
    def getRow(self):
        return self.row
    def getCol(self):
        return self.col
    def getState(self):
        return self.state
    def setRow(self,row=''):
        self.row=row
    def setCol(self,col=''):
        self.col=col
    def setState(self,state='-'):
        self.state=state
