from xlrd import open_workbook

numberOfEntries = 0
numberOfAttribute = 0
items = []

def readFile():
	wb = open_workbook('sample.xls')
	for sheet in wb.sheets():
		numberOfEntries = sheet.nrows
		numberOfAttribute = sheet.ncols

		rows = []
		for row in range(numberOfEntries):
			values = []
			for col in range(numberOfAttribute):
				value  = (sheet.cell(row,col).value)
				try:
				   value = float((value))
				except ValueError:
					pass #Default value not defined
				finally:
					values.append(value)
			#print values
			items.append(values)

	return (items, numberOfAttribute, numberOfEntries)

(items, numberOfAttribute, numberOfEntries) = readFile()

for i in xrange(numberOfEntries):
	print(items[i])