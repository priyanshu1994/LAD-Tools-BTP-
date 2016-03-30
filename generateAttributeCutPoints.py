import binarisationVariables as BV

def generateCutPoints(list):
	dict = {}
	cutPoints = []
	i = 0
	while i < BV.numberOfEntries:
		dict[list[i][0]] = [0,0]
		temp = list[i][0]
		while i < BV.numberOfEntries and list[i][0] == temp:
			dict[list[i][0]][int(list[i][1])] = dict[list[i][0]][int(list[i][1])] + 1
			i = i + 1
	# print dict
	curr = 1 if dict[list[0][0]][0] < dict[list[0][0]][1] else (0 if dict[list[0][0]][1] < dict[list[0][0]][0] else -1)
	prev = 0
	for i in dict.iterkeys():
		if i == list[0][0]:
			prev = list[0][0]
		else:
			if curr == 1 and dict[i][1] < dict[i][0]:
				cutPoints.append((prev + i) / 2.0)
				curr = 0
			elif curr == 0 and dict[i][1] > dict[i][0]:
				cutPoints.append((prev + i) / 2.0)
				curr = 1
			elif curr == -1 and dict[i][1] > dict[i][0]:
				curr = 1
			elif curr == -1 and dict[i][1] < dict[i][0]:
				curr = 0
			prev = i
		# print prev
		# print curr
		# print dict[i][1]
		# print dict[i][0]

	return cutPoints