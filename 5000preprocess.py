

import json

import pandas as pd
df5000movies = pd.read_csv('../5000/tmdb_5000_movies.csv')
pd.set_option('display.float_format', lambda x: '%.3f' % x)

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

def main(data):
    data = dropColumn(data, 'homepage')     
    data = toJson(data, 'genres', 'json_genres') 
    data = dropColumn(data, 'genres')
    data = makeGenreCol(data, "json_genres")
    data = populateGenreCol(data, "json_genres") 
    return data
    
    
main(df5000movies)