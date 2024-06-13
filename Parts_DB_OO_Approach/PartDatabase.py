from Part import *

class PartDatabase:
    def __init__(self):
        self.partDatabase={}
        self.total_parts=0
    
    def addPart(self,part):
        self.partDatabase.append(part)
        
