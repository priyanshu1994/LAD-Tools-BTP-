import binarisationVariables as BV
import json

def removeUselessPoints():
	with open("cutPoints.txt") as fileObj: cutPointsList = json.load(fileObj)
	attributeNum = 0
	uselessPointsNum = 0
	cutpointRow = 0
	cutpointCol = 0
	uselessPointsSize = len(BV.uselessPoints)
	for cutPoints in cutPointsList:
		if uselessPointsNum == uselessPointsSize:
			break
		if attributeNum == BV.numberOfAttributes - 1:
			continue
		for point in cutPoints:
			if cutpointCol == len(cutPointsList[cutpointRow]):
				break
			if attributeNum == BV.uselessPoints[uselessPointsNum]:
				cutPointsList[cutpointRow].remove(cutPointsList[cutpointRow][cutpointCol])
				uselessPointsNum = uselessPointsNum + 1
				cutpointCol = cutpointCol - 1
			cutpointCol = cutpointCol + 1
			attributeNum = attributeNum + 1
		cutpointRow = cutpointRow + 1
	fileObj = open("reducedCutpoints.txt","w")	
	json.dump(cutPointsList,fileObj)
	fileObj.close()