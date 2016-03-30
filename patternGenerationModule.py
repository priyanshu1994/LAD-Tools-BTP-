import binarisationVariables as BV
from excelFileReader import *
import json

def convertBinaryToInt(list):
	val = 0
	for attribute in list:
		val = val * 2 + attribute
	val = val - 1
	val = val / 2
	return val

def generatePattern():
	readFile('minimizedSupportSetOutput.xls')
	
	dict = {}
	i = 0
	for item in BV.items:
		if item[BV.numberOfAttributes - 1] == 1:
			val = convertBinaryToInt(item)
			dict[val] = 1
#	print dict
	json.dump(dict, open("patterns.txt","w"))

generatePattern()
