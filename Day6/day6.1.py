import sys

fp = open(sys.argv[1])

print(fp)

totalIterations = 1
for line in fp:
	print(line)
	inputArray = [int(x) for x in line.split("\t")]
	print(inputArray)
	observedConfigs = {}
	observedConfigs[' '.join(str(x) for x in inputArray)] = 1
	observedBefore = False

	while(not observedBefore):

		#grab block with maximum blocksToRedistribute
		maxBlockCountIndex = inputArray.index(max(inputArray))		
		
		#set the number of blocksToRedistribute we need to redistribute
		blocksToRedistribute = inputArray[maxBlockCountIndex]
		inputArray[maxBlockCountIndex] = 0
		currentIndex = (maxBlockCountIndex + 1)

		while(blocksToRedistribute > 0):

			#check to make sure that we aren't going beyond the end of our array; loop back if needed to first index
			if(currentIndex == len(inputArray)):
				currentIndex = 0

			inputArray[currentIndex] += 1
			blocksToRedistribute-=1
			currentIndex+=1

			
		if(' '.join(str(x) for x in inputArray) in observedConfigs):
			observedBefore = True
			break
		else:				
			observedConfigs[' '.join(str(x) for x in inputArray)] = 1
			totalIterations +=1 

print(totalIterations)