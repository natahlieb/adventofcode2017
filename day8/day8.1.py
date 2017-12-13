import sys
registerHash = {}
maxValue = 0

file = open(sys.argv[1])
i = 0

maxValue = 0
for line in file:
		values = line.split(" ")

		targetRegister = values[0]
		targetOperator =  values[1]

		targetValue = int(values[2])
		conditionalOperation = values[5]
		conditionalRegister = values[4]
		conditionalValue = values[6]
		conditionalRegisterValue  = 0



		#print(line)
		#print(values[0])
		
		if (conditionalRegister in registerHash):
			conditionalRegisterValue = registerHash[conditionalRegister]
		else:
			registerHash[conditionalRegister] = 0

		if(not targetRegister in registerHash):
			registerHash[targetRegister] = 0


		if conditionalOperation == ">":
			if (conditionalRegisterValue  >  int(conditionalValue)):
				if (targetOperator == 'inc'):
					registerHash[targetRegister] += targetValue
				else:
					registerHash[targetRegister] -= targetValue
				


		elif conditionalOperation == "<":
			if (conditionalRegisterValue  <  int(conditionalValue)):
				if (targetOperator == 'inc'):
					registerHash[targetRegister] += targetValue
				else:
					registerHash[targetRegister] -= targetValue



		elif conditionalOperation == "<=":
			if (conditionalRegisterValue  <=  int(conditionalValue)):
				if (targetOperator == 'inc'):
					registerHash[targetRegister] += targetValue
				else:
					registerHash[targetRegister] -= targetValue



		elif conditionalOperation == ">=":
			if (conditionalRegisterValue  >=  int(conditionalValue)):
				if (targetOperator == 'inc'):
					registerHash[targetRegister] += targetValue
				else:
					registerHash[targetRegister] -= targetValue



		elif conditionalOperation == "==":
			if (conditionalRegisterValue  ==  int(conditionalValue)):
				if (targetOperator == 'inc'):
					registerHash[targetRegister] += targetValue
				else:
					registerHash[targetRegister] -= targetValue



		elif conditionalOperation == "!=":
			if (conditionalRegisterValue  !=  int(conditionalValue)):
				if (targetOperator == 'inc'):
					registerHash[targetRegister] += targetValue
				else:
					registerHash[targetRegister] -= targetValue

		if (registerHash[targetRegister] > maxValue):
					maxValue = registerHash[targetRegister]
		
		'''for item in registerHash:
			print('{} : {}'.format(item, registerHash[item]))
		print('--------------------')
		'''

print(maxValue)

	