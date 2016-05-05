import binarisationVariables as BV
from excelFileReader import *
from calcSimilarity import *
from xlutils.copy import copy
from xlrd import open_workbook
from xlwt import easyxf
import json
import xlsxwriter

def testInstance():
	readFile("convertedTestData.xls")
	
	workbook = xlsxwriter.Workbook('output.xls')
	worksheet = workbook.add_worksheet()
	output = []
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
			if value & int(key) == int(key):
				pos = True
		for key in negativeFrequentItemsets:
			if value & int(key) == int(key):
				neg = True
		if pos == True and neg == False:
			output.append(1)
			worksheet.write(row, 0, 1)
			# print "Pos\n"
		elif pos == False and neg == True:
			output.append(0)
			worksheet.write(row, 0, 0)
			# print "Neg\n"
		else:
			maxPos = -1
			maxNeg = -1
			for key, times in positiveFrequentItemsets.iteritems():
				temp = value
				similarity = calcSimilarity(key,value)
				closeness = similarity * times/numOfPosPatterns
				# print "pos"
				# print similarity
				# print closeness
				# print "Positive"
				# print closeness
				# print "\n\n"
				if(closeness > maxPos):
					maxPos = closeness
			value = temp
			for key, times in negativeFrequentItemsets.iteritems():
				similarity = calcSimilarity(key,value)
				closeness = similarity * times/numOfNegPatterns
				# print "neg"
				# print similarity
				# print closeness
				if(closeness > maxNeg):
					maxNeg = closeness
			# print item
			# print value
			# # print maxNeg
			# # print maxPos
			# print "\n"
			if maxNeg > maxPos:
				output.append(0)
				worksheet.write(row, 0, 0)
			else:
				output.append(1)
				worksheet.write(row, 0, 1)
		row = row + 1
	workbook.close()
	json.dump(output, open("labels.txt","w"))

testInstance()
