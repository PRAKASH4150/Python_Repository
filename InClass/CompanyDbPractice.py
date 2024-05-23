partsInventory=[]
attrList=['Company Part Number','Manufacturer Part Number','Manufacturer','Description',
          'Cost','Parts on Hand','Parts Needed','Lead Time']

while(True):
    userChoice=int(input("\n1.Add Part to DB.\n2.Delete Part from DB\n3.Display Specific Part\n4For other operations\nEnter your choice:"))
    if(userChoice==1):
       numParts=int(input("Enter the number of Parts you want to enter:"))
       i=0
       while(i<numParts):
            partDetails=[attrList]
            for attrib in attrList:
                partDetails.append(input(f"Enter {attrib}:"))
            print("-------------------------")
            while(True): 
                commitChoice=input("Are you sure to add (Y/N)?")[0].upper()
                if(commitChoice=='Y'):
                   partsInventory.append(partDetails)
                   print("Record added successfully")
                   i+=1
                   break
                elif(commitChoice=='N'):
                   print("Please input the values again")
                   break
                else:
                    print("Invalid input")
    elif(userChoice==2):
        searchKey=input("Enter Company or Manufacturer part number:")
        deleteFlag=False
        for part in partsInventory:
            if((part[attrList.index("Company Part Number")+1]==searchKey) or
               (part[attrList.index("Manufacturer Part Number")+1]==searchKey)):
                partsInventory.remove(part)
                deleteFlag=True
                break
        if(deleteFlag != True):
            print("Record with the specified key not found.")        
        else:
            print("Record Deleted Successfully")
    elif(userChoice==3):
        searchKey=input("Enter Company or Manufacturer part number:")
        foundFlag=False
        for part in partsInventory:
            if((part[attrList.index("Company Part Number")+1]==searchKey) or 
               (part[attrList.index("Manufacturer Part Number")+1]==searchKey)):
                for attr in attrList:
                    print(f'{attr} : {part[attrList.index(attr)+1]}')
                foundFlag=True
                break
        if(foundFlag!=True):
            print("No record found with the given key.")
    elif(userChoice==4):
        recordCount=int(input("Enter the number of records to add to the list:"))
        compNumberList=[]
        i=0
        while(i< recordCount):
            compNumberList.append(input("Enter the Company Part Number"))
            i+=1
        operChoice=int(input("\n1.Calculate BOM cost\n2.Need List\nEnter your choice:"))
        if(operChoice==1):
            totalBomCost=0
            for partnum in compNumberList:
                for part in partsInventory:
                    if(part[attrList.index("Company Part Number")+1]==partnum):
                        totalBomCost+=(int(part[attrList.index("Cost")+1]) * int(part[attrList.index("Parts Needed")+1]))
                        break
            print(f"Total BOM cost: {totalBomCost}")
        elif(operChoice==2):
            needList=[]
            for partnum in compNumberList:
                for part in partsInventory:
                    if(part[attrList.index("Company Part Number")+1]==partnum):
                        if(int(part[attrList.index("Parts Needed")+1]) > int(part[attrList.index("Parts on Hand")+1])):
                            needList.append(partnum)
                            break