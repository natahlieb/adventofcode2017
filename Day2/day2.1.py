import sys

sum = 0
with open(sys.argv[1], "r") as f:
	for line in f:
		row = line.strip().split(' ')
		max = 0
		min = sys.maxsize
		for k in range(0, len(row), 1):
			
			if (int(row[k]) > max):
				max = int(row[k])

			if (int(row[k]) < min):
				min  = int(row[k])
				##print ('min: {}, value: {}'.format(min, k))
		print("max: {}    min: {}".format(max, min))
		sum += int(max - min)

print(sum)