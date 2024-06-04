#**************************************************************************************
#Name: Sai Surya Prakash Moka
#ID: 00834035
#Description: This program calculates the distance between any two points in a given 
#list by iterating over it and appends the results to a list with the given format
#and finally displays nicely formatted output to the user
#**************************************************************************************
#List of Point Names
myPoints=['Point1','Point2','Point3','Point4','Point5','Point6']
#List of Cordintates as a tuples (x,y,z)
myCords = [(1.1, 1.0, 1.5), (2.0, 2.1, 2.2), (3.0, 3.1, 3.5), (4.0, 4.5, 4.8), (5.6, 5.7, 5.3), (6.2, 6.4, 6.7)]
#Empty list for storing distances
distanceList=[]

for i in range(0,len(myCords)): #Outermost for loop
    for j in range(i+1,len(myCords)):#Inner for loop
        distance=((myCords[j][0]-myCords[i][0])**2+(myCords[j][1]-myCords[i][1])**2
                  +(myCords[j][2]-myCords[i][2])**2)**0.5 #Computing the distance between 2 points
        #appending the Distancelabel and Distance computed to the distancelist
        distanceList.append(f"DistanceP{i+1}P{j+1}")
        distanceList.append(distance)


#Taking the sublist of distance list to store distance labels and values
distanceLabels=distanceList[0:len(distanceList):2]
distanceValues=distanceList[1:len(distanceList):2]

#Iterating over the distance list and printing the values
print("Iterating over the list of distances")
for index,distances in enumerate(distanceLabels):
    print(f"{distances} : {round(distanceValues[index],2)}")
print("--------------------------------------")

#List to store the distance tuple records
distanceTupleList=[]

for i in range(0,len(myCords)): #Outermost for loop
    for j in range(i+1,len(myCords)):#Inner for loop
        
        distance=((myCords[j][0]-myCords[i][0])**2+(myCords[j][1]-myCords[i][1])**2
                  +(myCords[j][2]-myCords[i][2])**2)**0.5 #Computing the distance between 2 points
        #appending the tuple to the list with the given format
        distanceTupleList.append((f"DistanceP{i+1}P{j+1}",[round(distance,2),myCords[i],myCords[j]]))

#Iterating over the list of tuples
print("Iterating over the list of tuples")
for distRecord in distanceTupleList:
    print(f"{distRecord[0]} : {distRecord[1][0]}") 
print("--------------------------------------")

#---------------------END OF PROGRAM-------------------