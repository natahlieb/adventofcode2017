import sys

fp = open(sys.argv[1])


for line in fp:
	inputArray = [int(x) for x in line.split("\t")]
	initalConfig = inputArray

	observedConfigs = {}
	observedConfigs[' '.join(str(x) for x in inputArray)] = 1
	observedBefore = False
	loopCounter = 0

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

		
		#if we've seen this configuration before, we know we've looped around, and are starting from a blank slate. start the count on the second iterator	
		if(' '.join(str(x) for x in inputArray) in observedConfigs):
			observedConfigs[' '.join(str(x) for x in inputArray)] += 1
			loopCounter += 1
			
		#otherwise, add the configuration to our dict, and set its counter to 1
		else:				
			observedConfigs[' '.join(str(x) for x in inputArray)] = 1

		#if we've finished our second iteration (i.e. seen our initial configuration 3 times now, break and return the counter)
		if(observedConfigs[' '.join(str(x) for x in initalConfig)] > 2):
			print('loopCounter: {}'.format(loopCounter-1))
			observedBefore = True 
			break


