#***************************************************************************************************
# Name: Sai Surya Prakash Moka
# ID: 00834035
# Description: This module is used to create various instances out of the Polygon class and
# triggers the appropriate methods to print the test results and it also prints the class
# variable which gives the total number of instances created 
#***************************************************************************************************
from Polygon import * #Importing all the methods from the Ploygon class

def testClass():# Function that contains code to test the Polygon class
    #Instantiating an object of type Triangle
    myTriangle=Polygon("Triangle",3,[(1,3),(3,6),(7,14)])
    #Instantiating an object of type Quadrilateral
    myQuadrilateral=Polygon("Quadrilateral",4,[(7,9),(2,6),(11,18),(34,56)])
    #Instantiating an object of type Hexagon
    myHexagon=Polygon("Hexagon",6,[(7,11),(11,14),(16,89),(23,45),(67,45),(12,34)])

    #printing the results for each polygon type
    myTriangle.printResults()
    myQuadrilateral.printResults()
    myHexagon.printResults()

    #Accessing the class variable to get the number of polgon instances created
    print(f"Number of Polygon Instances: {Polygon.numPolyInstances}")

#invoking the Test class function
if __name__=="__main__":
    testClass()
