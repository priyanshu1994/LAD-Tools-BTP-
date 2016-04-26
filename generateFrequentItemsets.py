import binarisationVariables as BV
from fp_growth import find_frequent_itemsets
from excelFileReader import *
import json

def generateFrequentItemsets(minsup):
	# print BV.items
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
	# print "here\n\n"
	# print len(positiveTransactions)
	# print len(negativeTransactions)
	for positiveFrequentItemset, positiveSupport in find_frequent_itemsets(positiveTransactions, int(minsup * len(positiveTransactions)), True):
		positiveFrequentItemsets.append(positiveFrequentItemset)
		positiveSupports.append(positiveSupport)
	for negativeFrequentItemset, negativeSupport in find_frequent_itemsets(negativeTransactions, int(minsup * len(negativeTransactions)), True):
		negativeFrequentItemsets.append(negativeFrequentItemset)
		negativeSupports.append(negativeSupport)
	# print "FP done\n\n"
	# for itemset in positiveFrequentItemsets:
	# 	print itemset
	# print "negative"
	# for itemset in negativeFrequentItemsets:
	# 	print itemset
	# print "done"
	# print len(positiveFrequentItemsets)
	# print len(negativeFrequentItemsets)
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
	# print "dumping\n\n"
	json.dump(positiveDict, open("positiveFrequentItemsets.txt","w"))
	json.dump(negativeDict, open("negativeFrequentItemsets.txt","w"))
	json.dump(len(positiveTransactions), open("numOfPosResults.txt","w"))
	json.dump(len(negativeTransactions), open("numOfNegResults.txt","w"))
	# for itemset in find_frequent_itemsets(transactions, minsup):
	#     print itemset