import sys
import copy
import math

file = open(sys.argv[1])

class Node(object):
	def __init__(self, value, weight):
		self.value = value
		self.children = None
		self.parent = None
		self.weight = weight



nodes = {}
listChildren = []
for line in file:
	node_and_children = line.replace(',', '').split('->')
	nodeValue = node_and_children[0].split(' ')[0]
	nodeWeight = int(node_and_children[0].replace('(', '').replace(')', '').split(' ')[1])


	node = Node(nodeValue, nodeWeight)
	if len(node_and_children) > 1:
			node.children = list(node_and_children[1].strip().replace(',', '').split(' '))
			listChildren.extend(list(node_and_children[1].strip().split(' ')))
	nodes[nodeValue] = node


for item in nodes:
	currentNodeValue = nodes[item].value
	if nodes[item].children != None:
		for child in nodes[item].children:
			childName = child.strip(',')
			nodes[childName].parent = currentNodeValue



while(True): 
	childlessNodes = []
	parentNodes = []

	for x in nodes:
		if(nodes[x].children == None or len(nodes[x].children) == 0):
			childlessNodes.append(nodes[x].value)
			if nodes[x].parent not in parentNodes:
				parentNodes.append(nodes[x].parent)

	print('childless nodes:{}'.format(childlessNodes))
	print('parent nodes:{}'.format(parentNodes))



	for node in parentNodes:
		#sum up child values, divide by number of children
		encounteredValue = nodes[nodes[node].children[0]].weight
		for child in nodes[node].children:
			if(nodes[child].weight != encounteredValue):
				print('unbalanced weight at {}:'.format(child))
				print('unbalanced weight is {}'.format(math.fabs(nodes[child].weight - encounteredValue)))
				unbalanced = False
				sys.exit()


		nodes[node].weight += encounteredValue * len(nodes[node].children)
		print(nodes[node].weight)


	for value in childlessNodes:
		if (value in nodes):
			parent = nodes[value].parent
			nodes.pop(value)
			if(value in nodes[parent].children):
				nodes[parent].children.remove(value)


	for item in nodes:
		print('value:{} parent:{} children:{} weight:{}'.format(nodes[item].value, nodes[item].parent, nodes[item].children, nodes[item].weight))
	i += 1
	print('--------------\n')

'''


for node in nodes:
	print('Node: {} Children: {} Parent: {}'.format(nodes[node].value, nodes[node].children, nodes[node].parent))



print(deletedList)
for value in deletedList:
	if (value in nodes):
		parent = nodes[value].parent
		nodes.pop(value)
		if(value in nodes[parent].children):
			nodes[parent].children.remove(value)

for node in nodes:
	print('Node: {} Children: {} Parent: {}'.format(nodes[node].value, nodes[node].children, nodes[node].parent))

'''