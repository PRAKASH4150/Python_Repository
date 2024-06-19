from Part import *

class PartDatabase:
    
    def __init__(self):
        self.partDatabase={}
        self.total_parts=0
    
    def addPart(self,part):
        self.partDatabase.append(part)
        self.total_parts+=1

    #Method to delete a part form the DB    
    def deltePart(self,partNum):
        del(self.partDatabase[partNum])
    
    #Method to find a part with a given key
    def findPart(self,key):
        for keyVal,value in self.partDatabase.items():
            if keyVal==key:
                return self.partDatabase[keyVal]
    
    def updateManufacturerNumber(self,manufacturerNumber,partNumber):
        if self.partDatabase.get(partNumber):
            
        else:
            print("Part with the given number doesnot exist")