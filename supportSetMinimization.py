import binarisationVariables as BV
from excelFileReader import *
from minimizeByResultCovariance import *
from minimizeResultByAttributeCorrelation import *
import sys

def minimizeSupportSet():
	readFile('binarisedOutput.xls')
	#minimizeByResultCovariance(0.1)
	minimizeResultByAttributeCorrelation(float(sys.argv[1]))

minimizeSupportSet()