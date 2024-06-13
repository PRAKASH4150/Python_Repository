#***************************************************************************************
# Name:Sai Surya Prakash Moka
# ID: 00834035
# Description: This program makes use of the matplot libraray to plot a graph for the
# expresssion y=ax^2+bx+c with the given a,b,c constants and for x values from a range
# of 0 to 1 with an increment of 0.01. This code demonstrates plotting the graph with
# individual lists and graph plotted with the help of list of coordinate tuples
#***************************************************************************************
import matplotlib.pyplot as plt #Importing the matplot library with an alias as plt

#Function to plot the graph between Y vs X
def plot_signal(x,y):
  '''Plots a graph with the given x and y cordinates. Accepts list of x an y coordinates'''
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

#constants in the expression y=ax^2+bx+c 
a=0.01
b=0.002
c=0.0001

#list to store x-cordinates starting from 0 to 1 with a step of 0.01
xCordList=[round(xVal*0.01,2) for xVal in range(0,101)]

#Dependant variable y-cordinates after executing for each poin in xCordList
yCordList=[((a*(xVal)**2)+(b*xVal)+(c)) for xVal in xCordList]

#calling the function to plot the graph
plot_signal(xCordList,yCordList)

cordTupleList=[] #List to store the cordinate tuples

#iterating over the exisiting xCordList and taking each individual X-cordinate
for index,xCord in enumerate(xCordList): 
  yCord=yCordList[index] #Indexing Y-Cord using the enumerate
  cordTupleList.append((xCord,yCord)) # Appending the cordinates as a tuple to the list

xPointCord=[] #List to store individual x-coordinates
yPointCord=[] #List to store individual y-coordinates
for point in cordTupleList: #Iterating over the tuples in cordTupleList
  xPointCord.append(point[0]) #indexing the element in the tuple at 0th position and appending to the list
  yPointCord.append(point[1])#indexing the element in the tuple at 1st position and appending to the list

#calling the function to plot the graph
plot_signal(xPointCord,yPointCord)

#------------------------END OF PROGRAM--------------------------------------