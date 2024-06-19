#**********************************************************************************************
# Name: Sai Surya Prakash Moka
# ID: 00834035
# Description: This is the class which contains all the operations related to red black tree
# like insert, delete, methods for fixing the node after insert and delete. Method to get
# all the tree details like max word count etc. and also method to save the tree in JSON
# format.
#**********************************************************************************************
from Node import * #Importing the node class
import json #importing the json library
class RedBlackTreeManager:
    '''
     Class containing all the methods required for
     crearting a red black tree and to maintain 
     all the red black treee properties
    '''
    #Initializing the constructor
    def __init__(self):
        self.LEAF=Node("") #Setting empty value to the leaf
        self.LEAF.color="Black" #Setting black color to the leaf
        self.LEAF.lChild=None #Null referencing L-child
        self.LEAF.rChild=None #Null referencing R-child
        self.rootNode=self.LEAF #Initializing the root nodre as leaf node to start with

    def readTextFile(self,filePath):
        '''
         Method to read the specified file. Throws file not found error if the 
         file doesnot exists
        '''
        try:
            with open(filePath, 'r') as file:
             text = file.read()
        except FileNotFoundError:
            print(f"File in the path:{filePath} doesnot exist") #throws exception if file not found
        return text
    
    def getWords(self,lines):
        words = lines.lower().split()
        return words
    
    def insertNewWord(self,word):
        '''
        Description: This method is used to insert a new node on 
        to the red black tree.
        Parameters:
         Word: New word to be inserted
        '''
        node=Node(word)
        node.parent=None 
        node.rChild=self.LEAF #Setting r-child as leaf node
        node.lChild=self.LEAF #Setting l-child as leaf node
        node.color="Red"

        y = None
        x = self.rootNode

        while x != self.LEAF :#Finding the position to put the new word
            y = x
            if word == x.word:
                x.wordCount += 1 #incrementing the wordcounter
                return
            elif node.word < x.word :
                x = x.lChild
            else :
                x = x.rChild
        node.parent = y #Parent of new node will be y
        if y == None : # If parent is none then it is root node
            self.rootNode = node
        elif node.word < y.word :# Check if it is right Node or Left Node by checking the value
            y.lChild = node
        else :
            y.rChild = node

        if node.parent == None:#Coloring root node as black to maintain the red-black tree property
            node.color = 'Black'
            return

        if node.parent.parent == None :# If parent of node is Root Node
            return

        self.fixInsertedNode( node )# Else calling to fix the inserted node

     # Fix Up Insertion
    def fixInsertedNode(self, fixNode):
        while fixNode.parent.color == "Red":# While parent is red
            if fixNode.parent == fixNode.parent.parent.rChild:# if parent is right child of its parent
                u = fixNode.parent.parent.lChild#Left child of Granp
                if u.color == "Red": # if color of left child of grandparent is red
                    u.color = "Balck" # Set both children of grandparent node as black
                    fixNode.parent.color = "Black"
                    fixNode.parent.parent.color ="Red" # Set grandparent node as Red
                    fixNode = fixNode.parent.parent  # Repeat the algo with Parent node to check conflicts
                else:
                    if fixNode == fixNode.parent.lChild:  # If k is left child of it's parent
                        fixNode = fixNode.parent
                        self.RightRotate(fixNode)  #Call for right rotation
                    fixNode.parent.color = "Black"
                    fixNode.parent.parent.color = "Red"
                    self.LeftRotate(fixNode.parent.parent)
            else:   # if parent is left child of its parent
                u = fixNode.parent.parent.lChild # Right child of grandparent
                if u.color == "Red": # if color of right child of grandparent i.e, uncle node is red
                    u.color = "Black"  # Set color of childs as black
                    fixNode.parent.color = "Black"
                    fixNode.parent.parent.color = "Red" # set color of grandparent as Red
                    fixNode = fixNode.parent.parent # Repeat algo on grandparent to remove conflicts
                else:
                    if  fixNode== fixNode.parent.rChild: # if k is right child of its parent
                        fixNode = fixNode.parent
                        self.LeftRotate(fixNode) # Call left rotate on parent of k
                    fixNode.parent.color = "Black"
                    fixNode.parent.parent.color = "Red"
                    self.RightRotate(fixNode.parent.parent) # Call right rotate on grandparent
            if fixNode == self.rootNode:# If k reaches root then break
                break
        self.rootNode.color =    "Black"# Set color of root as black

    #Method for left rotation
    def LeftRotate( self ,rotateNode):
        y = rotateNode.rChild # Y = Right child of rotateNode
        rotateNode.rChild = y.lChild # Change right child of rotateNode to left child of y
        if y.lChild != self.LEAF:
            y.lChild.parent = rotateNode

        y.parent = rotateNode.parent # Change parent of y as parent of rotateNode
        if rotateNode.parent == None : # If parent of rotateNode == None ie. root node
            self.rootNode = y # Set y as root
        elif rotateNode == rotateNode.parent.lChild :
            rotateNode.parent.lChild = y
        else :
            rotateNode.parent.rChild = y
        y.lChild = rotateNode
        rotateNode.parent = y

    # Code for right rotate
    def RightRotate (self ,rotateNode) :
        y = rotateNode.lChild # Y = Left child of rotateNode
        rotateNode.lChild = y.rChild  # Change left child of rotateNode to right child of y
        if y.rChild != self.LEAF:
            y.rChild.parent = rotateNode

        y.parent = rotateNode.parent  # Change parent of y as parent of rotateNode
        if rotateNode.parent == None :   # If rotateNode is root node
            self.rootNode = y    # Set y as root
        elif rotateNode == rotateNode.parent.rChild :
            rotateNode.parent.rChild = y
        else :
            rotateNode.parent.lChild = y
        y.rChild = rotateNode
        rotateNode.parent = y

     # Deletion of node
    def deleteNode ( self ,word ) :
        self.deleteNodeHelperFunc( self.rootNode,word)#Call for deletion

     # Function to handle deletion
    def deleteNodeHelperFunc( self , node , word) :
        z = self.LEAF
        while node != self.LEAF :# Search for the node having that value/ key and store it in 'z'
            if node.word == word :
                z = node
            if node.word <= word :
                node = node.rChild
            else :
                node = node.lChild

        if z == self.LEAF : # If Key is not present then deletion not possible so return
            print (f"{word} not found to delte")
            return

        y = z
        y_original_color = y.color                          # Store the color of z- node
        if z.lChild == self.LEAF :                            # If left child of z is NULL
            x = z.rChild                                     # Assign right child of z to x
            self.transplantTree( z , z.rChild )            # Transplant Node to be deleted with x
        elif (z.rChild == self.LEAF) :                       # If right child of z is NULL
            x = z.lChild                                      # Assign left child of z to x
            self.transplantTree( z , z.lChild )             # Transplant Node to be deleted with x
        else :                                              # If z has both the child nodes
            y = self.minimum ( z.rChild )                    # Find minimum of the right sub tree
            y_original_color = y.color                      # Store color of y
            x = y.rChild
            if y.parent == z :                              # If y is child of z
                x.parent = y                                # Set parent of x as y
            else :
                self.transplantTree( y , y.rChild )
                y.rChild = z.rChild
                y.rChild.parent = y

            self.transplantTree( z , y )
            y.lChild= z.lChild
            y.lChild.parent = y
            y.color = z.color
        if y_original_color == 0 :                          # If color is black then fixing is needed
            self.fixDelete ( x )

     # Function to transplant nodes
    def transplantTree(self ,x,y) :
        if x.parent == None :
            self.rootNode = y
        elif x == x.parent.lChild :
            x.parent.lChild = y
        else :
            x.parent.rChild = y
        y.parent = x.parent

    # Function to fix issues after deletion
    def fixDelete ( self , x ) :
        while x != self.rootNode and x.color == "Black" :           # Repeat until x reaches nodes and color of x is black
            if x == x.parent.lChild :                       # If x is left child of its parent
                s = x.parent.rChild                        # Sibling of x
                if s.color == "Red":                         # if sibling is red
                    s.color = "Black"                           # Set its color to black
                    x.parent.color = "Red"                    # Make its parent red
                    self.LeftRotate(x.parent )                  # Call for left rotate on parent of x
                    s = x.parent.rChild
                # If both the child are black
                if s.lChild.color == "Black" and s.rChild.color == "Black":
                    s.color = "Red"                           # Set color of s as red
                    x = x.parent
                else :
                    if s.rChild.color == "Black":               # If right child of s is black
                        s.lChild.color = "Black"                  # set left child of s as black
                        s.color = "Red"                       # set color of s as red
                        self.RightRotate( s )                     # call right rotation on x
                        s = x.parent.rChild

                    s.color = x.parent.color
                    x.parent.color = 0                    # Set parent of x as black
                    s.rChild.color = 0
                    self.LeftRotate( x.parent )                  # call left rotation on parent of x
                    x = self.rootNode
            else :                                        # If x is right child of its parent
                s = x.parent.left                         # Sibling of x
                if s.color == "Red" :                         # if sibling is red
                    s.color = "Black"                           # Set its color to black
                    x.parent.color = "Red"                    # Make its parent red
                    self.RightRotate( x.parent )                  # Call for right rotate on parent of x
                    s = x.parent.lChild

                if s.rChild.color == 0 and s.rChild.color == 0 :
                    s.color = "Red"
                    x = x.parent
                else :
                    if s.lChild.color == "Black" :                # If left child of s is black
                        s.rChild.color = "Black"                 # set right child of s as black
                        s.color = "Red"
                        self.LeftRotate( s )                     # call left rotation on x
                        s = x.parent.lChild

                    s.color = x.parent.color
                    x.parent.color = "Black"
                    s.lChild.color = "Black"
                    self.RightRotate( x.parent )
                    x = self.rootNode
        x.color = "Black"
    
    def minimum(self, node):
        while node.lChild != self.LEAF:
            node = node.lChild
        return node
    
    # Function to print
    def printHelperFunc( self , node , indent , last ) :
        if node != self.LEAF :
            print(indent, end=' ')
            if last :
                print ("R----",end= ' ')
                indent += "     "
            else :
                print("L----",end=' ')
                indent += "|    "

            s_color = "Red" if node.color == "Red" else "BLACK"
            print ( str ( node.word ) + "(" + s_color + ")" )
            self.printHelperFunc ( node.lChild , indent , False )
            self.printHelperFunc ( node.rChild , indent , True )

    # Function to call print
    def printTree( self ) :
        self.printHelperFunc ( self.rootNode , "" , True )

    #Function to search for a particular word in the tree
    def searchWord(self, word):
        node = self.searchWordHelperFunc(self.rootNode, word) #calling the helper function
        if node:
            return node.wordCount #Returning the word count
        else:
            return 0

    def searchWordHelperFunc(self, node, word):
        if node == self.LEAF or word == node.word:
            return node

        if word < node.word:
            #Recursively calling the searchWordHelperFunc()
            return self.searchWordHelperFunc(node.lChild, word)
        return self.searchWordHelperFunc(node.rChild, word)
    
    def getTreeInfo(self):
        #Initializing the values
        self.maxWordOccr=""
        self.maxCount =  0
        self.minWordOccr="" 
        self.minCount = float('inf')
        self.totWords = 0
        self.totCount = 0
        self.uniqueWords = 0
        
        def inOrderTraversal(node):
            
            if node != self.LEAF:
                inOrderTraversal(node.lChild)
                self.totWords += 1
                self.totCount += node.wordCount
                self.uniqueWords += 1
                if node.wordCount > self.maxCount:
                    self.maxWordOccr=node.word
                    self.maxCount = node.wordCount
                if node.wordCount < self.minCount:
                     self.minWordOccr = node.word
                     self.minCount= node.wordCount
                inOrderTraversal(node.rChild)
        
        inOrderTraversal(self.rootNode)

        stats = {
            "Maximum_Occurred_Word": self.maxWordOccr,
            "Maximum_Occurred_Word_Count": self.maxCount,
            "Minimum_Occurred_Word": self.minWordOccr,
            "Minimum_Count": self.minCount,
            "total_number_of_word": self.totWords,
            "Unique_Word":self.uniqueWords ,
            "tree_depth": self.getDepth()
        }
        return stats

    def getDepth(self):
        def depthHelpFun(node):
            if node == self.LEAF:
                return 0
            left_depth = depthHelpFun(node.lChild)
            right_depth = depthHelpFun(node.rChild)
            return max(left_depth, right_depth) + 1
        return depthHelpFun(self.rootNode)
    
    def saveTreeToFile(self, filePath):
        def serialize(node):
            if node == self.LEAF:
                return None
            return {
                "word": node.word,
                "count": node.wordCount,
                "color": node.color,
                "left": serialize(node.lChild),
                "right": serialize(node.rChild)
            }
        try:
            with open(filePath, 'w') as file:
                json.dump(serialize(self.rootNode), file,indent=4)
        except FileNotFoundError:
            print(f"File doesnot exist in the path {filePath}")





