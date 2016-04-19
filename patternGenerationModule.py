import binarisationVariables as BV
from excelFileReader import *
from basicPatternGeneration import *
from generateFrequentItemsets import *
import json

def generatePattern():
	#readFile('minimizedSupportSetOutput.xls')
	readFile('minimizedSupportSetAttributeCorrOutput.xls')
	#basicPatternGeneration()
	generateFrequentItemsets()

generatePattern()
