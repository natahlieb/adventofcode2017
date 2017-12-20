import sys

#create List programs
startingAscii = 97
listPrograms = []
for i in range(0, 16):
	listPrograms.append(chr(startingAscii))
	startingAscii +=1

print(listPrograms)

file = open(sys.argv[1])
operations = file.readline().split(",")

for operation in operations:
	print(operation)
	#spin operation
	if operation[0] == "s":
		numberSpins = int(operation[1:])
		listPrograms = listPrograms[len(listPrograms)-numberSpins: ] + listPrograms[0:len(listPrograms)-numberSpins]
	#exchange operation
	elif operation[0]== "x":
		operation = operation[1:].split("/")
		print(operation)
		firstPosition = int(operation[0])
		secondPosition = int(operation[1])
		firstProgram = listPrograms[firstPosition]
		listPrograms[firstPosition]	= listPrograms[secondPosition]
		listPrograms[secondPosition] = firstProgram	

	#partner operation
	elif operation[0]== "p":
		operation = operation[1:].split("/")
		print(operation)
		indexFirstProgram = listPrograms.index(operation[0])
		indexSecondProgram = listPrograms.index(operation[1])
		firstProgram = listPrograms[indexFirstProgram]
		listPrograms[indexFirstProgram] = listPrograms[indexSecondProgram]
		listPrograms[indexSecondProgram] = firstProgram
	print(listPrograms)

print("".join(listPrograms))
