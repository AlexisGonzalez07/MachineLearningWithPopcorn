from home import df6820movies as df
import string
import pandas as pd
from datetime import datetime

def convertRating(rating):
    if rating == "G":
        return 1
    elif rating == "PG":
        return 2
    elif rating == "PG-13":
        return 3
    elif rating == "R":
        return 4
    else:
        return 5

def addRatingNum(data):
    data["rating_number"] = data['rating'].apply(lambda x: convertRating(x))
    return data

def cleanData(data):
    data = data.dropna(subset=(["budget"]))
    data = data.dropna(subset =(["rating"]))
    data = data.groupby('genre').filter(lambda x: len(x)>50)
    return data

def isKidFriendly(rating):
    try:
        if "G" in rating.upper():
            return 1
        else:
            return 0
    except: 
        return 0
    
def getMonthInt(date):
    month = date.split(" ")[0]
    if month[0].isnumeric():
        return None
    else:
        return datetime.strptime(month, '%B').month


def addMonthInt(data):
    
    data['month']= data['released'].apply(lambda date: getMonthInt(date))
    data = data.dropna(subset=(["month"]))    
    return data
    
    
def addKidFriendly(data):
    data["for_kids"] = data["rating"].apply(lambda x: isKidFriendly(x))
    return data

def main6820(data):
    data = addMonthInt(addRatingNum(addKidFriendly(cleanData(data))))
    return data
    
main6820(df)