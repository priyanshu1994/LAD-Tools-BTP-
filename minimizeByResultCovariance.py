import binarisationVariables as BV
import numpy as np
from xlutils.copy import copy
from xlrd import open_workbook
from xlwt import easyxf
import json

def createMinimizedSupportSetOutput(uselessPoints):
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
	i = 0
	while i < BV.numberOfAttributes - 1:
		# y = [[row[i] for row in BV.items],[row[BV.numberOfAttributes-1] for row in BV.items]]
		# print [row[i] for row in BV.items]
		# print[row[BV.numberOfAttributes-1] for row in BV.items]
		# print np.corrcoef([row[i] for row in BV.items],[row[BV.numberOfAttributes-1] for row in BV.items])
		correlationCoef = abs((np.corrcoef([row[i] for row in BV.items],[row[BV.numberOfAttributes-1] for row in BV.items]))[0][1])
		#print correlationCoef
		if correlationCoef < threshold:
			uselessPoints.append(i)
		i = i + 1
	BV.uselessPoints = uselessPoints
	createMinimizedSupportSetOutput(uselessPoints)
#	print BV.uselessPoints
