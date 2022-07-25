

import json

import pandas as pd
df5000movies = pd.read_csv('../5000/tmdb_5000_movies.csv')


def dropColumn(data, col):
    data = data.dropna(subset=([col]))
    return data

#homepage seems insignificant so I dropped it
df5000movies = dropColumn(df5000movies, 'homepage')
print(df5000movies.isnull().sum())

#function to convert colum to json format
def toJson(data, col, newCol):
    data[newCol] = data[data[col].notnull()][col].map(lambda x: json.loads(x))
    return data[newCol]
print(toJson(df5000movies, 'genres', 'json_genres'))


#convert genre names in json object to columns
def genre2Col(data, col):
    #step through genre column
    for j in range(len(data[col])):
        #save json object
        jsonObj = data[col][j]
        
        #index into keyword name
        for i in range(len(jsonObj)):
            #save name to a string obj
            name = str(jsonObj[i]['name']).lower()
            #create new column if genre doesn't exist a column
            if name not in data:
                data[name] = 0
                #add the column to the
                data[name].loc[j]  = 1
            else:
                data[name].loc[j] = 1
                
genre2Col(df5000movies, "json_genres")