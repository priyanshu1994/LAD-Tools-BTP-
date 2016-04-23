import binarisationVariables as BV
import json
from xlutils.copy import copy
from xlrd import open_workbook
from xlwt import easyxf
import xlsxwriter

def readExcelFile (fileName):
	items = []
	wb = open_workbook(fileName)
	for sheet in wb.sheets():
		numberOfEntries = sheet.nrows
		numberOfAttributes = sheet.ncols

		rows = []
		for row in range(numberOfEntries):
			values = []
			for col in range(numberOfAttributes):
				value  = (sheet.cell(row,col).value)
				try:
				   value = float((value))
				except ValueError:
					pass #Default value not defined
				finally:
					values.append(value)
			items.append(values)

	print items
	return items

def writeExcelFile (finalItems):
	workbook = xlsxwriter.Workbook('convertedTestData.xls')
	worksheet = workbook.add_worksheet()

	row = 0
	for item in finalItems:
		column = 0
		for value in item:
			worksheet.write(row, column, value)
			column = column + 1
		row = row + 1
	workbook.close()

def binarizeInputData (fileName):
	items = readExcelFile(fileName)

	binarisedInputs = []
	cutPoints = []
	with open("cutPoints.txt") as fileObj: cutPoints = json.load(fileObj)

	for item in items:
		binarisedInput = []
		i = 0
		for value in item:
			for cutPoint in cutPoints[i]:
				if cutPoint > value:
					binarisedInput.append(0)
				else:
					binarisedInput.append(1) 
			i = i + 1
		binarisedInputs.append(binarisedInput)
	return binarisedInputs

def reduceAttributeUsingAttributesCorr(fileName):
	binarisedInput = binarizeInputData(fileName)

	with open("attributeCorrelationList.txt") as fileObj: correlationCoef = json.load(fileObj)
	with open("correlatedAttributesList.txt") as fileObj: correlatedAttributes = json.load(fileObj)

	finalItems = []

	for item in binarisedInput:
		finalItem = []
		for attributes in correlatedAttributes:
			wt = 0
			for attribute in attributes:
				if item[attribute] == 0:
					wt = wt - correlationCoef[attribute][-1]
				else:
					wt = wt + correlationCoef[attribute][-1]
			if wt >= 0:
				finalItem.append(1)
			else:
				finalItem.append(0)
		finalItems.append(finalItem)
	return finalItems

def minimiseByAttriResultCorr(fileName):
	inputData = readExcelFile(fileName)

	reducedCutPoints = []
	with open("reducedCutpoints.txt") as fileObj: reducedCutPoints = json.load(fileObj)

	finalItems = []
	i = 0
	for item in inputData:
		finalItem = []
		for value in item:
			for cutPoint in reducedCutpoints[i]:
				if value < cutPoint:
					finalItem.append(0)
				else:
					finalItem.append(1)
		finalItems.append(finalItem)
	return finalItems

finalItems = reduceAttributeUsingAttributesCorr ('test.xls')
#finalItems = minimiseByAttriResultCorr (fileName)
writeExcelFile (finalItems)