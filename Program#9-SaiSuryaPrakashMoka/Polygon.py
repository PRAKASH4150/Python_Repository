#***************************************************************************************************
# Name: Sai Surya Prakash Moka
# ID: 00834035
# Description:This is a class that represents the Polygon and contains methods to get the 
# number of sides, calculate the length of eachside and method to print the results formatted.
#***************************************************************************************************
class Polygon: #Creating a class named Polygon
    numPolyInstances=0 #class varaible to track the number of instances created from this class
    
    def __init__(self,polyType,numVertices,verticesList):
        '''
         Description: A constructor to initialize the Polygon class and takes the below Parameters
         Parameters:
           polyType - Type of the polygon (Triangle, Quadrilateral, Hexagon etc.,)
           numVertices - Number of vertices present in that ploygon as a number
           vertices- List of co-ordinate tuples which specifies the location of the co-ordinates
        '''
        #assigning the parameters to the instance varaibles
        self.polyType=polyType
        self.numVertices=numVertices
        self.verticesList=verticesList
        Polygon.numPolyInstances+=1
    
    def sideCount(self):
        '''
         Descritption: Method to get the number of sides present in that ploygon
         Parameters: self
         Returns: Number of vertices as a number
        '''
        #For any polygon the number of sides will be the number of vertices
        return self.numVertices #Returning the number of vertices
    
    def calcSideLength(self):
        '''
         Description:Method to calculate the length of each side in the ploygon
         Parameters: self
         Retutns: List of lengths for each side
        '''
        sideLengths=[] #empty list to store the side lengths
        for vertexIndex in range(0,self.numVertices):
            point1=self.verticesList[vertexIndex] # getting the tuple from the verticesList
           
            # getting the tuple from the verticesList. Using % operator to roll back to the 1st point
            # since polygon is a closed shape
            point2=self.verticesList[(vertexIndex+1)%(self.numVertices)]

            #computing the distance between two points. Since each point is a tuple pair (x1,y1)
            # indexing them is possible
            distance=sum([(point2[0]-point1[0])**2,(point2[1]-point1[1])**2])**0.5

            #appending the computed distance to the list
            sideLengths.append(round(distance,2))
        
        return sideLengths #Returning the side lengths
    
    def printResults(self):
        '''
         Description: Method to print the computed results and to print the instance variables
         Parameters: self
        '''
        print("*************************************")
        print(f"Polygon Name: {self.polyType}")
        print(f"Number of Vertices: {self.numVertices}")
        #iterating over the vertex list to print each vertex
        for index,vertex in enumerate(self.verticesList):
            print(f"Vertex {index}: {vertex}")
        #calling the sideCount() method to print the number of sides in the polygon
        print(f"Number of sides: {self.sideCount()}") 
   
        #calling the method calcSideLength and iterating over it to 
        #produce a nicely formatted output.
        for index,sideLength in enumerate(self.calcSideLength()):
            print(f"Length b/w [{self.verticesList[index]},{self.verticesList[(index+1)%(self.numVertices)]}] : {sideLength} units")
        print("*************************************")



            

            



