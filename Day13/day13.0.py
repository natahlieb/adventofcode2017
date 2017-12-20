import sys

def calculateScannerLocation(cycleNubmer, depth):
	currentLocation = 0
	count = 0
	direction = "down"
	depth = depth - 1

	while(count != cycleNubmer):
		if (direction == "down"):
		 	if currentLocation+1 <= depth:
		 		currentLocation += 1
		 	else:
		 		direction = "up"
		 		currentLocation -= 1
		elif direction == "up":
			if(currentLocation -1 >= 0):
				currentLocation -= 1
			else:
				direction	 = "down"
				currentLocation+=1
		count+=1
		#print("Count:{}, Location: {}, Direction:{}".format(count, currentLocation, direction))



		

	#print("Current location of scanner is: {}".format(currentLocation))
	return currentLocation






layerHash = {}
file = open(sys.argv[1])

totalCost = 0

for line in file:
	inputArray = list(map(int, line.replace(" ", "").split(":")))
	layerHash[inputArray[0]] = inputArray[1]

for item in layerHash:
	print("{}: {}".format(item, layerHash[item]-1))

currentLayer = 0
numberCycles = max(layerHash)

for i in range(0, numberCycles+1):
	'''for j in layerHash:
		#calculate scanner location
		location = calculateScannerLocation(i, layerHash[j])
		print("Layer: {} CurrentLocation of scanner for this layer:{}".format(j, location))
		#if (location == 0):
		#	print("Hit the scanner; adding to total cost")
		#	totalCost +=  (i * layerHash[i])
	print("\\\\\\\\\\\\\\\\\n")
	input("Press Enter to continue...")
	'''
	if i in layerHash:
		#calculate scanner location
		location = calculateScannerLocation(i, layerHash[i])
		if location == 0:
			print("Cycle {}: Hit the scanner; adding to total cost".format(i))
			totalCost += (i * layerHash[i])
print(totalCost)

#severity = depth * range