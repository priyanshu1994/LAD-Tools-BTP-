import binarisationVariables as BV
from excelFileReader import *
from xlutils.copy import copy
from xlrd import open_workbook
from xlwt import easyxf
import json

def testInstance():
	dict = json.load(open("patterns.txt"))
	dict = {float(key) : value for (key, value) in dict.items()}
	readFile("testData.xls")
	with open("reducedCutpoints.txt") as fileObj: cutPointsList = json.load(fileObj)
	readWorkbook = open_workbook('Output.xls')
	workbook = copy(readWorkbook)
	worksheet = workbook.get_sheet(0)
	row = 0
	column = 0
	temp = 0
	value = 0
	print dict
	for item in BV.items:
		i = 0
		column = 0
		value = 0
		for attribute in item:
			for point in cutPointsList[i]:
				if attribute < point:
					temp = 0
				else:
					temp = 1
				value = value*2 + temp
				column = column + 1
			i = i + 1
		if value in dict:
			temp = 1
		else:
			temp = 0
		print value
		worksheet.write(row,0,temp)
		row = row + 1
	workbook.save('Output.xls')

testInstance()