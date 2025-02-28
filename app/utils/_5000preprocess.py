import json
import pandas as pd
# from home import df5000movies
# from home import df5000credits
pd.set_option('display.float_format', lambda x: '%.3f' % x)

def cleanCreditsData(data):
    data = data.dropna(subset=(["star_one"]))
    data = data.dropna(subset=(["star_two"]))
    return data

def dropColumn(data, col):
    data = data.drop(columns=[col])
    return data

#function to convert colum to json format
def toJson(data, col, newCol):
    data[newCol] = data[data[col].notnull()][col].map(lambda x: json.loads(x))
    return data
# print(toJson(df5000movies, 'genres', 'json_genres'))


def makeGenreCol(data,col):
    for j in range(len(data[col])):
        jsonObj = data[col][j]

        for i in range(len(jsonObj)):
            name = str(jsonObj[i]['name']).lower()
            if name not in data:
                data[name] = pd.Series([0 for x in range(len(data[col]))])
    return data
                
def makeStarCol(data):
    data['star_one'] = pd.Series([None for x in range(len(data))])
    data['star_two'] = pd.Series([None for x in range(len(data))])
    return data

def populateStars(data,col):
    for j in range(len(data[col])):
        jsonObj = data[col][j]
        # index into keyword name
        try:
            for i in range(2):
                name = str(jsonObj[i]['name']).lower()
                if i == 0:
                    data.at[j, "star_one"] = name
                if i == 1:
                    data.at[j, "star_two"] = name
        except: 
            # print("No actors") 
            continue   
    return data

#convert genre names in json object to columns
def populateGenreCol(data, col):
    for j in range(len(data[col])):
        jsonObj = data[col][j]
        # index into keyword name
        for i in range(len(jsonObj)):
            name = str(jsonObj[i]['name']).lower()
            data.at[j, name] = 1
    return data
          
#homepage seems insignificant so I dropped it

def updateMovies(data):
    data = dropColumn(data, 'homepage')     
    data = toJson(data, 'genres', 'json_genres') 
    data = dropColumn(data, 'genres')
    data = makeGenreCol(data, "json_genres")
    data = populateGenreCol(data, "json_genres") 
    return data
    
    
def updateCredits(data):
    data = toJson(data, 'cast', 'json_cast')
    data = dropColumn(data, 'cast')
    data = makeStarCol(data)
    data = populateStars(data, 'json_cast')
    data = dropColumn(data, 'json_cast')
    data = cleanCreditsData(data)
    return data


def main5000(movie_data,credits_data):
    movie_data = updateMovies(movie_data)
    credits_data = updateCredits(credits_data)
    data = pd.merge(movie_data, credits_data, left_on="id", right_on="movie_id")
    return data

# data_5000 = main5000(df5000movies, df5000credits)
# data_5000.describe()