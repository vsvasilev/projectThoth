#! /usr/bin/env python3
#arrayManipulation.py includes functions for manipulating list of lists (arrays)

def transpondArray(inputArray):
	transArray = [[]]
	for i in range(len(inputArray)):
		for j in range(len(inputArray[i])):
			transArray[j][i] = inputArray[i][j]
	return transArray

testArray = [['a', 'b', 'c'] , [1 , 2 , 3] , ['t1', 't2', 't3'], ['z1', 'z2', 'z3']]

print(testArray)

print(transpondArray(testArray))