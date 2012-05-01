import sys

for line in sys.stdin:
	line = line.strip()
	line2 = line[1] + line[0] + line[2:-2] + line[-1] + line[-2]
	print line2
