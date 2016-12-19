#!/usr/bin/python3

from sklearn.metrics import mean_squared_error
from math import sqrt

import os
import ast

actual = []
predicted =[]
i = 0

with open('movies_testset') as f:
	testset = f.read().splitlines()
	with open('movies_prediction') as g:
        	prediction = g.read().splitlines()
		for line in prediction:#testset:
			splitLine = line.split()
			value = str(splitLine[0])
#			print(value)
			#value = float(value)
			#value = ast.literal_eval(value)
			predicted.append(value)
			splitLine = testset[i].split()
			
			value = str(splitLine[0])
#			value = float(value)
			#value = ast.literal_eval(value)
			actual.append(value)
			i+=1

i = 0

for line in actual:
	try:
		actual[i] = float(line)
	except:
		actual[i] = 0
	i+=1

i = 0
for line in predicted:

	try:
		predicted[i] = float(line)
		if predicted[i]>10:
			predicted[i] = predicted[i]/10000
	except:
		predicted[i] = 0
	i+=1


#print(actual)
#print(predicted)

rms=(sqrt(mean_squared_error(actual, predicted)))	


print(rms)
