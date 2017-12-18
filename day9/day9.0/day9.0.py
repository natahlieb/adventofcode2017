import sys

file = open(sys.argv[1])
inputString = file.readline()

print(inputString)

while ('!' in inputString):
	firstIndex = inputString.index('!')
	inputString = inputString[:firstIndex] + inputString[firstIndex+2:]


while('<' in inputString):
	firstIndex = inputString.index('<')
	closingBraket = inputString.index('>')
	inputString = inputString[:firstIndex] + inputString[closingBraket+1:]

	
acceptedChars = ['{','}', ',']
inputString = ''.join([i for i in inputString if i in acceptedChars])


#construct our stack
totalCount = 0
totalOpen = 0
for char in list(inputString):
	  if(char == '{'):
	  	totalOpen += 1
	  	totalCount += totalOpen
	  if(char == '}'):
	  	totalOpen -=1

print(totalCount)