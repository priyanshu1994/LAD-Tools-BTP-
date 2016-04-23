import binarisationVariables as BV
import numpy as np
from xlutils.copy import copy
from xlrd import open_workbook
from xlwt import easyxf
import json

def createMinimisedSupportSetOutput(uselessPoints):
	readWorkbook = open_workbook('minimizedSupportSetOutput.xls')
	workbook = copy(readWorkbook)
	worksheet = workbook.get_sheet(0)
	row = 0
	column = 0
	temp = 0
	uselessPointsSize = len(uselessPoints)
	for item in BV.items:
		i = 0
		column = 0
		j = 0
		for attribute in item:
			if i == BV.numberOfAttributes - 1:
				worksheet.write(row, column - j, attribute)
				continue
			if j < uselessPointsSize and uselessPoints[j] == i:
				j = j + 1
			elif j == uselessPointsSize:
				worksheet.write(row, column - j, attribute)
			else:
				worksheet.write(row, column - j, attribute)
			column = column + 1
			i = i + 1
		row = row + 1
	workbook.save('minimizedSupportSetOutput.xls')

def minimizeByResultCovariance(threshold):
	uselessPoints = []
	correlation = []
	i = 0
	while i < BV.numberOfAttributes - 1:
		correlationCoef = abs((np.corrcoef([row[i] for row in BV.items],[row[BV.numberOfAttributes-1] for row in BV.items]))[0][1])
		if correlationCoef < threshold:
			uselessPoints.append(i)
		else:
			correlation.append(correlationCoef)
		i = i + 1
	BV.uselessPoints = uselessPoints
	createMinimisedSupportSetOutput(uselessPoints)

	fileObj = open("finalCorrelationValue.txt","w")	
	json.dump(correlation, fileObj)
	fileObj.close()