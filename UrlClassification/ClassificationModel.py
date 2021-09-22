# -*- coding: utf-8 -*-
"""
Created on Fri May 28 10:39:28 2021

@author: STC
"""



import mimetypes
from deep_translator import GoogleTranslator
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn. ensemble import RandomForestClassifier, BaggingClassifier, AdaBoostClassifier, VotingClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics
import pickle


data = pd.read_csv("input.csv") 




X=data[[ 'otherWebsiteLink', 'follow_allowed', 'isFileLink','isBaseOnly','containsNOfollowKeyword','urlLength','titleLength','nOfDdigits','nOfForwardSlash','nOfDot','nOfEqual','nOfHash']]  # Features
y=data['isNews']  # Labels

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) # 70% training and 30% te
#Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=100)

#Train the model using the training sets y_pred=clf.predict(X_test)
h=clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)

from sklearn import metrics
# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))


from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))



# save the model to disk
filename = 'urlClassification_model.sav'
pickle.dump(clf, open(filename, 'wb'))

# some time later...

# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, y_test)
print(result)


  

tryInput = pd.DataFrame(columns = [ 'otherWebsiteLink', 'follow_allowed', 'isFileLink','isBaseOnly','containsNOfollowKeyword','urlLength','titleLength','nOfDdigits','nOfForwardSlash','nOfDot','nOfEqual','nOfHash'])


tryInput = tryInput.append({'otherWebsiteLink' :True, 'follow_allowed':False,'isFileLink':False, 'isBaseOnly' : False, 'containsNOfollowKeyword' : False, 'urlLength' : 95, 'titleLength' : 135, 'nOfDdigits' : 0, 'nOfForwardSlash' : 5, 'nOfDot' : 2, 'nOfEqual' : 0, 'nOfHash' : 1,}, 
                ignore_index = True)


resultOfPrediction=loaded_model.predict(tryInput)
print(resultOfPrediction[0])
