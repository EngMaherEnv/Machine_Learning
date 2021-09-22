import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from RFFeatureSelect import *
from knn import *
from RandomForest import *
from dtree import *
from SVM import *
from Log import *
from sklearn. ensemble import RandomForestClassifier, BaggingClassifier, AdaBoostClassifier, VotingClassifier
ADWARE_DOWGIN = pd.read_csv("ADWARE_DOWGIN.csv") 
RANSOMWARE_CHARG = pd.read_csv("RANSOMWARE_CHARG.csv") 
begin = pd.read_csv("begin.csv") 


#i compined the three data frames in one dataframe then i mixed it up ,
#this will allow me to splite the data to train and test without taking oly one type of data to the test 
frames = [ADWARE_DOWGIN, RANSOMWARE_CHARG,begin]
df = pd.concat(frames)
df = df.sample(frac=1)

 
X = df.iloc[:, :-1].values

X=df.drop(columns=['Flow ID', ' Source IP', ' Source Port',' Destination IP',' Destination Port',' Timestamp',' Protocol',' Label',])
y = df.iloc[:, 84].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)


# calling a selecting function that uses RandomForestClassifier to reduse the number of features to ,
Selected=Select_Features(X_train , y_train , num=30)

# updating my features to use only selected features.

X_train=X_train.iloc[:, Selected]
X_test=X_test.iloc[:, Selected]

# scale the data 
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

Knnclassifier = KNeighborsClassifier(n_neighbors=7)
DTclf = DecisionTreeClassifier()

Knnclassifier.fit(X_train, y_train)
DTclf = DTclf.fit(X_train,y_train)

y_Knnpred = Knnclassifier.predict(X_test)
y_DTpred = DTclf.predict(X_test)

RFmodel = RandomForestClassifier(n_estimators=100)
RFmodel.fit(X_train, y_train)
y_Rfpred = RFmodel.predict(X_test)

print("Accuracy:",metrics.accuracy_score(y_test, y_Rfpred))

logClassifier = LogisticRegression()
logClassifier.fit(X_train, y_train)
    # lOG Classifier predection 
y_logClassifierpredlog = logClassifier.predict(X_test)

from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score

voting_clf = VotingClassifier(estimators=[('KNN', Knnclassifier), ('DTree', DTclf),('RF', RFmodel),('lOG', logClassifier)], voting='hard')
voting_clf.fit(X_train, y_train)
preds = voting_clf.predict(X_test)
acc = accuracy_score(y_test, preds)

from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report, confusion_matrix

print("ACC after feature selection for Knnclassifier:",accuracy_score(y_test, y_Knnpred))
print( "f1_score for Knnclassifier :", f1_score(y_test, y_Knnpred, average="macro"))
print("precision_score for Knnclassifier :",precision_score(y_test, y_Knnpred, average="macro"))
print("recall_score for Knnclassifier:",recall_score(y_test, y_Knnpred, average="macro"))    

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics

cm = metrics.confusion_matrix(y_test, preds)
print(cm)
plt.figure(figsize=(9,9))
sns.heatmap(cm, annot=True, fmt=".3f", linewidths=.5, square = True, cmap = 'Blues_r');
plt.ylabel('Actual label');
plt.xlabel('Predicted label');
all_sample_title = 'Accuracy Score: {0}'.format(acc)
plt.title(all_sample_title, size = 15);
