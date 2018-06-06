from sklearn.neural_network import MLPClassifier as MLPC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler  
from sklearn.datasets import load_breast_cancer

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = load_breast_cancer()

data.keys()

data['data'].shape;

X = data['data']
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y)

scaler = StandardScaler()

scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

clf = MLPC(hidden_layer_sizes=(100, 100, 100), max_iter=1000)

clf.fit(X_train, y_train)

predictions = clf.predict(X_test)

confusion_m = pd.DataFrame(confusion_matrix(y_test,predictions), columns=['Benigno', 'Maligno'], index=['Benigno','Maligno'])
plt.show(sns.heatmap(confusion_m, annot=True, fmt='g')) 
