#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Sunny Islam, 2017
# sklearn features many machine learning models

from sklearn import linear_model
import pandas as pd
import numpy as np

# importing the data from beamTest.py

df = pd.read_csv('file.csv', header=None)

# converting to numpy arrays

df = pd.DataFrame.as_matrix(df)

# training data

X = df[:, 0:6]

# target values

y = df[:, 6:]

# scikit mathemagics

regr = linear_model.LinearRegression()
regr.fit(X, y, sample_weight=None)

# array of dimensions for the predictor

test = np.array([
    5,
    10,
    5,
    10,
    5,
    10,
    ])
test = np.transpose(test)
print regr.predict(test)
