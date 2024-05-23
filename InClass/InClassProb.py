
partDatabase=[]

count=0
while(count<2):
    compPartNumer=input("Enter the company partnumber:")
    manuPartNumber=input("Enter the Manufacturer partnumber:")
    cost=int(input("Enter the cost:"))
    partDetails=[compPartNumer,manuPartNumber,cost]
    partDatabase.append(partDetails)
    count+=1

print(partDatabase)
print("--------Before Delete--------------")
for part in partDatabase:
    print("Company Part Number:",part[0])
    print("Manufacturer Part Number:",part[1])
    print("Cost:",part[2])
    print("----------------------")

compPartNumerDel=input("Enter the part number to be deleted:")

print("--------After Delete--------------")
for part in partDatabase:
    if compPartNumerDel in part:
        del(partDatabase[part])