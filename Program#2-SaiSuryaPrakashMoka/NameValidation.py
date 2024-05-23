#*****************************************************************
# Assignment 2
# Name: Sai Surya Prakash Moka 
# ID: 00834035
# Description: This python module gets an input from the user 
# representing first name and last name separated by a space then 
# input validations are prerformed on it and displays the name
# as title case on STDOUT or else an appropriate error message wil
# be rendered on STDOUT.
#*****************************************************************

while(True): # Infinite loop to repititively run the code

    # Getting the user input, stripping the leading and trailing whitespaces if any
    # and splitting the name in to two substrings using inbuilt split() method
    names=input("Enter your First Name and Last Name separated by a Space:").strip().split(" ")
    if(len(names)==2): #checking whether both first name and last name were entered
        firstName,lastName=names # Storing the contents of the array in two seperate variables
        if(firstName.isalpha()==False): # Performing Alphabetic validation for firstName
            print("Invalid entry!! First name cannot contain numeric characters. Try again.")
        elif(lastName.isalpha()== False):#Performing Alphabetic validation for lastName
            print("Invalid entry!! Last name cannot contain numeric characters. Try again.")
        elif(firstName.lower()==lastName.lower()): #checking whehter both first name and last name
            # are same by converting in to lower case
            print("Invalid entry!! First Name and Last Name cannot be the same")
        else:
            #Printing the first name and last name in title case after successful validations
            print("Name Entered:"+firstName.title()+" "+lastName.title())
            print("-----------------------------")
    else:
        if(len(names)>2):
            #Printing error message if the use enter more than two names
            print("Invalid entry!! You need to enter only First Name and Last Name separated "
                  "by a space. Try again")
        elif(len(names)<2):
             # Printing error rmessage if the user enters either of first name or last name
            print("Invalid entry!! Both First Name and Last Name should be entered. Try again.")
