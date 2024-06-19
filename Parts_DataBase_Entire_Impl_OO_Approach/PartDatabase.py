#***************************************************************************************************
# Name:Sai Surya Prakash Moka
# ID: 00834035
#Description: This class manages all the CRUD operations on the parts database. It contains method
# to add the part, modify an existing part, fetch for a particular part, display the entire parts
# and to delete a part with the given serial number.
#***************************************************************************************************
from Part import * #Importing all the methods and members from Part class

#Class representing a Part Databse which includes all the methods to perform the CRUD operations on
#the DB.
class PartDatabase:
    
    totalParts=0 #Class variable to store the total parts

    def __init__(self):

        #This dictionary will contain all the details about the entire parts.
        # The key will be the Serial Number of the Part and the value will
        # be the part object itself
        self.partsInventory={}
    
    def addPartToDB(self,part):
        '''
          Description: Method to add the part to the Database
          Parameters:
           Self
           part - Takes the part object as an argument
        '''
        #Checking whether any part with the same serial number exists in the db
        if part.getPartSerialNum() in self.partsInventory.keys():
            print(f"Part with the same Serial Number : {part.getPartSerialNum()} "
                  " already exists in the DB.")
        else:
            #If the part doesnot exists we add to the inventory
            self.partsInventory[part.getPartSerialNum()]=part
            PartDatabase.totalParts+=1

    def searchPartBySerialNum(self,partSerialNum):
        '''
         Description: Method to search for a part with a particular serial number.
         Prints and returns  the part details if found.
          self
          partSerialNum - Takes the Part Serial Number as an argument
        '''
        #Checking whether the given serial number exists in the db
        if partSerialNum in self.partsInventory.keys():
            self.partsInventory[partSerialNum].displayPart()
            return self.partsInventory[partSerialNum] #Returning the part object.
        else:
            print(f"Part not found with the given Serial Number : {partSerialNum}")
        

    
    def displayAllParts(self):
        '''
         Description: Method to display all the Parts in the Database
         Parameters:
          self
        '''
        #iterating over the entire db to display the parts
        for index,(key) in enumerate(self.partsInventory.keys()):
            print(f"Part {index+1} - {key}")
            self.partsInventory[key].displayPart()

    def modifyPart(self,part):
        '''
         Description: Method to modify an exisiting part in the Database
         Parameters:
          self
          part: Modified part object
        '''
        if part.getPartSerialNum() in self.partsInventory.keys():
            self.partsInventory[part.getPartSerialNum()]=part #Modifying the exisiting part with new part
            print("Record Modified Sucessfully")
        else:
            print(f"Part with the Serial Number {part.getPartSerialNum()} doesnot exist")    
    
    def deltePart(self,partSerialNum):
        '''
         Description: This method is used to delte a Part for a given serial number if found
         Parameters: 
          self
          partSerialNum: Serial number of the part
        '''
        #Checking whether the enetered serial number exists in the dictionary
        if partSerialNum in self.partsInventory.keys(): 
            del(self.partsInventory[partSerialNum]) #Deleting the Part
            print(f"Part with the Serial Number {partSerialNum} delted sucessfully.")
        else:
            print("Part with the given serial number not found to delete")    
