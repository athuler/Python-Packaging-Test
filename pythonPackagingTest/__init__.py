from pythonPackagingTest.sampleModule import sampleFunction
import threading
import subprocess
import sys
import time

__all__ = ["sampleModule"]
__version__ = "0.1.6.7"

def run():
	
	# Set Up Shutdown Trigger
	global shutDownEvent
	shutDownEvent = threading.Event()
	shutDownEvent.set()
	
	# Prepare Threads
	updaterThread = threading.Thread(target = updater, name="Updater")
	mainThread = threading.Thread(target = main, name="Updater")
	mainThread.daemon = True
	
	# Start Threads
	updaterThread.start()
	mainThread.start()
	
	# Catch Keyboard Interrupt
	try:
		while 1:
			time.sleep(.1)
	except KeyboardInterrupt:
		print("Shutting Down...")
		shutDownEvent.clear()
		updaterThread.join()
		mainThread.join()
		print("Shut down!")
	

def main():
	while shutDownEvent.is_set():
		data = input("Please enter a number to double: ")
		processed = sampleFunction(int(data))
		print(f"Here's the doubled number: {processed}")
	
def updater():
	installed_version = None
	while shutDownEvent.is_set():
		
		# Update Package With pip
		if installed_version is not None:
			subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "git+https://github.com/athuler/Python-Packaging-Test.git@main"])
		
		# Get Running Vs Installed Versions
		reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'show', 'Python-Packaging-Test'])
		for pkg in reqs.split(b"\r\n"):
			if("Version" not in str(pkg)):
				continue
			installed_version = pkg.split(": ")[1]
			break
		print(f"Running version: {__version__}")
		print(f"Installed Version: {installed_version}")
		
		# Determine Whether Update is Necessary
		if(__version__ == installed_version and installed_version != None):
			print("UPDATE AVAILABLE")
		
		time.sleep(5)