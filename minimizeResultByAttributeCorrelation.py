import binarisationVariables as BV
import numpy as np
from xlutils.copy import copy
from xlrd import open_workbook
from xlwt import easyxf
import json

reached = []
correlationCoef = []

def dfs(head, threshold):
	ans = []
	global correlationCoef
	for i in range(BV.numberOfAttributes - 1):
		if abs(correlationCoef[head][i]) >= threshold and reached[i] == 0:
			reached[i] = 1
			ans  = ans + [i] + dfs(i, threshold)
	return ans

def getSetsOfCorrelatedAttributes(threshold):
	correlatedAttributesList = []
	global reached
	for i in range(BV.numberOfAttributes - 1):
		reached.append(0)
	for i in range(BV.numberOfAttributes - 1):
		if reached[i] == 0:
			reached[i] = 1
			correlatedAttributes = [i] + dfs(i, threshold)
			correlatedAttributesList.append(correlatedAttributes)
	return correlatedAttributesList


def createNewAttributes(correlatedAttributes):
	finalItems = []
	global correlationCoef
	for instance in BV.items:
		finalInstance = []
		for attributes in correlatedAttributes:
			wt = 0
			for attribute in attributes:
				if instance[attribute] == 0:
					wt = wt - correlationCoef[attribute][BV.numberOfAttributes - 1]
				else:
					wt = wt + correlationCoef[attribute][BV.numberOfAttributes - 1]
			if wt >= 0:
				finalInstance.append(1)
			else:
				finalInstance.append(0)
		finalInstance.append(instance[BV.numberOfAttributes - 1])
		finalItems.append(finalInstance)

	correlation = []
	i = 0
	numberOfAttributes = len(correlatedAttributes)
	while i < numberOfAttributes:
		correlationCoef = abs((np.corrcoef([row[i] for row in finalItems],[row[numberOfAttributes] for row in finalItems]))[0][1])
		correlation.append(correlationCoef)
		i = i + 1

	fileObj = open("finalCorrelationValue.txt","w")	
	json.dump(correlation, fileObj)
	fileObj.close()

	return finalItems

def createMinimizedSupportSetAttributeCorrOutput(newAttributesList, numberOfAttributes):
	readWorkbook = open_workbook('minimizedSupportSetAttributeCorrOutput.xls')
	workbook = copy(readWorkbook)
	worksheet = workbook.get_sheet(0)
	row = 0
	for item in newAttributesList:
		column = 0
		for attribute in item:
				worksheet.write(row, column, attribute)
				column = column + 1
		row = row + 1
	workbook.save('minimizedSupportSetAttributeCorrOutput.xls')

def minimizeResultByAttributeCorrelation(threshold):
	uselessPoints = []
	i = 0
	data = []
	while i < BV.numberOfAttributes:
		# y = [[row[i] for row in BV.items],[row[BV.numberOfAttributes-1] for row in BV.items]]
		# print [row[i] for row in BV.items]
		# print[row[BV.numberOfAttributes-1] for row in BV.items]
		# print np.corrcoef([row[i] for row in BV.items],[row[BV.numberOfAttributes-1] for row in BV.items])
		data.append([row[i] for row in BV.items])
		i = i + 1

	global correlationCoef
	correlationCoef = np.corrcoef(data)

	correlatedAttributes = getSetsOfCorrelatedAttributes(threshold)

	# print type(correlationCoef)

	json.dump(correlatedAttributes, open("correlatedAttributesList.txt","w"))
	json.dump(correlationCoef.tolist(), open("attributeCorrelationList.txt","w"))

	newAttributesList = createNewAttributes(correlatedAttributes)

	createMinimizedSupportSetAttributeCorrOutput(newAttributesList, len(correlatedAttributes) + 1)