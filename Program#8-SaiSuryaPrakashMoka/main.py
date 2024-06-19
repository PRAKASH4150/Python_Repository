#************************************************************************************************
# Name: Sai Surya Prakash Moka
# ID: 00834035
# Description: This is the main module which instanitates the class ExpressionPlot and class the
# required methods to plot the graph. This module contains of a function to render the menu 
# to the user inorder to call the methods present in the class ExpressionPlot.
#************************************************************************************************
from ExpressionPlot import * #importing all the methods present in the class ExpressionPlot

def menu():
    '''Description:This function used to display the menu options to plot the graph
       and call the other helper methods present in the ExpressionPlot class.
       Parameters: None
       Return type: None
    '''
    coeffSet=False #setting the coefficient mode to false
    domainSet=False #setting the domain mode to false
    myPlot=ExpressionPlot() #instantinating the class and labelling it as myPlot

    while(True): #starting an infinite loop
         #prompting the user to enter a choice from the provided options
         inputChoice=input("\nInput 1 to enter the degree of the polynomial."+
              "\nInput 2 to enter the coefficients of the polynomial."+
              "\nInput 3 to enter the domain to evaluate the ploynomial over"+
              "\nInput 4 to plot the polynomial over the specified domain"+
              "\nInput Q or q to quit the program"+
              "\nEnter your choice:")
         if(inputChoice.lower()=='q'): # if the choice is Q or q the program stops
              break
         elif(inputChoice=="1"):
              myPlot.polyDeg() #calling the method ployDeg using the object instance
         elif(inputChoice=="2"):
              myPlot.collectCoefs()  #calling the method collectCoefs using the object instance
              coeffSet=True #setting the coefficeint mode to true which helps in initiating the plot
         elif(inputChoice=="3"):
              myPlot.setDomain()#calling the method setDomain using the object instance
              domainSet=True#setting the Domain mode to true which helps in initiating the plot
         elif(inputChoice=="4"):
              if(coeffSet and domainSet): # Only plots when both coefficient moder and domain mode are set to true
                  myPlot.computePolynomial()#calling the method computePolynomial using the object instance
                  coeffSet=False
                  domainSet=False
              else:
                  print("You need to enter both the coefficients and domain to plot. Try again!!")
         else:
              print("Invalid choice!! Try again.")

if __name__=="__main__":
     menu() #condition which triggers the menu() function.
