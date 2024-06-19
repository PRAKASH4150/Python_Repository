#************************************************************************************************
# Name: Sai Surya Prakash Moka
# ID: 00834035
# Description: This is a class which is used to plot a graph for the expression
# ax^n+bx^(n-1)+.....c=f(x). This class contains all the helper methods used for plotitng a 
# graph. As soon as the object is initialized the values like degree, coeffList and domain will
# be initialized to empty or zero.
#************************************************************************************************
import matplotlib.pyplot as plt # Importing matplotlib.pyplot with an alias of plt

class ExpressionPlot: #class named ExpressionPlot

    def __init__(self): #comnstructor to initialize the instance variables.
        self.degree=0 # variable to store the degree of the polynomial
        self.coeefList=[] #List to store the polynomial coefficeints
        self.domain=[] #List to store the domain values

    def polyDeg(self):
     '''Description:This method is used to set the degree of the polynomial
        Parameters: None
        Returns: Degree of the polynomial
     '''

     while(True): #Infintie loop to check for validation
          self.degree=input("Enter the degree of the polynomial:") #Getting the degree input from the user
          if(self.degree):
               self.degree=int(self.degree) #converting string to int 
               if(self.degree<0): #Checking if the degree is negative
                    print("Degree cannot be negative.Try again.")
               else:
                    break #breaking from theloop if the validation passes
          else: 
               print("Degree cannot be empty.Try again.")
     return self.degree  
    
    def collectCoefs(self):
     '''Description:This method is used to collect the coefficients of the ploynomial
        Parameter: Accepts degree as an argument
        Returns: coefficient list
     '''
     while(True): #Main outer loop
        self.coeefList=[] #empty list to store the coefficients
        for i in range(0,self.degree+1): #iterating over the degree range
           while(True): #Infinite loop to check for validation
               coeef=input(f"Enter coefficient {i+1}:")
               if(coeef):
                    coeef=float(coeef)
                    self.coeefList.append(coeef) #adding each coefficient to the list
                    break
               else:
                    print(f"Coeeficient {i} cannot be empty")
        print(f"Entered coefficients are {self.coeefList}") 
        choice=input("Do you want to save the values ? (Y/N)") # getting confirmation from the user
        # to save or to key in the values again
        if(choice[0].lower()=='y'):
             break #breaking from the main outer loop
      
     return self.coeefList
    
    def setDomain(self):
     '''Description: Method to set the domain to evaluate the polynomial over
     Parameters: none
     returns: domain as a list [start,stop,step]
     '''
     while(True):#Main outer loop
       self.domain=[]#empty list to store the domain range
       while(True): # loop for start value validation
          startValue=input("Enter the start value:")
          if(startValue):
            startValue=int(startValue)
            self.domain.append(startValue)
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
                      self.domain.append(endValue)
                      break #breaks from the stop value loop if validation pass
            else:
                 print("End value cannot be empty")
       while(True): #loop for step count validation
            stepCount=input("Enter the step value:") 
            if(stepCount):
                self.domain.append(int(stepCount))
                break #breaks from step count loop if validation pass
            else:
                print("Step count cannot be empty. Try again.")
       print(f"Entered domain is Start Value:{startValue} End Value:{endValue} Step Value:{stepCount}")
       # getting confirmation from the user to save or to key in the values again
       choice=input("Do you want to save the values ? (Y/N)")
       if(choice[0].lower()=='y'):
           break 
       return self.domain
     
    def pltFnct(self,x,y):
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
     
    def computePolynomial(self):
      '''
      Description: This method is used to compute the polynomial for a given degree, coefficeints and domain
      Parameters: degree, coefficeints and domain
      return type: none
      '''
      xArr=[] #Empty list to store the X-Coordinates
      yArr=[] #Empty list to store the Y-Coordinates
      for dom in range(self.domain[0],self.domain[1],self.domain[2]): #iterating over the specified domain
          xArr.append(dom)
          ySum=0
          for deg in range(0,self.degree+1):
               ySum+=(self.coeefList[deg]*(dom**(deg))) #evalauting the expression ax^n+bx^(n-1)+.....c=f(x)
          yArr.append(ySum)
      self.pltFnct(xArr,yArr) #calls the plot function