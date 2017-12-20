import sys

currentA = int(sys.argv[1])
currentB = int(sys.argv[2])
divisor =2147483647

totalCount = 0

checkedPairs = 0
multiplierA = 16807
multiplierB  = 48271

for i in range(0, 5000000):

	while(currentA % 4 != 0):
		currentA = (currentA * multiplierA) % divisor
	while(currentB % 8 != 0):
		currentB  = (currentB * multiplierB ) % divisor

	tempA = bin(currentA)
	tempB = bin(currentB)

	aBinary = tempA[len(tempA) - 16:]
	bBinary = tempB[len(tempB)-16:]

	checkedPairs += 1

	'''
	print(int(currentA))
	print(int(currentB))
	print(bBinary)
	print(aBinary)
	print("------------")
	'''

	if(aBinary == bBinary):
		totalCount +=1

	#input("Press Enter to continue")

	currentA = (currentA * multiplierA) % divisor
	currentB  = (currentB * multiplierB ) % divisor

print(totalCount)
