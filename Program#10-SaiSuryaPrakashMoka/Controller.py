#**********************************************************************************************
# Name: Sai Surya Prakash Moka
# ID: 00834035
# Description: This is the class which calls all the related methods in the RedBlackTreeManager
# class which orchestrates the entire application.
#**********************************************************************************************
from RedBlackTreeManager import * #importing all the methods from RedBlackTreeManager

class Controller:
    
    def initiateProcess(self):
        #Creating the instance of the red balck tree
        myRedBlackTreeObj=RedBlackTreeManager()

        #getting the file path from the user

        while(True): #Loop for doing the input validation
             filePath=input("Enter the file absolute path:") #Prompting the user to enter the path
             if(filePath):#if filePath is not empty break out of the loop
                 break
             else:
                 print("File path cannot be empty.Try again.")
        
        #Calling the method to read data from the file
        fileData=myRedBlackTreeObj.readTextFile(filePath)

        #checking whether data exists in the file
        if(fileData):
            #calling the method to get the words from the file
            words=myRedBlackTreeObj.getWords(fileData)
        else:
            print("Input file is empty")

        #Adding all the words to the red balck tree
        for word in words:
            myRedBlackTreeObj.insertNewWord(word.lower())

        #myRedBlackTreeObj.printTree()

        while(True): #Loop for doing the input validation
            # Find a word in the tree
            findWord = input("Enter a word to find its frequency in the file: ")
            if(findWord):
                break
            else:
                print("Search word cannot be empty")

        frequency = myRedBlackTreeObj.searchWord(findWord) #getting the word frequency
        print(f"Word: {findWord} Frequency:{frequency}")

        #Getting all the required stats
        treeInfoDic=myRedBlackTreeObj.getTreeInfo()
        #Iterating over the dictionary to print
        for key,value in treeInfoDic.items():
            print(f"{key} : {value}")
        
        #Saving the tree as a json file
        #getting the file path from the user
        while(True): #Loop for doing the input validation
             filePath=input("Enter the file absolute path to save the output in JSON:") #Prompting the user to enter the path
             if(filePath):#if filePath is not empty break out of the loop
                 break
             else:
                 print("File path cannot be empty.Try again.")
        myRedBlackTreeObj.saveTreeToFile(filePath)

        # Remove a word from the tree
        while(True):
            remove_word = input("Enter a word to remove from the tree: ").lower()
            if remove_word:
                break
            else:
                print("Word cannot be empty")
                
        myRedBlackTreeObj.deleteNode(remove_word)
        print(f"'{remove_word}' has been removed from the tree.")



if __name__=="__main__":

    #creating the controller object
    myController=Controller()
    myController.initiateProcess()