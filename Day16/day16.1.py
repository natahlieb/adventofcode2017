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

seenPatterns = {}
seenPatterns["".join(listPrograms)] = 0

cycle = 1
neededCycle = 0

while cycle <= 1000000000:
	for operation in operations:
		#spin operation
		if operation[0] == "s":
			numberSpins = int(operation[1:])
			listPrograms = listPrograms[len(listPrograms)-numberSpins: ] + listPrograms[0:len(listPrograms)-numberSpins]
		#exchange operation
		elif operation[0]== "x":
			operation = operation[1:].split("/")
			firstPosition = int(operation[0])
			secondPosition = int(operation[1])
			firstProgram = listPrograms[firstPosition]
			listPrograms[firstPosition]	= listPrograms[secondPosition]
			listPrograms[secondPosition] = firstProgram	

		#partner operation
		elif operation[0]== "p":
			operation = operation[1:].split("/")
			indexFirstProgram = listPrograms.index(operation[0])
			indexSecondProgram = listPrograms.index(operation[1])
			firstProgram = listPrograms[indexFirstProgram]
			listPrograms[indexFirstProgram] = listPrograms[indexSecondProgram]
			listPrograms[indexSecondProgram] = firstProgram

	print("cycle: {}: {}".format(cycle, "".join(listPrograms)))
	if not "".join(listPrograms) in seenPatterns:
		seenPatterns["".join(listPrograms)] = cycle
	else:
		print("Pattern last seen at cycle: {}".format(seenPatterns["".join(listPrograms)]))
		print("current cycle is :{}".format(cycle)) 
		neededCycle = cycle
		break

	cycle+=1

cycle = 1000000000 % cycle
for i in seenPatterns:
	if seenPatterns[i] == cycle:
		print(i)
		break

