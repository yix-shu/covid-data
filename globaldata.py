import pandas as pd
import numpy as np
import matplotlib as pt
from datetime import date

df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")
#Our World In Data Organization data
print("Overall Stats of Global COVID-19 Data:")
print(df.describe()) 
print("\nOverview Stats:")
print(df.head())
regional = df.groupby("continent").sum() #groups and sums the group stats

print("\nNew Cases (Regionally): ")
regionalNew = df.groupby("continent").sum()['new_cases'].reset_index()
print(regionalNew)
print("\nTotal Cases (Regionally): ")
regionalTotal = df.groupby("continent").sum()['total_cases'].reset_index()
print(regionalTotal)
print("\nNew and Total Cases by Date (Regionally): ")
dateNew = df.groupby(["date", "location"]).sum()[['new_cases', 'total_cases']].reset_index()
recentNew = dateNew.sort_values(by = ['date', 'new_cases'], ascending = False)

print("\nRecent Cases")
print(recentNew)
def rank(data, date, numOfCountries, rankType): #countries with highest rates
    """
    This function returns an organized dataset that is sorted by number of new cases based on an indicated date

    Args:
        data - takes the desired dataset to organize
        date - takes the desired date of the dataset 
        numOfCountries - number of countries in the top or bottom ranks (ex.; top 10 or bottom 10)
        rankType - top or bottom/highest or lowest
    """
    x = data.loc[data["date"] == date]
    x = x.loc[x['new_cases'] > 0.0]
    if (rankType == "high"):
        return print(x.head(numOfCountries)) 
    if (rankType == "low"):
        return print(x.tail(numOfCountries)) 

print("Highest on 12/25: ")
lows = rank(recentNew, '2020-12-25', 20, "high")

print("Lowest on 12/25: ")
highs = rank(recentNew, '2020-12-25', 20, "low")

def newDate(date, days):
    """
    returns the date of the days before the inputted date
    ex. newDate("2020-12-15", 5) would return "2020-12-10"
    Args:
        date - takes the desired date from which the days we will count backwards from (ex. if the date is 2020-12-15, we will return the days back from 2020-12-15)
        days - days before the date
    """
    nowDate = date.split('-')
    nowDate[2] = int(nowDate[2]) - days
    newDate = "{}-{}-{}".format(nowDate[0], nowDate[1], nowDate[2])
    return newDate

def countryData(country, data, days, endDate):
    """
    This function compiles all the data on a specific country for a specified timespan 
    ex. countryData("United States", recentNew, 5, "2020-12-26") would return all the data on the US from 2020-12-21 to 2020-12-26

    Args:
        country - specified country for which the data will be compiled on
        data - data set to be organized
        days - timespan in days
        endDate - date of the last/most recent data point
    """
    x = data.loc[data["location"] == country]
    for day in range(days + 1):
        print(x.loc[x["date"] == newDate(endDate, day)])
now = str(date.today())
print("\n\nThe past few days for the US: \n")
countryData("United States", recentNew, 5, now)

print("\n~~~~~")
nation = input("Which country would you like to analyze? ")
days = int(input("What is the timespan you would like to analyze? (in days): "))
print('\033[94m'+f"\nData on {nation} {days} days from {now}: \n" + '\033[0m')
countryData(nation, recentNew, days, now)

