#RatingPrediction5000
#Using the df5000 data from home.py, this module uses sklearn.ensemble.RandomForestRegressor to weigh traits which determine the IMDB rating of a particular movie
#Long term steps for development of this module include linking back any given data to the name of the movie and to retrieve it from the dataframe
#Created: devongulley1602 2022-07-21
#Last Edit: devongulley1602 2022-07-28

#NOTE: PART 2 NEEDS WORK


import pandas as pd
import datetime as dt
import numpy as np
from itertools import chain
from preprocess5000 import data_5000 #this dataframe includes binary encoding for all genres built into its columns by default
import functools
from sklearn.preprocessing import LabelBinarizer
from collections import Counter
from sklearn.ensemble import RandomForestRegressor as rf #Regressor because we're working with continuous values
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from matplotlib import pyplot as plt
from sklearn.model_selection import validation_curve
from sklearn.preprocessing import MinMaxScaler
#data_5000.columns

#Some further data trimming
#NOTE: There are 997 records with missing budget data which have all been defaulted to $0.00
data_5000 = data_5000[data_5000.budget != 0] #we will not analyse them

data_matrix = data_5000.to_numpy() #for storing all the data retrieved

#Categories relevant for our analysis here
scores = data_matrix[:,16].astype('float64') #data_5000['vote_average'] #IMDB scores are on on the 16th column
budgets = data_matrix[:,0].astype('float64') #budgets are the first column
all_star1 = data_matrix[:,42] #for the names of actors
all_star2 = data_matrix[:,43]
release_dates = pd.to_datetime(data_5000['release_date'], errors='coerce')

#Some date analysis:
release_quarters = np.array(list(map(lambda date: [(date.month-1)//3], release_dates))).astype('int64')
release_years = np.array(list(map(lambda date: [date.year], release_dates))).astype('int64')

#Genres is a matrix with columns binary encoded to:
# {'action', 'adventure', 'fantasy','science fiction', 'crime', 'drama', 'thriller', 'animation', 'family','western', 'comedy', 'romance', 'horror', 'mystery', 'history', 'war','music', 'documentary', 'foreign', 'tv movie'} respectively
#and rows as each specific movie. ie if a movie (row) is of a certain category (column) its entry will be represented by a 1, otherwise 0
genres = data_matrix[:,19:39].astype('int64') #currently all 20 genres are stored in the data_matrix columns 19 to 39

#star1 and star2 are matrices with columns binary encoded to the top 5 primary and secondary stars respectively
topStars1 = [i[0] for i in Counter(all_star1).most_common(5)] #the names of the 5 most common star_one
topStars2 = [i[0] for i in Counter(all_star2).most_common(5)] #the names of the top 5 star_two

star1  = LabelBinarizer().fit(topStars1).transform(all_star1)
star2 = LabelBinarizer().fit(topStars2).transform(all_star2)


#The features that we would like to use to weigh in determining an IMDB score for a given film are currently:
#release_years, release_quarters,budget, the encoded genres, the encoded stars
features = [list(chain(*i)) for i in list(zip([[j] for j in budgets],release_years,release_quarters,genres,star1,star2))] #this line is horrible
feature_keys = list(chain(['budget'],['release_year'],['release_quarter'],list(data_5000.columns[19:39]), list(topStars1),list(topStars2)))

#A dictionary to hold the arrays of features whose index correspond to the same movie
features_dict = {}
for i in range(len(features[0])):
    features_dict[feature_keys[i]] = np.array(features)[:,i]



#print(list(zip(features[0],feature_keys)))

#Based off of df5000 data set what will a particular movie be rated given some properties?

#1. Look at the dataset, include budget, cast, release_date.year and release quarter, determine feature weights using random forest decision tree regression

rf = rf(n_estimators = 1000)

#Splitting the training and testing data
features_train, features_test, scores_train, scores_test = train_test_split(features,scores,test_size = 0.2)

#Training the random forest regression model
rf.fit(features_train, scores_train)
predictions = rf.predict(features_test) #Predictions finalised

#Plotting Actual Scores

def plot_all(model):
    plt.title(f"{model} - Scores By Movie")
    plt.ylabel("Score")
    plt.xlabel("Movie Number in Test Set")
    plt.scatter(range(len(predictions)),scores_test,s=1,c='b',label = 'actual')
    plt.scatter(range(len(predictions)),predictions,s=1,c = 'r',label='predicted')
    plt.legend(loc = 'upper left')

    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    # ax1.scatter(range(len(predictions)),scores_test,s=1,c='r',label = 'actual')#.scatter(x[:4], y[:4], s=10, c='b', marker="s", label='first')
    # ax1.scatter(range(len(predictions)),predictions,s=1,c='b',label='predicted')#.scatter(x[40:],y[40:], s=10, c='r', marker="o", label='second')
    for i in range(len(predictions)):
        ax1.plot([i,i], [predictions[i],scores_test[i]],marker = 'o')

    ax1.set_title(f"{model} - Score Prediction Variation")
    ax1.set_ylabel("Prediction Disparity")
    ax1.set_xlabel("Movie Number in Test Set")
    # plt.legend(loc='upper left')
    plt.show()

    #Some statistics on the efficacy of the regressor
    plt.title(f"{model} - Prediction Error")
    plt.xlabel("Movie Number in Test Set")
    plt.ylabel("Score Variation")
    signed_errors = predictions-scores_test
    errors = abs(predictions-scores_test)
    avg_error = np.average(errors)
    print(f"Scores within {min(errors)} and {max(errors)}.\nPredictions incorrect by {avg_error} points on average.")


    #Visualisation of the efficacy of the regressor
    plt.scatter(range(len(predictions)),errors,c='red')
    plt.show()
plot_all("Random Forest Regressor")

#Error checking to ensure that feature_keys and feature_importances_ have the same length
if(len(feature_keys) != len(rf.feature_importances_)): raise IndexError('The number of feature labels do not match the number of features being evaluated.')

ar = list(zip(feature_keys,rf.feature_importances_))
sorted_importance = np.array(list(reversed(sorted(ar, key=lambda x: float(x[1])))))
#sorted_importance[:,1] = (list(map(lambda value: round(value*100,2),sorted_importance[:,1].astype('float64'))))#having weights as whole number percentages


#For printing the relative importance of each feature in the decision tree
for i in range(len(feature_keys)):
    print(feature_keys[i], (20 - len(feature_keys[i]))*'_', round(rf.feature_importances_[i]*100,2),'%')

sorted_importance
plt.title("Feature Importance - Random Forest Regression")
plt.rcParams.update({'font.size': 10})
plt.barh(sorted_importance[:,0],sorted_importance[:,1].astype('float64'))
#plt.tick_params(axis='x', direction='out')
plt.show()



#2. Put the most important features into the Multi-layer Perceptron Regressor to build a model
mlpr = MLPRegressor(solver= 'lbfgs',hidden_layer_sizes=100,max_iter = 1000,shuffle=True,activation='relu');
scaler = MinMaxScaler(feature_range = (0,10))


#Starting new by again splitting the training and testing data
importantFeatNames = sorted_importance[:,0][0:15]
print(f"The {len(importantFeatNames)} most important features from the decision tree: {importantFeatNames}")
columns = [features_dict[i] for i in importantFeatNames]
features = np.zeros(shape = (len(columns[0]),len(importantFeatNames)))

for i in range(len(importantFeatNames)):#i goes from 0 to 5
    for j in range(len(columns[0])):#j goes through the length of the data
        features[j][i] = np.array(columns[i][j])
features = np.array(features) #so that columns of features and rows can be easily called


features_train, features_test, scores_train, scores_test = train_test_split(features,scores,test_size = 0.2)


mlpr.fit(X=features_train, y=scores_train)

predictions = mlpr.predict(features_test)#[mlpr.predict([features_test[i]]) for i in range(len(features_test))]

for i in range(len(predictions)):
    if predictions[i]>50:
        predictions[i] = 10
    if predictions[i]<0:
        predictions[i] = 0


plot_all("Multi-layer Perceptron Regressor")
