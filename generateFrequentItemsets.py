import binarisationVariables as BV
from fp_growth import find_frequent_itemsets
from excelFileReader import *
import json

def generateFrequentItemsets():
	# print BV.items
	minsup = 1
	positiveTransactions = []
	negativeTransactions = []
	positiveFrequentItemsets = []
	negativeFrequentItemsets = []
	positiveSupports = []
	negativeSupports = []
	for item in BV.items:
		transaction = []
		count = 0
		if item[-1] == 1:
			for attribute in item[:-1]:
				if attribute == 0.0:
					transaction.append(count * 2)
				else:
					transaction.append(count * 2 + 1)
				count = count + 1
			positiveTransactions.append(transaction)
		else:
			for attribute in item[:-1]:
				if attribute == 0.0:
					transaction.append(count * 2)
				else:
					transaction.append(count * 2 + 1)
				count = count + 1
			negativeTransactions.append(transaction)
	for positiveFrequentItemset, positiveSupport in find_frequent_itemsets(positiveTransactions, minsup, True):
		positiveFrequentItemsets.append(positiveFrequentItemset)
		positiveSupports.append(positiveSupport)
	for negativeFrequentItemset, negativeSupport in find_frequent_itemsets(negativeTransactions, minsup, True):
		negativeFrequentItemsets.append(negativeFrequentItemset)
		negativeSupports.append(negativeSupport)
	# for itemset in positiveFrequentItemsets:
	# 	print itemset
	# print "negative"
	# for itemset in negativeFrequentItemsets:
	# 	print itemset
	# print "done"
	positiveDict = {}
	negativeDict = {}
	removePositive = {}
	removeNegative = {}
	idx = 0
	for itemset in positiveFrequentItemsets:
		num = 0
		for item in itemset:
			num = num + 2**item
		# print "positive num"
		# print num
		useless = False
		for key in positiveDict:
			if key & num == num:
				useless = True
			elif key & num == key:
				removePositive[key] = 1
		if useless == False:
			positiveDict[num] = positiveSupports[idx]
		idx = idx + 1
	idx = 0
	for itemset in negativeFrequentItemsets:
		num = 0
		for item in itemset:
			num = num + 2**item
		useless = False
		for key in negativeDict:
			if key & num == num:
				useless = True
			elif key & num == key:
				removeNegative[key] = 1
		# if num in positiveDict and positiveDict[num] != 1 and useless == False:
		if useless == False:
			negativeDict[num] = negativeSupports[idx]
		# print positiveDict
		# print negativeDict
		for key in removePositive:
			if key in positiveDict:
				del positiveDict[key]
		for key in removeNegative:
			if key in negativeDict:
				del negativeDict[key]
	json.dump(positiveDict, open("positiveFrequentItemsets.txt","w"))
	json.dump(negativeDict, open("negativeFrequentItemsets.txt","w"))
	json.dump(len(positiveFrequentItemsets), open("numOfPosResults.txt","w"))
	json.dump(len(negativeFrequentItemsets), open("numOfNegResults.txt","w"))
	# for itemset in find_frequent_itemsets(transactions, minsup):
	#     print itemset