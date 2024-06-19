#***************************************************************************************************
# Name:Sai Surya Prakash Moka
# ID: 00834035
#Description: This class is the base class which represents the Part which contains a set of
# attributes. This class is used to initialize a Part and set values to it.
#***************************************************************************************************
class Part: # A class representing a part

    #Class Variable Attribute list which represents a part with all the required details
    attribList=['compPartNum','partSerialNum','manufacturer',
                'description','weight','partCondition','cost',
                'warrantyPeriod','hazardousMaterial','partsonHand','partsNeeded','leadTime']
    #Note: Part Serial Number will be a unique attribute
    
    #Creating a constructor to instantiate the instance variables of the Part class
    def __init__(self,partDetails):
        '''
          Description: Constructor to initialize the values present in the partDetails 
          dictionary as a instance variables
          Parameters:
           self: self object
           partDetails: Dictionary representing the attribName:attribValue Eg: compPartNum:Ivy12345
        '''
        #iterating over the dictionary to set the values to the self object using setattr method
        for key,value in partDetails.items():
            setattr(self,key,value)
       

    #Creating getters to retrieve the instance variables
    #Note: Setting the instance variables only happens with the use of constructor

    def getCompPartNum(self):
         return self.compPartNum
    def getPartSerialNum(self):
        return self.partSerialNum
    def getManufacturer(self):
        return self.manufacturer
    def getDescription(self):
        return self.description
    def getWeight(self):
        return self.weight
    def getPartCondition(self):
        return self.partCondition
    def getCost(self):
        return self.cost
    def getPartsonHand(self):
        return self.partsonHand
    def getWarrantyPeriod(self):
        return self.warrantyPeriod
    def getHazardousMaterial(self):
        return self.hazardousMaterial
    def getPartsNeeded(self):
        return self.partsNeeded
    def getLeadTime(self):
        return self.leadTime
    
    #Method to display the part details as a formatted output
    def displayPart(self):
        print("***********PART DETAILS************")
        print(f"{Part.attribList[0]} : {self.getCompPartNum()}")
        print(f"{Part.attribList[1]} : {self.getPartSerialNum()}")
        print(f"{Part.attribList[2]} : {self.getManufacturer()}")
        print(f"{Part.attribList[3]} : {self.getDescription()}")
        print(f"{Part.attribList[4]} : {self.getWeight()}")
        print(f"{Part.attribList[5]} : {self.getPartCondition()}")
        print(f"{Part.attribList[6]} : {self.getCost()}")
        print(f"{Part.attribList[7]} : {self.getWarrantyPeriod()}")
        print(f"{Part.attribList[8]} : {self.getHazardousMaterial()}")
        print(f"{Part.attribList[9]} : {self.getPartsonHand()}")
        print(f"{Part.attribList[10]} : {self.getPartsNeeded()}")
        print(f"{Part.attribList[11]} : {self.getLeadTime()}")
        print("***********************************")