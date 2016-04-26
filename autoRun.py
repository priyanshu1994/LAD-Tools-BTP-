import os
def autoRun():
	for i in range(0,5):
		for j in range(0,10):
			bashCommand = "python binarisationModule.py"
			os.system(bashCommand)
			bashCommand = "python supportSetMinimization.py " + str(i*0.1 +0.5)
			os.system(bashCommand)
			bashCommand = "python patternGenerationModule.py " + str(j*0.05+0.5)
			os.system(bashCommand)
			bashCommand = "sh test.sh"
			os.system(bashCommand)

autoRun()