import binarisationVariables as BV
from excelFileReader import *
from minimizeByResultCovariance import *
from removeUselessPoints import *

def minimizeSupportSet():
	readFile('binarizedOutput.xls')
	minimizeByResultCovariance(0.3)
	removeUselessPoints()

minimizeSupportSet()