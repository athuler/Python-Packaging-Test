from importlib import reload
import pythonPackagingTest
import sys


while True:
	
	# Run Application
	exitCode = pythonPackagingTest.run(
		quitOnUpdateAvailable = True # Quits When Update Available & Installed
	)
	
	
	
	if(exitCode == 0):
		# Load Update
		reload(pythonPackagingTest)
		print("Application updated & reloaded!")
	else:
		break