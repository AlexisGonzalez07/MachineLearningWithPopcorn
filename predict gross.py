import pandas as pd
import numpy as np
from home import df6820movies as df
from processing6820 import main6820
from scipy import spatial

def vectorizeGenres(data, vectorized_data, column): #used for genre, director, writer, stars, countries, companies
    unique_types = list(data[column].unique())
    vectorized_data[column] = data[column].apply(lambda x: vectorizeGenre(x, unique_types))
    return vectorized_data

def vectorizeGenre(genre, unique_genres):
    binary_genres = np.zeros(len(unique_genres))
    for i in range(len(unique_genres)):
        if genre == unique_genres[i]:
            binary_genres[i] = 1
    return binary_genres


def calcDistVectors(veca, vecb):
    return 1 - spatial.distance.cosine(veca, vecb)

def calcDistVals(vala, valb):
    return min(vala, valb)/max(vala, valb)

#calculates "closeness" of movies. The higher dist is, the closer the are. Dist is probably a bad name because distance implies the opposite, so i'll likely change that
def calcDistMovies(moviea, movieb, data, data_to_vectorize, other_data):
    dist = 0
    for col in data.columns:
        if col in data_to_vectorize:
            dist += calcDistVectors(moviea[col], movieb[col])
        elif col in other_data and col != "name":
            dist += calcDistVals(moviea[col], movieb[col])
    return dist

#prepares data by creating vectors for non-numerical data
def prepareData(data, data_to_vectorize, other_data):
    data = main6820(data)
    prepared_data = pd.DataFrame()
    for col in data.columns:
        if col in data_to_vectorize:
            prepared_data = vectorizeGenres(data, prepared_data, col)
        elif col in other_data:
            prepared_data[col] = data[col].apply(lambda x: x)
    return prepared_data

# in progress
def predict_gross():
    name = input("Enter a movie title: ")

#checks data about genre, director, writer, etc. and score, votes etc.
def main(data):
    data_to_vectorize = ["genre", "director", "writer", "star", "country", "company"]
    other_data = ["score", "votes", "budget", "rating_number", "name"]
    prepared_data = prepareData(data, data_to_vectorize, other_data)

    #test lines, tests the third movie against the first 10 movies
    test_movie = prepared_data.iloc[3]
    print(data.iloc[3]["name"])
    similarities = []
    for i in range(10):
        similarities.append((data.iloc[i]["name"],calcDistMovies(test_movie, prepared_data.iloc[i], prepared_data, data_to_vectorize, other_data)))
    print(similarities)
main(df)