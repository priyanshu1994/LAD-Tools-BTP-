import binarisationVariables as BV
from excelFileReader import *
from minimizeByResultCovariance import *
from minimizeResultByAttributeCorrelation import *
import sys

def minimizeSupportSet():
	readFile('binarisedOutput.xls')
	if int(sys.argv[1]) == 1:	
		minimizeByResultCovariance(float(sys.argv[2]) - 0.4)
	else:
		minimizeResultByAttributeCorrelation(float(sys.argv[2]))

minimizeSupportSet()
