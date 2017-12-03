import sys

class Node (object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class linked_list(object):

    def __init__(self,  head = None):
        self.head = head
        if (head == None):
            self.size = 0
        else:
            self.size = 1
            
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.size +=1



    def toString(self):

        returnval = ''
        tempHead = self.head
        while tempHead is not None:
         returnval += tempHead.data    
         tempHead = tempHead.next_node
        return returnval

def getSum(valueList):
    tempHead = valueList.head
    sum = 0
    while tempHead is not None and tempHead.next_node is not None:
        if tempHead.data == tempHead.next_node.data:
            print(tempHead.data)
            print(tempHead.next_node.data)
            sum+=int(tempHead.data )
        tempHead = tempHead.next_node 
    if (tempHead.data == valueList.head.data):
        sum += int(tempHead.data)
    print(sum)
    return sum


def main(value):

     inputList = linked_list()

     for x in value:
        inputList.insert(x)
     returnVal = inputList.toString()
     sum = getSum(inputList)
     print('final sum: {}'.format(sum))
     #print (inputList.size)
     return

if __name__ == "__main__":
    main(sys.argv[1])