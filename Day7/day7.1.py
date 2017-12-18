import sys
import copy

file = open(sys.argv[1])

class Node(object):
	def __init__(self, value, children = None, parent = None):
		self.value = value
		self.children = None
		self.parent = None



nodes = {}
listChildren = []
for line in file:
	node_and_children = line.replace(',', '').split('->')
	nodeValue = node_and_children[0].split(' ')[0]

	node = Node(nodeValue)
	if len(node_and_children) > 1:
			node.children = list(node_and_children[1].strip().replace(',', '').split(' '))
			listChildren.extend(list(node_and_children[1].strip().split(' ')))
	nodes[nodeValue] = node


for item in nodes:
	if (item not in listChildren):
		print(item)
