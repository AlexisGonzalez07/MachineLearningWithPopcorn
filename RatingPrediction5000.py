#RatingPrediction5000
#Using the df5000 data from home.py, this module uses sklearn.ensemble.RandomForestRegressor to weigh traits which determine the IMDB rating of a particular movie
#Created: devongulley1602 2022-07-21
#Last Edit: devongulley1602 2022-07-26

import pandas as pd
import datetime as dt
import numpy as np
from itertools import chain
from preprocess5000 import data_5000 #this dataframe includes one hot encoding for all genres built into its columns by default


#Some further data trimming..
#NOTE: There are 997 records with missing budget data which have all been defaulted to $0.00
    # missing_budget = data_5000[data_5000.budget == 0]
    # len(missing_budget)

data_5000 = data_5000[data_5000.budget != 0]
#data_drop_scores = data_5000.drop('vote_average', axis=1)

data_5000.columns


data_matrix = data_5000.to_numpy()

scores = data_matrix[:,16].astype('float64') #data_5000['vote_average'] #IMDB scores are on on the 16th column
budgets = data_matrix[:,0].astype('float64') #budgets are the first column
all_star1 = data_matrix[:,42] #for the names of actors
all_star2 = data_matrix[:,43]
release_dates = pd.to_datetime(data_5000['release_date'], errors='coerce')

#Genres is a matrix with columns binary encoded to:
# {'action', 'adventure', 'fantasy','science fiction', 'crime', 'drama', 'thriller', 'animation', 'family','western', 'comedy', 'romance', 'horror', 'mystery', 'history', 'war','music', 'documentary', 'foreign', 'tv movie'} respectively
#and rows as each specific movie. ie if a movie (row) is of a certain category (column) its entry will be represented by a 1, otherwise 0
genres = data_matrix[:,19:39].astype('int64') #currently all 20 genres are stored in the data_matrix columns 19 to 39


#star_enc is a matrix with columns binary encoded to the top 5 primary and secondary stars

from sklearn.preprocessing import LabelBinarizer

from collections import Counter
topStars1 = [i[0] for i in Counter(all_star1).most_common(5)] #the names of the 5 most common star_one
topStars2 = [i[0] for i in Counter(all_star2).most_common(5)] #the names of the top 5 star_two

star1  = LabelBinarizer().fit(topStars1).transform(all_star1)
star2 = LabelBinarizer().fit(topStars2).transform(all_star2)





#The features that we would like to use to weigh in determining an IMDB score for a given film are currently:
#budget, the encoded genres, the encoded stars
features = [list(chain(*i)) for i in list(zip([[j] for j in budgets],genres,star1,star2))] #this line is horrible
feature_keys = list(chain(['budget'], list(data_5000.columns[19:39]), list(topStars1),list(topStars2)))
feature_keys

#'action', 'adventure', 'fantasy','science fiction', 'crime', 'drama', 'thriller', 'animation', 'family','western', 'comedy', 'romance', 'horror', 'mystery', 'history', 'war','music', 'documentary', 'foreign', 'tv movie'] #for each element in features

#Based off of df5000 data set what will a particular movie be rated given some properties?

#1. Look at the dataset, include keywords, cast, actors, release_date.day/month/year/isWeekend

from sklearn.ensemble import RandomForestRegressor as rf #Regressor because we're working with continuous values
from sklearn.model_selection import train_test_split

rf = rf(n_estimators = 1000)

features_train, features_test, scores_train, scores_test = train_test_split(features,scores,test_size = 0.8)

rf.fit(features_train, scores_train)
predictions = rf.predict(features_test)
predictions

errors = abs(predictions-scores_test)
np.average(errors)
np.max(errors)
np.min(errors)
max(predictions)
min(predictions)



rf.feature_importances_

#For printing the relative importance of each feature in the decision tree
len(feature_keys)
len(rf.feature_importances_)


for i in range(len(feature_keys)):
    print(feature_keys[i], (20 - len(feature_keys[i]))*'_', round(rf.feature_importances_[i]*100,2),'%')
