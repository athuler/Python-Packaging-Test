from pythonPackagingTest.sampleModule import sampleFunction

__all__ = ["sampleModule"]

def run():
	data = input("Please enter a number to double: ")
	
	print("Thanks for the number")
	
	processed = sampleFunction(int(data))
	
	print(f"Here's the doubled number: {processed}")
