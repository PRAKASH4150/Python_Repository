import copy
partsInventory=[] # This is the main list to store the parts


def extractAttributes(part):
    '''
    Description:This function returns the attributes for
    a given part as a list
    param: part (Dictionary)
    return: List of attributes for a given part
    '''
    return list(part)

def addAttribute(attribName,value,part): #Function to add a new attribute to a exisiting part
    if attribName in part.keys():
        print(f"Attribute {attribName} already present")
    else:
        part[attribName]=value
    return part

def checkForCommonAttributes(partsInventory):
    countOfAttributes=[] # Keep track of number of attributes in each part
    for part in partsInventory:
        countOfAttributes.append(len(part))

    #check if number of attributes are the same
    if(max(countOfAttributes) == min(countOfAttributes)):
        uniqueAttributes=[]
        partsInventoryCopy=copy.deepcopy(partsInventory)

        part1=partsInventoryCopy.pop()
        for part2 in partsInventory:
            for attribute in part2.keys():
                if attribute not in part1:
                    uniqueAttributes.append(attribute) 
if __name__=="__main__":
    part={"Company Part Number":"Ivy18909",
          "Manufacturer Part Number":"Ivy76890549",
          "Manufacturer":"Ivy Biomedical Systems.Inc",
          "Description":"This is a ECG machine",
          "Cost":2500,
          "Parts on Hand":45,
          "Parts Needed":57,
          "Lead Time":"3hrs"} # Dicitionary representing a part
    print(f"Before Adding Attrib: {part}")
    part=addAttribute("Remarks","None",part)
    print(f"After Adding Attrib: {part}")

    #iterating over the list of part attributes
    for attributes in extractAttributes(part):
        print(attributes)