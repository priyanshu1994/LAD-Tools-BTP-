import binarisationVariables as BV
from excelFileReader import *
from generateAttributeCutPoints import *
from generateBinaryAttributes import *
import json

def binariseEntries():
	readFile('sample.xls')
	
	for i in range(BV.numberOfAttributes - 1):
		attributeList = []
		
		for j in xrange(BV.numberOfEntries):
			value = (BV.items[j][i], BV.items[j][BV.numberOfAttributes - 1])
			attributeList.append(value)
		
		attributeList.sort()
		
		cutPoints = generateCutPoints(attributeList)
		# print cutPoints
		BV.cutPointsList.append(cutPoints)

	# print BV.cutPointsList
	fileObj = open("cutPoints.txt","w")	
	json.dump(BV.cutPointsList,fileObj)
	fileObj.close()
	generateBinaryAttributes()

binariseEntries()