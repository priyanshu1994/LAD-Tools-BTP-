import binarisationVariables as BV
from excelFileReader import *
from xlutils.copy import copy
from xlrd import open_workbook
from xlwt import easyxf
import json

def calcSimilarity(key, value):
	key = int(key)
	with open("finalCorrelationValue.txt") as fileObj: correlationValues = json.load(fileObj)
	num = 0
	den = 0
	idx = len(correlationValues)
	idx = idx - 1
	while key != 0 and value != 0:
		if key%2 != 0:
			if key%2 == value%2:
				num += correlationValues[idx]
			else:
				num -= correlationValues[idx]
			den += correlationValues[idx]
		elif (key/2)%2 != 0:
			if (key/2)%2 == (value/2)%2:
				num += correlationValues[idx]
			else:
				num -= correlationValues[idx]
			den += correlationValues[idx]
		idx = idx-1
		key = key/4
		value = value/4
	return num * 1.0 / den