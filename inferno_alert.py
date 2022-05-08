# -*- coding: utf-8 -*-
"""Inferno_Alert.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19-OskI_DVh5UurnNckSyui6bKyBi9B65

# Forest Fire prediction using Machine Learning

## Importing the Libraries
"""



# Commented out IPython magic to ensure Python compatibility.
import datetime as dt
from fileinput import filename
from statistics import mode

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import torch
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import deep_tabular_augmentation as dta
import warnings; warnings.simplefilter('ignore')
# %matplotlib inline 
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
import time
from sklearn.metrics import f1_score

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

DATA_PATH = 'forest_fire.csv'
forest_fire = pd.read_csv(DATA_PATH)



forest_fire.head()

"""Data Exploration"""

forest_fire.shape

forest_fire.columns

"""Checking if there are any null values

"""

forest_fire.isnull().sum()

forest_fire.describe()

#Extras 
plt.figure(figsize=(10, 10))
sns.heatmap(forest_fire.corr(),annot=True,cmap='viridis',linewidths=.5)

forest_fire['class'].value_counts()

"""# Data Cleaning

Removal of unwanted observation

Dropping of the columns which are not useful.
"""

forest_fire.drop(['FFMC','DMC','DC','rain','temp','RH','wind'], axis=1, inplace=True)

forest_fire.columns
forest_fire.head()

"""Fixing Structural Errors"""

forest_fire.describe()

"""Handling Missing Data"""

#There is no missing data in this Dataset
forest_fire.isnull().sum()

data = forest_fire.values



forest_fire = forest_fire[~(forest_fire['ISI']>18)]
forest_fire = forest_fire[~(forest_fire['BUI']>60)]
forest_fire = forest_fire[~(forest_fire['FWI']>23)]



"""Preprocessing

We need to encode the text data such as Month and Class in some numeric form so we can spli the data into training and testing data.
"""

def encoding(forest_fire, column, ordering):
  forest_fire = forest_fire.copy()
  forest_fire[column] = forest_fire[column].apply(lambda y: ordering.index(y)) 
  return forest_fire

#To check all the unique months in the Month column 
forest_fire['month'].unique()

#To check all the unique class in the Class column
forest_fire['class'].unique()

forest_fire

def preprocess(forest_fire, type):
  forest_fire = forest_fire.copy()
  forest_fire = encoding(forest_fire, column = 'month', ordering = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'])
  forest_fire = encoding(forest_fire, column = 'class', ordering = ['fire','not fire'])
  if type == 'Regression':
    Y = forest_fire['class']
  elif type == 'Classification':
    Y = forest_fire['class']
  X = forest_fire.drop('class', axis = 1)

  X_train, X_test, Y_train, Y_test = train_test_split(X,Y,train_size = 0.80, shuffle = True, random_state = 1)

  scaler=StandardScaler()
  scaler.fit(X_train)

  X_train = pd.DataFrame(scaler.transform(X_train),columns = X.columns)
  X_test = pd.DataFrame(scaler.transform(X_test),columns = X.columns)

  return X_train, X_test, Y_train, Y_test, forest_fire

"""Splitting & Testing model"""

X_train, X_test, Y_train, Y_test, forest_fire_new = preprocess(forest_fire, type = 'Regression')

forest_fire_new

X_train.head()

X_test.head()

Y_train

Y_test.head()

df_ = forest_fire_new[forest_fire_new['class']==1]
df_ = df_.drop(['class'], axis=1)

X_train1, X_test1 = train_test_split(df_, test_size=0.1, random_state=42)

x_scaler = StandardScaler()

X_train_scaled = x_scaler.fit_transform(X_train1)

X_test_scaled = x_scaler.transform(X_test1)




regr = RandomForestRegressor(max_depth=2, random_state=0, n_estimators=100)
regr.fit(X_train, Y_train)

regr.score(X_test, Y_test)

from sklearn import neighbors
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(X_train, Y_train)

knn.score(X_test,Y_test)

# from sklearn.datasets import load_iris
# from sklearn.linear_model import LogisticRegression

# classifier = LogisticRegression()
# classifier.fit(X_train, Y_train)

# classifier.score(X_test,Y_test)

classifiers = [
    DecisionTreeClassifier(),
    RandomForestClassifier(max_depth=2, random_state=0),
    LogisticRegression(random_state=0),
    SVC(gamma='auto'),
    GaussianNB(),
    KNeighborsClassifier(n_neighbors=3)

]

names = ["Decision Tree", "Random Forest", "Logistic Regression", "Support Vector Machines", "Naive Bayes", "k Nearest Neighbors"]

from prettytable import PrettyTable
x = PrettyTable()
x.field_names = ["Algorithm", "Accuracy", "f1-score"]

import pickle
max_score = 0.0
max_class = ''
# iterate over classifiers
for name, clf in zip(names, classifiers):
    start_time = time.time()
    clf.fit(X_train, Y_train)
    score = 100.0 * clf.score(X_test, Y_test)
    print('Classifier = %s, Score (test, accuracy) = %.2f,' %(name, score), 'Training time = %.2f seconds' % (time.time() - start_time))
    y_pred = clf.predict(X_test)

    score_f1 = f1_score(Y_test, y_pred, average='micro')
    
    x.add_row([name, round(score, 4), round(score_f1, 4)])
    cm = confusion_matrix(Y_test, y_pred, labels=clf.classes_)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=clf.classes_)
    disp.plot()
    filename = 'model.pkl'
    pickle.dump(clf, open(filename, 'wb'))
    filename = 'model.pkl'
    model = pickle.load(open(filename,'rb'))
    
   
    if score > max_score:
        clf_best = clf
        max_score = score
        max_class = name

print(x)

print('Best --> Classifier = %s, Score (test, accuracy) = %.2f' %(max_class, max_score))