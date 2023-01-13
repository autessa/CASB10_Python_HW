from sys import *

#file1 = argv[1]
#file2 = argv[2]

#input is string of dna
#converts input to list of codons (need to run function on each reading frame)
#retrieves all the start codon indexes and start/stop codon index pairs
def startStop(input):
	starts = []
	stops = []
	stsp = []
	scripts = []
	output = []
	codons = []
	code = ""
	for i in range(0,len(input)):
		code += input[i]
		if len(code) == 3:
			codons.append(code)	
			code = ""
	
	for i in range(0,len(codons)):
		if codons[i] == "ATG":
			starts.append(i)

		if codons[i] == "TGA" or codons[i] == "TAA" or codons[i] == "TAG" or i == len(codons)-1:
			end = i+1
			for j in range(0,len(starts)):
				begin = starts[j]
				output.append(proteinTranslate(myDict, begin, end, codons))	
			starts = []	
	return output


#input is list of strings (each string is a codon)
#translates codons into amino acid, adds protein to list
def proteinTranslate(dict, beg, end, DNA):
	proteins = []
	aminoa = ""
	for i in range(beg, end):
		current = DNA[i]
		aminoa += dict.get(current)
	proteins.append(aminoa)
	return proteins	


#reverse and substitute codons function
def revSub(strDNA):
	sub = ""
	reverse = strDNA[::-1]
	for i in reverse:
		if i == "A":
			sub += "T"
		if i == "T":
			sub += "A"
		if i == "G":
			sub += "C"
		if i == "C":
			sub += "G"
	return sub


#print lists of proteins
def printProtein(proList):
	for i in proList:
		if i != []:
			print(i[0])
			

#actual script
#create dictionary
codon = []
amino = []
for line in open(argv[2], "r"):
	if line.strip():
		codon.append(line.split()[0])
		amino.append(line.split()[1])

myDict={}
for i in range(len(codon)):
	c = codon[i]
	letter = amino[i]
	myDict[c] = letter

#convert fastfa file into string
dnaSeq = ""
for line in open(argv[1], "r"):
	if (line[0] != '>'):
		dnaSeq += line.strip()
		dnaSeq = dnaSeq.upper()
dna1 = dnaSeq
dna2 = dna1[1:]
dna3 = dna2[1:] 

#rf = reading frame
rf1 = startStop(dna1)
rf2 = startStop(dna2)
rf3 = startStop(dna3)

#properly reversed dna sequence
rdna1 = revSub(dna1)
rdna2 = rdna1[1:]
rdna3 = rdna2[1:]

#rrf reversed reading frame
rrf1 = startStop(rdna1)
rrf2 = startStop(rdna2)
rrf3 = startStop(rdna3)

printProtein(rf1)
printProtein(rf2)
printProtein(rf3)
printProtein(rrf1)
printProtein(rrf2)
printProtein(rrf3)
