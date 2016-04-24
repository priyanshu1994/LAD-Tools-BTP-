import binarisationVariables as BV

from xlrd import open_workbook

def readFile(fileName):
	BV.items = []
	wb = open_workbook(fileName)
	for sheet in wb.sheets():
		BV.numberOfEntries = sheet.nrows
		BV.numberOfAttributes = sheet.ncols

		rows = []
		for row in range(BV.numberOfEntries):
			values = []
			missing = False
			for col in range(BV.numberOfAttributes):
				value  = (sheet.cell(row,col).value)
				try:
				   value = float((value))
				except ValueError:
					missing = True
				finally:
					values.append(value)
			#print values
			if missing == False:
				BV.items.append(values)
		BV.numberOfEntries = len (BV.items)
	return