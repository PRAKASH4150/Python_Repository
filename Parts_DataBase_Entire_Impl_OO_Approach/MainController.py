#***************************************************************************************************
# Name:Sai Surya Prakash Moka
# ID: 00834035
#Description: This class acts as the controller which orcestrates the calls to PartDatabase depending
# on  the option the user selects from the menu. This class also handles the user validations
# before triggering the PartDatabase class calls.
#***************************************************************************************************
from Part import * #Importing all the methods and members from Part class
from PartDatabase import * #Importing all the methods and members from PartDatabase class

# creating a class which acts as an orchestrator in managing the  Part and PartDatabse modules
class MainController:

    def __init__(self):
        self.partDBObj=PartDatabase()

    def renderMenu(self):
        '''
         Description: Method which renders the menu to perform the CRUD operation
        '''
        #Rendering the menu options to the user.
        while(True):
            userChoice=input("\nEnter 1 to add a Part to the DB."
                  "\nEnter 2 to Search for a Part using Serial Number"
                  "\nEnter 3 to Display all the parts."
                  "\nEnter 4 to Modify a Part"
                  "\nEnter 5 to Delete a Part"
                  "\nEnter Q or q to quit."
                  "\nEnter your choice:")
            
            if(userChoice=="1"):
               self.addPart()
            elif(userChoice=="2"):
               self.searchBySerialNum()
            elif(userChoice=="3"):
               self.partDBObj.displayAllParts()
            elif(userChoice=="4"):
               self.modifyPart()
            elif(userChoice=="5"):
               self.deltePart()
            elif(userChoice[0].lower()=="q"): #exits the loop if the user chooses Q or q
               break
            else:
               print("Invalid input. Try again.")
    
    def addPart(self):
        '''
         Description: Method to add part to the Database from the console
         Parameters:
          self
        '''
        partDetails={} #empty dictionary to store the part details

        #Iterating over the attribute list and storing all the values in the partDetails dictionary
        for attr in Part.attribList:
          while(True): #Validation loop
           partDetails[attr]=input(f"Enter {attr}:")
           if(partDetails[attr]):
             break
           else:
             print(f"{attr} cannot be empty")  
        myPartObj=Part(partDetails)
        #Adding the part to the DB
        self.partDBObj.addPartToDB(myPartObj)
        print(f"Total Number of Parts : {PartDatabase.totalParts}")
            
          
    def searchBySerialNum(self):
       '''
        Description: Method to call the relavant method in PartDatabase to display a specific part
        Parameters:
           self
       '''
       while(True): #Validation loop
          serialNum=input("Enter the Serial Number of the part to display:")
          if(serialNum):
             break
          else:
             print("Serial Number cannot be empty")
       self.partDBObj.searchPartBySerialNum(serialNum)

    def modifyPart(self):
       '''
        Description: Method to modify the value of an existing part
        Parameters:
         self
       '''
       while(True): #Validation loop
          serialNum=input("Enter the Serial Number to modify the part:")
          if(serialNum):
             break
          else:
             print("Serial Number cannot be empty")
       partDetails=self.partDBObj.searchPartBySerialNum(serialNum)
       if partDetails:
        newPartDetails={}
        newPartDetails["partSerialNum"]=partDetails.getPartSerialNum()
        #Iterating over the attribute list and storing all the values in the partDetails dictionary
        for attr in Part.attribList:
         if  attr !="partSerialNum": # cannot modify the serial number since it is a key
           while(True): #Validation loop
             newPartDetails[attr]=input(f"Enter {attr}:")
             if(newPartDetails[attr]):
               break
             else:
               print(f"{attr} cannot be empty")  
        myPartObj=Part(newPartDetails)       
        self.partDBObj.modifyPart(myPartObj)
        print("********RECORD AFTER MODIFICATION********")
        self.partDBObj.searchPartBySerialNum(serialNum)
      
    def deltePart(self):
       '''
        Description: This method is used to delete a Part with the given serial number
        Parameters:
         Self
       '''
       while(True): #Validation loop
          serialNum=input("Enter the Serial Number of the part to display:")
          if(serialNum):
             break
          else:
             print("Serial Number cannot be empty")
       self.partDBObj.deltePart(serialNum)

#Code to trigger the menu
if(__name__=="__main__"):
   controllerObj=MainController()
   controllerObj.renderMenu()