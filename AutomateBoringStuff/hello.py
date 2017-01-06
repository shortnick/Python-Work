#! python3
import sys

name = input("What is your name?")
def hello(name):
	print("Howdy "+ name, end='!')
	print("Hello " + name, end='!')
	print("Hi " + name, end='!')

# can end a print statment with a specific char sequence (, end = "thing")
# can also do a sperator sequence (, sep='thing')
hello(name)

print(sys.argv)