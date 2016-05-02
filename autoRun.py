import os
import sys
def autoRun():
	bashCommand = "python binarisationModule.py"
	os.system(bashCommand)
	for i in range(0,6):
		bashCommand = "python supportSetMinimization.py " + str(sys.argv[1]) + " " + str(i * 0.05 + 0.5)
		os.system(bashCommand)
		for j in range(0,8):
			f =  open("accuracy","r+")
			accuracy = f.read()
			f.seek(0)
			if int(sys.argv[1]) == 1:
				accuracy = accuracy + "Correlation = " + str(i * 0.05 + 0.1) + " MinSup = " + str(j * 0.05 + 0.7) + " "
			else:
				accuracy = accuracy + "Correlation = " + str(i * 0.05 + 0.6) + " MinSup = " + str(j * 0.05 + 0.7) + " "
			f.write(accuracy)
			f.close()
			bashCommand = "python patternGenerationModule.py " + str(j * 0.05 + 0.7)
			os.system(bashCommand)
			bashCommand = "sh test.sh " + str(sys.argv[1])
			os.system(bashCommand)

autoRun()
