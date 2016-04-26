import binarisationVariables as BV
from excelFileReader import *
from basicPatternGeneration import *
from generateFrequentItemsets import *
import sys
import json

def generatePattern():
	readFile('minimizedSupportSetOutput.xls')
	#basicPatternGeneration()
	generateFrequentItemsets(float(sys.argv[1]))
	f =  open("accuracy","r+")
	accuracy = f.read()
	f.seek(0)
	accuracy = accuracy + " MinSup = " + str(sys.argv[1]) + " "
	f.write(accuracy)

generatePattern()