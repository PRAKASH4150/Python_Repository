#**********************************************************************
# Assignment 3
# Name: Sai Surya Prakash Moka 
# ID: 00834035
# Description: This Python module contains List and List Manipulations
#
#**********************************************************************

#The below list contains Cities and has a length of 5 elements
cityList=["New York City","West Haven","Hartford","Irving","Springfield"]

#The below list contains zip codes and has a length of 5 elements.Each 
#value is positionally indexed with the CityList i.e, The first element
#in the city list corresponds to the first element in the zipList..
zipList=["10001","06516","06101","75014","01020"]

#The below list is a compositecontains a list of list. Each list is city
#and zipcodes respectively
compList=[cityList,zipList]

#Indexing the Individual Lists
print("---------From Individual List-----------")
#First Element in the list
print(f"City Name: {cityList[0]} | Zip Code: {zipList[0]}")
#Last Element in the list. The index -1 is used access the last element
print(f"City Name: {cityList[-1]} | Zip Code: {zipList[-1]}")
#Accessing any other element in the list
print(f"City Name: {cityList[2]} | Zip Code: {zipList[2]}")
print("----------------------------------------")

# Indexing the elements in the Composite List
print("---------From Composite List-----------")
#First Element in the list
print(f"City Name:{compList[0][0]} Zip Code: {compList[1][0]}")
#Indexing the last element  in the composite list
print(f"City Name:{compList[0][-1]} Zip Code:{compList[1][-1]}")
#Accesing element at index 3
print(f"City Name:{compList[0][3]} Zip Code:{compList[1][3]}")
print("----------------------------------------")

#Appending to the individual list

#Getting the city and zip code inputs from the user
print("---------Appending to Individual List-----------")
cityName=input("Please enter the city name:")
zipCode=input("Please enter the zip code:")

#The append() function is used to append to the end of the list
cityList.append(cityName)
zipList.append(zipCode)

print("List After Appending:")
print(f"City Names: {cityList} Zip Codes: {zipList}")
print("-------------------------------------------------")

#Appending to the composite list

#Getting the city and zip code inputs from the user
print("---------Appending to Composite List-----------")
cityName=input("Please enter the city name:")
zipCode=input("Please enter the zip code:")

#Appending to the composite list
#Appending to the first sub list
compList[0].append(cityName)
#Appending to the next sub list
compList[1].append(zipCode)

print("Composite List after Appending:")
print(f"City Names : {compList[0]} Zip Codes: {compList[1]}")
print("-------------------------------------------------")

#Deleting from the individual list

#Getting the city and zip code inputs from the user
print("---------Deleteing from Individual List-----------")
#Getting the city and zip code inputs from the user
cityName=input("Please enter the city name:")

#Checking whether the entered city is present in the list 
if(cityName in cityList):
    # remove() is used to remove that object from the list if found
    recordIndex=cityList.index(cityName)
    cityList.remove(cityName)
    zipList.remove(zipList[recordIndex])
    print("List After Deleting:")
    print(f"City Names: {cityList} Zip Codes: {zipList}")
else:
    #printing the error message
    print(f"{cityName} not found in the exisitng list")
print("-------------------------------------------------")

#Deleting from the Composite List
print("---------Deleteing from Composite List-----------")
#Getting the city and zip code inputs from the user
cityName=input("Please enter the city name:")

#checking whether the enetered city is present in composite list

if cityName in compList[0]:
    #remove() is used to remove that object from the list
    recordIndex=compList[0].index(cityName)
    compList[0].remove(cityName)
    compList[1].remove(compList[1][recordIndex])
    print("Composite List After Deleting:")
    print(f"City Names: {compList[0]} Zip Codes: {compList[1]}")
else:
     #printing the error message
    print(f"{cityName} not found in the exisitng list")
print("-------------------------------------------------")

#len() function is used to get the length of the list
print("--------Size of the Individual Lists--------")
print(f"City List Length: {len(cityList)} Zip Code List Length: {len(zipList)}")
print("-------------------------------------------------")

print("--------Size of the Composite Lists--------")
print(f"Composite List Length: {len(compList)}")
print("-------------------------------------------------")

#Indexing from the end to the beginning of the individual and composite Lists
# For Individual Lists
print("--------Indexing Individual list from last to begining-----------")
for index in range(len(cityList)-1,-1,-1):
    print(f"City Name: {cityList[index]} | Zip Code: {zipList[index]}")
print("-------------------------------------------------")

# For composite lists
print("--------Indexing Composite list from last to begining-----------")
for index in range(len(compList[0])-1,-1,-1):
    print(f"City Name: {compList[0][index]} | Zip Code: {compList[1][index]}")
print("-------------------------------------------------")

#code to walk through the Lists and create a nicely formatted output with a 
#header followed by the List data

print("---------Iterating through the list----------")
for index in range(0,len(compList[0])):
    print(f"City{index+1} : {compList[0][index]} , Zip{index+1} : {compList[1][index]}")
print("-------------------------------------------------")

#Tuple Operations

#The below tuple contains the city values separated by a ,
cityTuple=("New York City","West Haven","Hartford","Irving","Springfield")

#The below tuple contains the zip code values separated by a ,
zipTuple=("10001","06516","06101","75014","01020")

#The below list contains city,tuple pairs 
compTupeList=list(zip(cityTuple,zipTuple))

#Indexing the elements in the Tuple List
#Indexing the first element:
print("---------Indexing the elements in the Tuple List---------")
print(f"City Name: {compTupeList[0][0]} Zip Code: {compTupeList[0][1]}")
#Indexing the last element
print(f"City Name: {compTupeList[-1][0]} Zip Code: {compTupeList[-1][1]}")
print("---------------------------------------------------------")

#Appending to the tuple list
print("----------------Appending to the Tuple List----------------")
#Getting the city name and zip code inputs from the user
cityName=input("Enter the city name:")
zipCode=input("Enter the Zip Code:")
#appending the tuple to the list
compTupeList.append((cityName,zipCode))
#List after appending
print(f"After Appending to the List: {compTupeList}")
print("---------------------------------------------------------")

#deleting from the tuple list
print("----------------Deleting from the Tuple List----------------")
#deleting the first element
del compTupeList[0]
print(f"List after deleting first element {compTupeList}")
#deleting the last element
del compTupeList[-1]
print(f"List after deleting last element {compTupeList}")
print("---------------------------------------------------------")

#obtaining the length of tuple list
print("----------Length of Tuple List--------------")
print(f"Length of Tuple List: {len(compTupeList)}")
print("---------------------------------------------------------")

#Indexing from the end to the beginning of the List of Tuples
print("--------Indexing tuple list from last to begining-----------")
for index in range(len(compTupeList)-1,-1,-1):
    print(f"City Name: {compTupeList[index][0]} | Zip Code: {compTupeList[index][1]}")
print("---------------------------------------------------------")

#code to walk through the tuple and create a nicely formatted output with a 
#header followed by the List data

print("---------Iterating through the Tuple list----------")
for index in range(0,len(compTupeList)):
    print(f"City Name: {compTupeList[index][0]} | Zip Code: {compTupeList[index][1]}")
print("---------------------------------------------------------")

# End of the Program