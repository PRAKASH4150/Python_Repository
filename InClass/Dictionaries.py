#Getting the input string from the user
inputString=input("Enter the input string:")

#Initializing an empty dictionary 
letterCountDict=dict()

# iterating over the inputstring
for char in inputString:
    # checking for membership 
    if char in letterCountDict:
        letterCountDict[char] +=1 # if the key already exists increment the count
    elif char not in letterCountDict:
        letterCountDict[char]=1 #if the key doesnot exists assign a value 1 to it

for (key, value) in letterCountDict.items():
    print(f"Char: {key} Count:{value}")