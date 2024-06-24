from importlib import reload
import pythonPackagingTest
import sys


while True:
	
	# Run Application
	exitCode = pythonPackagingTest.run(
		quitOnUpdateAvailable = True # Quits When Update Available & Installed
	)
	
	print(f"Received exit code {exitCode}")
	
	
	if(exitCode == 0):
		# Load Update
		reload(pythonPackagingTest)
		print("Application updated & reloaded!")
	else:
		# Exit Application
		print("Application shut down!")
		break