import array
myArray=array.array("i",[val for val in range(1,11)])

print(myArray[0])

myArray[1]=12
myArray.append(12)

for val in myArray:
    print(val)