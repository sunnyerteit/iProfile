#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Sunny Islam
# import math functions

import math
import numpy as np

# n is the number of steps (integer)

n = 5

# i is the maximum value of a dimension (float)

i = 10.0

# j is the sample vector

j = np.arange(i, 0.0, -i / n)

# M is the array of results
# M = np.zeros((10, int(math.pow(6, n) / 2)))

M = np.zeros((1, 10))
count = 0
for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                for e in range(n):
                    for f in range(n):

                        # area of profile

                        A = j[a] * j[b] + j[c] * j[d] + j[e] * j[f]

                        # centroid of profile

                        y = (j[b] / 2 * j[b] * j[a] + (j[b] + j[d] / 2)
                             * j[d] * j[c] + (j[b] + j[d] + j[f] / 2)
                             * j[f] * j[c]) / A

                        # neutral axis

                        y_n = (j[b] + j[d] + j[f]) / 2

                        # I_x, split up in four components I_x1(a,b),
                        # I_x2(c,d) and I_x3(e,f)

                        I_x1 = 0.08333 * j[a] * math.pow(j[b], 3) \
                            + j[a] * j[b] * math.pow(math.fabs(j[b] / 2
                                - y_n), 2)
                        I_x2 = 0.08333 * j[c] * math.pow(j[d], 3) \
                            + j[c] * j[d] * math.pow(math.fabs(j[b]
                                + j[d] / 2 - y_n), 2)
                        I_x3 = 0.08333 * j[e] * math.pow(j[f], 3) \
                            + j[e] * j[f] * math.pow(math.fabs(j[b]
                                + j[d] + j[f] / 2 - y_n), 2)
                        I_x = I_x1 + I_x2 + I_x3

                        # I_y is simple to calculate as the centroid of
                        # all segments are on the neutral axis

                        I_y = 0.08333 * (j[b] * math.pow(j[a], 3)
                                + j[d] * math.pow(j[c], 3) + j[f]
                                * math.pow(j[e], 3))

                        # create temporary vector m to be merged with the matrix M

                        m = np.array([
                            j[a],
                            j[b],
                            j[c],
                            j[d],
                            j[e],
                            j[f],
                            A,
                            y,
                            I_x,
                            I_y,
                            ])
                        M = np.vstack((M, m))

# delete first row

M = np.delete(M, 0, axis=0)

# print matrix M to file.csv

np.savetxt('file.csv', M, delimiter=',')
