#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Sunny Islam, 2017
# example2.py asks for properties and yields properties
# employs random forest regression
# sklearn features many machine learning models

from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import math

# importing the data from beamTest.py

df = pd.read_csv('file.csv', header=None)

# converting to numpy arrays

df = pd.DataFrame.as_matrix(df)

# training data

X = df[:, 0:6]

# target values

y = df[:, 6:]

# scikit mathemagics

max_depth = 30
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    train_size = 4000,
                                                    random_state = 4)
regr = RandomForestRegressor(max_depth=max_depth,
                             random_state = 0)
regr.fit(X_train, y_train, sample_weight=None)

# array of properties for the predictor, choose your desired parameters

test = np.array([
    5,
    10,
    5,
    10,
    5,
    10,
    ])
test = np.transpose(test)

# should compare the multivariate fit with the input properties

j = np.transpose(test)

a = 0
b = 1
c = 2
d = 3
e = 4
f = 5

# area of profile

A = j[a] * j[b] + j[c] * j[d] + j[e] * j[f]

# centroid of profile

y = (j[b] / 2 * j[b] * j[a] + (j[b] + j[d] / 2)
     * j[d] * j[c] + (j[b] + j[d] + j[f] / 2)
     * j[f] * j[c]) / A

# height of profile

h = j[b] + j[d] + j[f]

# I_x, split up in four components I_x1(a,b),
# I_x2(c,d) and I_x3(e,f)

I_x1 = 0.08333 * j[a] * math.pow(j[b], 3) \
    + j[a] * j[b] * math.pow(math.fabs(j[b] / 2
        - y), 2)
I_x2 = 0.08333 * j[c] * math.pow(j[d], 3) \
    + j[c] * j[d] * math.pow(math.fabs(j[b]
        + j[d] / 2 - y), 2)
I_x3 = 0.08333 * j[e] * math.pow(j[f], 3) \
    + j[e] * j[f] * math.pow(math.fabs(j[b]
        + j[d] + j[f] / 2 - y), 2)
I_x = I_x1 + I_x2 + I_x3

# I_y is simple to calculate as the centroid of
# all segments are on the neutral axis

I_y = 0.08333 * (j[b] * math.pow(j[a], 3)
        + j[d] * math.pow(j[c], 3) + j[f]
        * math.pow(j[e], 3))

# create temporary vector m to be merged with the matrix M

m = np.array([
    A,
    y,
    I_x,
    I_y,
    h,
    ])
print('Dimensions of proposed beam profile')
print j
print('Properties of proposed beam profile')
print m
print('Desired properties')
print regr.predict(test)