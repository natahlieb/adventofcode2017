import sys

fp = open(sys.argv[1])

passphraseCounter = 0


for line in fp:
		row = line.strip().split(' ')
		examinedChunks = dict()
		validPassphrase = True
		for word in row:
			if (''.join(sorted(word)) in examinedChunks):
				validPassphrase = False
			else:
				examinedChunks[''.join(sorted(word))] = 1
		if (validPassphrase == True):
			passphraseCounter += 1


print(passphraseCounter)
			
