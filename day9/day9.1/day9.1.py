import sys

file = open(sys.argv[1])
inputString = file.readline()

#print(inputString)

while ('!' in inputString):
	firstIndex = inputString.index('!')
	inputString = inputString[:firstIndex] + inputString[firstIndex+2:]


totalCount = 0
while('<' in inputString):
	firstIndex = inputString.index('<')
	closingBracket = inputString.index('>')
	totalCount += (closingBracket-1)-firstIndex
	inputString = inputString[:firstIndex] + inputString[closingBracket+1:]
	
print(totalCount)

