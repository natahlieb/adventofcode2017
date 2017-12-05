import sys

fp = open(sys.argv[1])

passphraseCounter = 0


for line in fp:
		row = line.strip().split(' ')
		examinedChunks = dict()
		validPassphrase = True
		for x in row:
			if x in examinedChunks:
				validPassphrase = False
				break;
			else:
			   examinedChunks[x] = 1
		if (validPassphrase == True):
			passphraseCounter+=1
print(passphraseCounter)