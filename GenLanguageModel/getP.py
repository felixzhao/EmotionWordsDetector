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
		p *= getsubP(doclist,input[i:])
	return p
