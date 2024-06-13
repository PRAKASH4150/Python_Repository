#******************************************************************************
# Name: Sai Surya Prakash Moka
# ID: 00834035
# Description: This program uses dictionaries to perform various manipulations
# on the months. This program uses dicitonary comprehension to produce other
# dictionaries with months having less than 30 days, with 30 days and with
# 31 days and dictionaries consisting of the months with the same last letter
# and with same first letter. Finally this program also produces dictionaries
# consisting of months for different seasons.
#******************************************************************************

#Dictionary of the months of the year and the total number of days for each
main_month_dict={
    "January": 31,"February": 28,  "March": 31,"April": 30,"May": 31,
    "June": 30,"July": 31,"August": 31,"September": 30,"October": 31,"November": 30,"December": 31
}

#Using dicitionary comprehension to get months with less than 30 days
lessthan_30_dict={ month:days for month,days in main_month_dict.items() if days<30}

#Using dicitionary comprehension to get months with 31days
months_31_dict={months:days for months,days in main_month_dict.items() if days==31}

#Using dicitionary comprehension to get months with 30days
months_30_dict={months:days for months,days in main_month_dict.items() if days==30}

#Dictionary to store the months with the same first letter
same_first_letter_dict={}
#Dictionary to store the months with the same last letter
same_last_letter_dict={}

#iterating over the main dictionary to get the months
for month in main_month_dict.keys():
    #checking if the first letter in the obtained month not in the same_first_letter_dict
    if month[0] not in same_first_letter_dict.keys():  
        same_first_letter_dict[month[0]] = [month] # Adding the new key  and month as a list
    #checking if the first letter in the obtained month in the same_first_letter_dict
    elif month[0] in same_first_letter_dict.keys(): 
        #appending the current month with the existing list
        same_first_letter_dict[month[0]].append(month) 
    #checking if the last letter in the obtained month not in the same_last_letter_dict
    if month[-1] not in same_last_letter_dict.keys():
        same_last_letter_dict[month[-1]] = [month] # Adding the new key and month as a list
     #checking if the last letter in the obtained month in the same_last_letter_dict
    elif month[-1] in same_last_letter_dict.keys(): 
        #appending the current month with the existing list
        same_last_letter_dict[month[-1]].append(month) 

#Dictionary to store the months for each season
seasons_dict={
    "Spring":("March","April","May"),
    "Summer":("June","July","August"),
    "Fall":("September","October","November"),
    "Winter":("December","January","February")
}

#using dictionary comprehension to get the months in spring season and storing as a dictionary
spring_season_dict={month:days for month,days in main_month_dict.items()
                     if month in seasons_dict["Spring"]}

#using dictionary comprehension to get the months in summer season and storing as a dictionary
summer_season_dict={month:days for month,days in main_month_dict.items()
                     if month in seasons_dict["Summer"]}

#using dictionary comprehension to get the months in fall season and storing as a dictionary
fall_season_dict={month:days for month,days in main_month_dict.items()
                     if month in seasons_dict["Fall"]}

#using dictionary comprehension to get the months in winter season and storing as a dictionary
winter_season_dict={month:days for month,days in main_month_dict.items()
                     if month in seasons_dict["Winter"]}

#Printing the months with less than 30 days
print("----------Months with less than 30 days-----------")
for month in lessthan_30_dict:
    print(month)
print("--------------------------------------------------")

#Printing thr months with 31 days
print("-----------Months with 31 days--------------------")
for month in months_31_dict:
    print(month)
print("--------------------------------------------------")

#Printing thr months with 30 days
print("-----------Months with 30 days--------------------")
for month in months_30_dict:
    print(month)
print("--------------------------------------------------")

#iterating over the same_first_letter_dict to print the months with the same first letters
print("--------Months with the same first Letters--------")
for letter,monthList in same_first_letter_dict.items():
   if(len(monthList)>1):
      print(f"Letter:{letter} Months:{monthList}")
print("--------------------------------------------------")


#iterating over the same_last_letter_dict to print the months with the same last letters
print("--------Months with the same last Letters-------- ")
for letter,monthList in same_last_letter_dict.items():
   if(len(monthList)>1):
      print(f"Letter:{letter} Months:{monthList}")
print("---------------------------------------------------")

#priting months in Spring Season
print("------------Months in Spring Season----------------")
for month,days in spring_season_dict.items():
    print(f"Month:{month} Days:{days}")
print("---------------------------------------------------")

#priting months in Summer Season
print("------------Months in Summer Season----------------")
for month,days in summer_season_dict.items():
    print(f"Month:{month} Days:{days}")
print("---------------------------------------------------")

#priting months in Fall Season
print("------------Months in Fall Season----------------")
for month,days in fall_season_dict.items():
    print(f"Month:{month} Days:{days}")
print("---------------------------------------------------")

#priting months in Winter Season
print("------------Months in Witner Season----------------")
for month,days in winter_season_dict.items():
    print(f"Month:{month} Days:{days}")
print("---------------------------------------------------")