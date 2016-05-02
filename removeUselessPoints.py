import binarisationVariables as BV
import json

def removeUselessPoints():
	with open("cutPoints.txt") as fileObj: cutPointsList = json.load(fileObj)

	attributeNum = 0
	uselessPointsNum = 0
	uselessPointsSize = len(BV.uselessPoints)
	tempCutPointsList = []
	markedList = []

	for cutPoints in cutPointsList:
		marked = []
		for point in cutPoints:
			if uselessPointsNum < uselessPointsSize and attributeNum == BV.uselessPoints[uselessPointsNum]:
				marked.append(1)
				uselessPointsNum = uselessPointsNum + 1
			else:
				marked.append(0)
			attributeNum = attributeNum + 1
		markedList.append(marked)

	cutpointRow = 0
	i = 0
	for marked in markedList:
		vec = []
		cutpointCol = 0
		for var in marked:
			i = i + 1
			if var == 0:
				vec.append(cutPointsList[cutpointRow][cutpointCol])
			cutpointCol = cutpointCol + 1
		cutpointRow = cutpointRow + 1

		tempCutPointsList.append(vec)

	cutPointsList = tempCutPointsList

	fileObj = open("reducedCutpoints.txt","w")	
	json.dump(cutPointsList,fileObj)
	fileObj.close()