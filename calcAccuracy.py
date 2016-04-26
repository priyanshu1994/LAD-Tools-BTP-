import binarisationVariables as BV
from excelFileReader import *
import json

def calcAccuracy():
	output = []
	with open("labels.txt") as fileObj: output = json.load(fileObj)
	readFile("results.xls")
	i = 0
	count = 0
	for item in BV.items:
		if item[0] == output[i]:
			count = count + 1
		i = i + 1
	f =  open("accuracy","r+")
	accuracy = f.read()
	f.seek(0)
	accuracy = accuracy + "Accuracy = " + str(count*100.0/BV.numberOfEntries) + "\n"
	f.write(accuracy)

calcAccuracy()