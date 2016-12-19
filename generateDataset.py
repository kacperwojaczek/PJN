#!/usr/bin/python

import os

output = open('movies_dataset', 'w+')
output2 = open('movies_testset', 'w+')

i = 0

for filename in os.listdir('files/'):
	
	if i > 430:
		output = output2

	with open('files/'+filename) as f:
		lines = f.read().splitlines() 
	if len(lines[2:]) > 0:
		output.write(lines[1] + " '" + lines[0].replace(" ","") + ' | length:' + str(len(lines[2:])) + '\n')

	i += 1
	
output.close()
	
		
		
