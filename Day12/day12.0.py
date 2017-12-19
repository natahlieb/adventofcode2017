import sys

examinedNodes = []
nodeHash = {}

def getValidNeighbors(listNeighbors):
	returnList = []
	for item in listNeighbors:
		if not item in examinedNodes:
			returnList.append(item)

	return returnList

def getNeighbors(currentNode):
	examinedNodes.append(currentNode)
	validNeighborList = getValidNeighbors(nodeHash[currentNode])
	print(validNeighborList)
	if (len(validNeighborList) == 0):
		return
	else:
		for node in validNeighborList:
			getNeighbors(node)




def main():
	file = open(sys.argv[1])

	for line in file:
		line = line.replace(" <->", ",").replace(" ", "").strip()
		line = list(map(int, line.split(",")))
		global nodeHash
		if len(line) > 1:
			if not (line[0] in nodeHash):
				nodeHash[line[0]] = []
			for i in range(1, len(line)):
				if not line[i] in nodeHash[line[0]]:
					nodeHash[line[0]].append(line[i])
	getNeighbors(0)
	

	#dedupe our nodesd
	newList = []
	for i in examinedNodes:
		if not  i in newList:
			newList.append(i)
	print(newList)
	print(len(newList))
	
main()