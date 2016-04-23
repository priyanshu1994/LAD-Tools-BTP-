import binarisationVariables as BV
from excelFileReader import *
from calcSimilarity import *
from xlutils.copy import copy
from xlrd import open_workbook
from xlwt import easyxf
import json
import xlsxwriter

def testInstance():
	dict = json.load(open("patterns.txt"))
	dict = {float(key) : value for (key, value) in dict.items()}
	readFile("convertedTestData.xls")
	
	workbook = xlsxwriter.Workbook('Output.xls')
	worksheet = workbook.add_worksheet()
	
	row = 0
	temp = 0
	with open("positiveFrequentItemsets.txt") as fileObj: positiveFrequentItemsets = json.load(fileObj)
	with open("negativeFrequentItemsets.txt") as fileObj: negativeFrequentItemsets = json.load(fileObj)
#	print dict
	with open("numOfPosResults.txt") as fileObj: numOfPosPatterns = json.load(fileObj)
	with open("numOfNegResults.txt") as fileObj: numOfNegPatterns = json.load(fileObj)
	for item in BV.items:
		value = 0
		count = 0
		pos = False
		neg = False
		for attribute in item:
			if attribute == 0:
				value = value + 2**count
			else:
				value = value + 2**(count+1)
			count = count + 2
		for key in positiveFrequentItemsets:
			if value & int(key) == key:
				pos = True
		for key in negativeFrequentItemsets:
			if value & int(key) == key:
				neg = True
		if pos == True and neg == False:
			worksheet.write(row, 0, 1)
		elif pos == False and neg == True:
			worksheet.write(row, 0, 0)
		else:
			maxPos = -1
			maxNeg = -1
			for key, times in positiveFrequentItemsets.iteritems():
				similarity = calcSimilarity(key,value)
				closeness = similarity * times/numOfPosPatterns
				if(closeness > maxPos):
					maxPos = closeness
			for key, times in negativeFrequentItemsets.iteritems():
				similarity = calcSimilarity(key,value)
				closeness = similarity * times/numOfNegPatterns
				if(closeness > maxNeg):
					maxNeg = closeness
			if maxNeg > maxPos:
				worksheet.write(row, 0, 0)
			else:
				worksheet.write(row, 0, 1)
		row = row + 1
	workbook.close()

testInstance()