rm output.xls
python createPatternForInputFile.py
python testInstance.py
#libreoffice --calc Output.xls
python calcAccuracy.py
# rm *.txt
# rm binarisedOutput.xls
# rm convertedTestData.xls
# rm minimizedSupprtSetOutput.xls
