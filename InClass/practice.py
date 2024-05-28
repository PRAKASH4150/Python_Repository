import array
myArray=array.array("i",[x for x in range(1,101)])
print(myArray[0])
myArray.append(1371)
print(myArray)
myArray.remove(1371)
print(myArray)

myString="Prakash"
for index, val in enumerate(myString):
    print(f"Index: {index} Value: {val}")

myList=[x for x in range(1,21)]
for index,value in enumerate(myList):
    print(f"Index : {index} Value:{value}")

list1=[1,2,3,4,5,6,7,8,9,10]
list2=['a','b','c','d','e','f','g','h','i','j']
list3=list(zip(list1,list2))
print(list3)

for index,(val1,val2) in enumerate(zip(list1,list2)):
    print(f"{index} {val1} {val2}")

a,b=zip(*list3)
print(a)
print(b)

myString='The quick brown fox jumped over the lazy moon!'
countO=0
countJ=0
countZ=0

for x in myString:
    if(x.lower()=='o'):
        countO+=1
    elif(x.lower()=='j'):
        countJ+=1
    elif(x.lower()=='z'):
        countZ+=1
print(f"Number of o's {countO}")
print(f"Number of j's {countJ}")
print(f"Number of z's {countZ}")

myString=""
if myString:
    print("string is not empty")
else:
    print("String is empty")

print("This is not empty") if myString else print("This is empty")