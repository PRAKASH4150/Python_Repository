class Part:
    '''This class represents a Part entity'''
    def __init__(self,partName,manufacturerNumber,manufacturerdescription,cost,model):
        self.partName=partName
        self.manufacturerNumber=manufacturerNumber
        self.manufacturerdescription=manufacturerdescription
        self.cost=cost
        self.model=model
    
    def set_partName(self,partName):
        self.partName=partName
    def set_manufacturerNumber(self,manufacturerNumber):
        self.manufacturerNumber=manufacturerNumber
    def set_manufacturerDescription(self,manufacturerdescription):
        self.manufacturerdescription=manufacturerdescription
    def set_cost(self,cost):
        self.cost=cost
    def set_model(self,model):
        self.model=model

    def get_partName(self):
        return self.partName
    def get_manufacturerNumber(self):
        return self.manufacturerNumber
    def get_manufacturerDescription(self):
        return self.manufacturerdescription
    def get_cost(self):
        return self.cost
    def get_model(self):
        return self.model
