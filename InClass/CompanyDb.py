partsInventory=[]
partCount=0

while(partCount < 3):
    print("--------------------------------------")
    partAttr=['Company Part Number','Manufacturer Part Number','Manufacturer','Description',
          'Cost','Parts on Hand','Parts Needed','Lead Time']
    partDetails=[partAttr]
    for attrib in partAttr:
        partDetails.append(input("Enter "+attrib+" :"))
    n=1
    for attrib in partDetails[0]:
        print(f"{attrib}: {partDetails[n]}")
        n+=1
    partsInventory.append(partDetails)

    partCount+=1
    
print(partsInventory)