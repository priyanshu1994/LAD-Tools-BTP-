import binarisationVariables as BV
from excelFileReader import *
from generateAttributeCutPoints import *
from generateBinaryAttributes import *
import json

def binariseEntries():
	readFile('sample.xls')
	for i in range(BV.numberOfAttributes - 1):
		attributeList = []
		dict = {}
		for j in xrange(BV.numberOfEntries):
			value = (BV.items[j][i], BV.items[j][BV.numberOfAttributes - 1])
			attributeList.append(value)
			dict[value] = 1
		if len (dict) == 2:
			max_key = -1
			for key in dict:
				max_key = max (int(key), max_key)
			cutPoints.append(max_key)
		else:
			attributeList.sort()
			cutPoints = generateCutPoints(attributeList)

		BV.cutPointsList.append(cutPoints)

	fileObj = open("cutPoints.txt","w")	
	json.dump(BV.cutPointsList, fileObj)
	fileObj.close()

	generateBinaryAttributes()

binariseEntries()
