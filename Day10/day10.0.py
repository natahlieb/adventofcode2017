import sys
file = open(sys.argv[1])
inputList = list(map(int, file.readline().split(",")))


currentPosition = 0
skipSize = 0
listSize = 256
listNums = list(range(listSize))

for num in inputList:
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

			print("listnums:{} currentPosition:{} currentValue:{} skipSize:{}\n\n\n".format(listNums, currentPosition	, listNums[currentPosition], skipSize))

print(listNums[0]*listNums[1])


