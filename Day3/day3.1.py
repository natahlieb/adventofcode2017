import sys
import math

inputNum = int(sys.argv[1])

startingSquare = 1
while ((startingSquare**2) < inputNum):
	startingSquare +=2


maxDistance = startingSquare -1

#determineCorners
rightBottom = startingSquare ** 2
rightTop = (startingSquare-2)**2 + (startingSquare-1)
leftTop = rightTop	 + (startingSquare-1)
leftBottom = leftTop + (startingSquare-1)


#see if we're on a corner
if (inputNum == rightBottom or inputNum == rightTop or inputNum == leftTop or inputNum == leftBottom):
	print('distance is: {}'.format(maxDistance))
else:

	#we're not on a corner, so we need to figure out what edge we're on

	print('maxdistance is {}'.format(maxDistance))
	midPoint = 0

	#see if on right edge
	if (inputNum > (startingSquare-2)**2 and inputNum < rightTop):
		print('rightEdge')
		midPoint = (startingSquare-2)**2 + maxDistance/2
		
	elif (inputNum > rightTop and inputNum < leftTop):
		print('top edge')
		midPoint = rightTop + (maxDistance/2)
	elif (inputNum > leftTop and inputNum	 < leftBottom):
		print('left edge')
		midPoint = leftTop + (maxDistance/2)
	else:
		print('bottomEdge')
		midPoint = leftBottom + (maxDistance/2)

	if(inputNum == midPoint):
		distance = maxDistance/2
	else:
		#see if closer to edge or midPoint

		distance = maxDistance/2 + abs(inputNum - midPoint)
	print('distance is {}'.format(distance))


