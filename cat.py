#imports things from system library
import sys 

# sys.stdin -> python's special name for whatever you type into it when you run it
#python's for loop syntax
for line in sys.stdin:

	#takes any whitespace and gets rid of them
	line = line.strip()

	#print line back out
	print line
