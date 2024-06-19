#**********************************************************************************************
# Name: Sai Surya Prakash Moka
# ID: 00834035
# Description: This is the class which represents each node in the red-black tree
# #Initializing the node with the given word and setting the default lchild and rchild
#**********************************************************************************************
class Node: #This is the class which represents each node in the red-black tree
    #Initializing the node with the given word and setting the default lchild and rchild
    def __init__(self,word):
        self.word = word # Word Passed to the Node
        self.wordCount=1 #Gives the number of times the word got repeated
        self.parent = None # Parent of Node
        self.lChild = None # Left Child of Node
        self.rChild = None # Right Child of Node
        self.color = "Red" #A new node is always colured red.