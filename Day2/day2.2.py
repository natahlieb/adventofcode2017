import sys

def findDivisor(row):
		max = 0
		min = sys.maxsize
		for k in range(0, len(row), 1):
			for j in range(k+1, len(row), 1):
				print(' comparing k {} j {}'.format(row[k], row[j]))
				if(int(row[k]) > int(row[j])):
					if (int(row[k]) % int(row[j]) == 0):						
						return int(row[k]) / int(row[j])
				else:
					if (int(row[j]) % int(row[k]) == 0):						
						return int(row[j]) / int(row[k])

sum = 0
with open(sys.argv[1], "r") as f:
	for line in f:
		row = line.strip().split(' ')
		sum += findDivisor(row)
print(sum)

