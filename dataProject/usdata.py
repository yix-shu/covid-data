import pandas as pd
import numpy as np  
import matplotlib as plt
import datetime 

df = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv")
print(df.describe()) #descriptive stats
print(df.head(10)) #top 10 lines of stats from file
state = input("Which state would you like to analyze? ")
startDate = input("What is the start date you are interested in? ")
endDate = input("What is the end date you are interested in? ")

def dateBefore(date1, date2):
    date1 = date1.split("-")
    date2 = date2.split("-")
    date1 = datetime.date(int(date1[0]), int(date1[1]), int(date1[2]))
    date2 = datetime.date(int(date2[0]), int(date2[1]), int(date2[2]))
    return date1 < date2

def toDate(date1):
    date1 = date1.split("-")
    date1 = datetime.date(int(date1[0]), int(date1[1]), int(date1[2]))
    return date1 

#print(compareDates("2020-12-25","2020-12-12"))

stateData = df.loc[df['state'] == state]
stateData = df.loc[toDate(startDate) <= toDate(df['date']) <= toDate(endDate)]
print(stateData)