
import binarisationVariables as BV
from excelFileReader import *
from minimizeByResultCovariance import *
from minimizeResultByAttributeCorrelation import *

def minimizeSupportSet():
	readFile('binarizedOutput.xls')
	minimizeByResultCovariance(0.1)
	#minimizeResultByAttributeCorrelation(0.62)

minimizeSupportSet()