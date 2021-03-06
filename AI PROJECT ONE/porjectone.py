import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
dataset_url = 'http://mlr.cs.umass.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
data = pd.read_csv(dataset_url)
data = pd.read_csv(dataset_url, sep=';')

 
#print data.head()
#print data.shape
#print data.describe()
y = data.quality
X = data.drop('quality', axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2, 
                                                    random_state=123, 
                                                    stratify=y)
scaler = preprocessing.StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
 
#print X_train_scaled.mean(axis=0)
X_test_scaled = scaler.transform(X_test)
 
print X_test_scaled.mean(axis=0)

print X_test_scaled.std(axis=0)

