import sys

generatorAPrevious = int(sys.argv[1])
generatorBPrevious = int(sys.argv[2])
divisor =2147483647

totalCount = 0

cycles = 40000000
multiplierA = 16807
multiplierB  = 48271

for i in range(0, cycles):
	currentA = (generatorAPrevious * multiplierA) % divisor
	currentB  = (generatorBPrevious * multiplierB ) % divisor

	tempA = bin(currentA)
	tempB = bin(currentB)

	aBinary = tempA[len(tempA) - 16:]
	bBinary = tempB[len(tempB)-16:]

'''	
	print(int(currentA))
	
	print(int(currentB))
	print(bBinary)
	print(aBinary)
	print("------------")

'''
	generatorBPrevious = currentB
	generatorAPrevious = currentA

	

	if(aBinary == bBinary):
		totalCount +=1

print(totalCount)
