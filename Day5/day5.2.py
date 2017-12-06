import sys

inputList = []
fp = open(sys.argv[1])

#read in our file and construct the list
for line in fp:
	inputList.append(int(line))


iterationCounter = 0
currentIndex = 0

#iterate until we're out of the loop -> need to see if go ahead of list (index <0) or outside of it (index > len(list))
while(currentIndex < len(inputList) and currentIndex > -1 ):
	#determine how far to jump
	currentValue = inputList[currentIndex]

	#increment our current location in the list by 1 if offset is less than three
	if(currentValue < 3):
		inputList[currentIndex] += 1
	#otherwise decrement our current offset by 1
	else:
		inputList[currentIndex] -= 1

	#update the index we want to look at and increment our iteration counter
	currentIndex += currentValue
	iterationCounter += 1


print('total iterations: {}'.format(iterationCounter))
#print(inputList)