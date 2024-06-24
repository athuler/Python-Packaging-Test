from pythonPackagingTest.sampleModule import sampleFunction
import threading
import subprocess
import sys
import time

__all__ = ["sampleModule"]
__version__ = "0.1.6.10.2"

def run(quitOnUpdateAvailable = False):
	
	# Set Up Shutdown Trigger
	global shutDownEvent
	shutDownEvent = threading.Event()
	shutDownEvent.set()
	
	# Prepare Threads
	updaterThread = threading.Thread(target = updater, name="Updater", args = (quitOnUpdateAvailable,))
	mainThread = threading.Thread(target = main, name="Updater")
	mainThread.daemon = True
	
	# Start Threads
	updaterThread.start()
	mainThread.start()
	
	# Catch Keyboard Interrupt
	
	while shutDownEvent.is_set():
		try:
			time.sleep(.1)
		except KeyboardInterrupt:
			shutDownEvent.clear()
			break
	
	# Shut Down Sequence
	print("Shutting Down...")
	updaterThread.join()
	mainThread.join()
	print("Shut down!")
	

def main():
	while shutDownEvent.is_set():
		try:
			data = input("Please enter a number to double: ")
		# Handle CTRL-C Input
		except EOFError:
			shutDownEvent.clear()
			continue
		processed = sampleFunction(int(data))
		print(f"Here's the doubled number: {processed}")


def updater(quitOnUpdateAvailable = True):
	installed_version = None
	while shutDownEvent.is_set():
		
		# Update Package With pip
		if installed_version is not None:
			subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "git+https://github.com/athuler/Python-Packaging-Test.git@main"], stdout = subprocess.DEVNULL,stderr = subprocess.DEVNULL)
		
		# Get Running Vs Installed Versions
		reqs = subprocess.run([sys.executable, '-m', 'pip', 'show', 'Python-Packaging-Test'], capture_output=True).stdout
		for pkg in reqs.split(b"\r\n"):
			if("Version" not in str(pkg)):
				continue
			installed_version = str(pkg).split(": ")[1].replace("'","")
			break
		print(f"Running version: {__version__}")
		print(f"Installed Version: {installed_version}")
		
		# Determine Whether Update is Necessary
		if(__version__ != installed_version and installed_version != None):
			print("UPDATE AVAILABLE")
			
			if quitOnUpdateAvailable:
				shutDownEvent.clear()
		else:
			# No update necessary
			time.sleep(5)