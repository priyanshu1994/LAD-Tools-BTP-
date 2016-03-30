import binarisationVariables as BV
from xlutils.copy import copy
from xlrd import open_workbook
from xlwt import easyxf

def generateBinaryAttributes():
	readWorkbook = open_workbook('binarizedOutput.xls')
	workbook = copy(readWorkbook)
	worksheet = workbook.get_sheet(0)
	row = 0
	column = 0
	temp = 0
	for item in BV.items:
		i = 0
		column = 0
		for attribute in item:
			if i == BV.numberOfAttributes - 1:
				worksheet.write(row, column, attribute)
				continue
			for point in BV.cutPointsList[i]:
				if attribute < point:
					temp = 0
				else:
					temp = 1
				worksheet.write(row, column, temp)
				column = column + 1
			i = i + 1
		row = row + 1
	workbook.save('binarizedOutput.xls')