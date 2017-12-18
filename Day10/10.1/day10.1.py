import sys
file = open(sys.argv[1])
inputString = file.readline()


#convert to ascii value
convertedInput = []
for char in inputString:
	asciiValue = ord(char)
	convertedInput.append(asciiValue)

convertedInput = list(map(int, convertedInput)) + [17, 31, 73, 47, 23]
print(convertedInput)

currentPosition = 0
skipSize = 0
listSize = 256
listNums = list(range(listSize))

for i in range(0, 64):
	print("round {}".format(i))
	for num in convertedInput:
			print("{}, ".format(num), end=" ")
			if(num <= listSize):
				#reverse the chunk of list
				reverseList	= None
				if(num + currentPosition > listSize):
					pullFromFront = (num + currentPosition	) - listSize
					reverseList = listNums[currentPosition	: listSize]
					reverseList += (listNums[0:pullFromFront])
					reverseList.reverse()


				else:
					reverseList = listNums[currentPosition:currentPosition+num]
					reverseList.reverse()


				tempIndex = currentPosition	
				for item in reverseList:
						if(tempIndex >= listSize):
							tempIndex	 = 0
						listNums[tempIndex] = item
						tempIndex	+= 1
				
				currentPosition	+= skipSize	+ num
				skipSize+=1
				while (currentPosition	> listSize):
					currentPosition	 -= listSize
	print("\n")

print(listNums)	
#convert from sparse hash to dense hash
denseList = []
i = 0
while(i+16 <= 256):
		xordValue = 0
		j = i
		while(j < i+16 ):
			xordValue =  xordValue ^ listNums[j]
			j+=1

		i+=16
		denseList.append(xordValue)

#convert values to hash
finalList=  list(map(hex, denseList))
print(finalList)

