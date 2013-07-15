def getfeq(doclist, term):
	feq = 0
	for doc in doclist:
		feq += doc.count(' '.join(term))
	return feq
	
def getsubP(doclist, subterm):
	feq = getfeq(doclist, subterm)
	per = getfeq(doclist, subterm[:-1])
	p = feq/float(per)
	return p

def getP(doclist, term):
	p = 1
	input = term.split(' ')
	for i in range(len(input)):
		feq = getfeq(doclist, input[i:])
		per = getfeq(doclist, input[i:-1])
		p *= feq/float(per)
	return p

def getngrams( term, n ):
    ngrams = []
	for i in xrange( len(term) ):
		if i == 0:
			ngrams.append(term[-n:])
		else:
		ngrams.append( term[-n-i:-i])
    return ngrams
	
def main():

	
if __name__ == "__main__":
    main()