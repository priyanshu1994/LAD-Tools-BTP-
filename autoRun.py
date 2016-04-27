import os
def autoRun():
	bashCommand = "python binarisationModule.py"
	os.system(bashCommand)
	for i in range(0,5):
		bashCommand = "python supportSetMinimization.py " + str(i * 0.1 + 0.5)
		os.system(bashCommand)
		for j in range(0,10):
			f =  open("accuracy","r+")
			accuracy = f.read()
			f.seek(0)
			accuracy = accuracy + "Correlation = " + str(i * 0.1 + 0.5) + " MinSup = " + str(j * 0.05 + 0.5) + " "
			f.write(accuracy)
			print "Correlation = " + str(i * 0.1 + 0.5) + " MinSup = " + str(j * 0.05 + 0.5) + " "
			f.close()
			bashCommand = "python patternGenerationModule.py " + str(j * 0.05 + 0.5)
			os.system(bashCommand)
			bashCommand = "sh test.sh"
			os.system(bashCommand)

autoRun()