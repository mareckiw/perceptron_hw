import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
import joblib
# from model import Perceptron
from sklearn.linear_model import Perceptron

#loading the standard dataset
iris = load_iris()
#create df to work on dataset
df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                  columns=iris['feature_names'] + ['target'])
#define X and y (input parameters and target var)
X, y = df.iloc[:100, [0, 2]].values, df.iloc[:100, 4]

#data transformations
def a(x):
    if x == 0:
        return -1
    else:
        return 1

y = y.map(a)

#train model
model = Perceptron()
#fit model
model.fit(X, y)
#save model
dump(model, './Perceptron.joblib')