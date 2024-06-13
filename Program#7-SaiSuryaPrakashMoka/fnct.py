#************************************************************************************************
# Name: Sai Surya Prakash Moka
# ID: 00834035
# Description: This is a submodule which is used to plot a graph for the expression
# ax^n+bx^(n-1)+.....c=f(x). This program contains a menu which takes the degree, coefficeints 
# and the domain to evaluate the expression over from the user and performs all the necessary
# user validations. Finally, after validations are sucessfull it plots the graph
#************************************************************************************************
import matplotlib.pyplot as plt # Importing matplotlib.pyplot with an alias of plt

def menu():
    '''Description:This function used to display the menu options to plot the graph
       and call the other helper functions.
       Parameters: None
       Return type: None
    '''

    n=0 # variable to store the degree of the polynomial
    polyCoeff=[] #List to store the polynomial coefficeints
    domain=[] #List to store the domain values
    coeffSet=False #setting the coefficient mode to false
    domainSet=False #setting the domain mode to false
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
              n=polyDeg()
         elif(inputChoice=="2"):
              polyCoeff=collectCoefs(n)
              coeffSet=True #setting the coefficeint mode to true which helps in initiating the plot
         elif(inputChoice=="3"):
              domain=setDomain()
              domainSet=True#setting the Domain mode to true which helps in initiating the plot
         elif(inputChoice=="4"):
              if(coeffSet and domainSet): # Only plots when both coefficient moder and domain mode are set to true
                  computePolynomial(n,polyCoeff,domain)
                  coeffSet=False
                  domainSet=False
              else:
                  print("You need to enter both the coefficients and domain to plot. Try again!!")
         else:
              print("Invalid choice!! Try again.")

def polyDeg():
     '''Description:This function is used to set the degree of the polynomial
        Parameters: None
        Returns: Degree of the polynomial
     '''

     while(True): #Infintie loop to check for validation
          degree=input("Enter the degree of the polynomial:") #Getting the degree input from the user
          if(degree):
               degree=int(degree) #converting string to int 
               if(degree<0): #Checking if the degree is negative
                    print("Degree cannot be negative.Try again.")
               else:
                    break #breaking from theloop if the validation passes
          else: 
               print("Degree cannot be empty.Try again.")
     return degree  

def collectCoefs(degree):
     '''DescriptionThis function is used to collect the coefficients of the ploynomial
        Parameter: Accepts degree as an argument
        Returns: coefficient list
     '''
     while(True): #Main outer loop
        coeefList=[] #empty list to store the coefficients
        for i in range(0,degree+1): #iterating over the degree range
           while(True): #Infinite loop to check for validation
               coeef=input(f"Enter coefficient {i+1}:")
               if(coeef):
                    coeef=float(coeef)
                    coeefList.append(coeef) #adding each coefficient to the list
                    break
               else:
                    print(f"Coeeficient {i} cannot be empty")
        print(f"Entered coefficients are {coeefList}") 
        choice=input("Do you want to save the values ? (Y/N)") # getting confirmation from the user
        # to save or to key in the values again
        if(choice[0].lower()=='y'):
             break #breaking from the main outer loop
      
     return coeefList

def setDomain():
 '''Description: fucntion to set the domain to evaluate the polynomial over
    Parameters: none
    returns: domain as a list [start,stop,step]
 '''

 while(True):#Main outer loop
     dom=[]#empty list to store the domain range
     while(True): # loop for start value validation
          startValue=input("Enter the start value:")
          if(startValue):
            startValue=int(startValue)
            dom.append(startValue)
            break #breaks from the start value loop if validation pass
          else:
            print("Start value cannot be empty")
     while(True): #loop for stop value validation
            endValue=input("Enter the end value:")
            if(endValue):
                 endValue=int(endValue)
                 if(endValue<startValue):
                      print("End value cannot be less than start value. Try again.")
                 else:
                      dom.append(endValue)
                      break #breaks from the stop value loop if validation pass
            else:
                 print("End value cannot be empty")
     while(True): #loop for step count validation
            stepCount=input("Enter the step value:") 
            if(stepCount):
                dom.append(int(stepCount))
                break #breaks from step count loop if validation pass
            else:
                print("Step count cannot be empty. Try again.")
     print(f"Entered domain is Start Value:{startValue} End Value:{endValue} Step Value:{stepCount}")
     # getting confirmation from the user to save or to key in the values again
     choice=input("Do you want to save the values ? (Y/N)")
     if(choice[0].lower()=='y'):
          break 
 return dom


def pltFnct(x,y):
     '''
     Description: Plots a graph with the given x and y cordinates. Accepts list of x an y coordinates
     Parameters: x and y co-ordinates lists
     Return type: None
     '''
     #get a figure
     fig,ax= plt.subplots()
     #set title
     ax.set_title('Poly Eval')
     #set x label
     ax.set_xlabel('Range')
     #set y label
     ax.set_ylabel('Domain')
     #turn on grid
     ax.grid()
     #plot
     ax.plot(x,y)
     #display the plot
     plt.show()
     
def computePolynomial(degree, coeeficients, domain):
     '''
     Description: This function is used to compute the polynomial for a given degree, coefficeints and domain
     Parameters: degree, coefficeints and domain
     return type: none
     '''
     xArr=[] #Empty list to store the X-Coordinates
     yArr=[] #Empty list to store the Y-Coordinates
     for dom in range(domain[0],domain[1],domain[2]): #iterating over the specified domain
          xArr.append(dom)
          ySum=0
          for deg in range(0,degree+1):
               ySum+=(coeeficients[deg]*(dom**(deg))) #evalauting the expression ax^n+bx^(n-1)+.....c=f(x)
          yArr.append(ySum)
     pltFnct(xArr,yArr) #calls the plot function
               

