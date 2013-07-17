def getfeq(doclist, term):
  feq = 0
  for doc in doclist:
    feq += doc.count(term)
  return feq

def getP(doclist, term):
  p = 1
  input = term.split(' ')
  for i in range(len(input)):
    feq = getfeq(doclist, ' '.join(input[i:]))
    per = getfeq(doclist, ' '.join(input[i:-1]))
    p *= feq/float(per)
  return p
	
def getngrams(term,n):
  ngrams = []
  term = term.split(' ')
  for i in range(len(term)):
    if i == 0:
      ngrams.append(' '.join(term[-n:]))
    else:
      ngrams.append(' '.join(term[-n-i:-i]))
  return ngrams

def write2file(outpath, outlist):
  out = '\n'.join(outlist)
  f = open(outpath, 'w')
  f.write(out)
  f.close()

def main():
  splitflag = ','
  plist = []
  doclistpath = 'e:\\practice.txt'
  termpath = 'e:\\neg.txt'
  outpath = 'e:\\p.txt'
  n = 2
  doclist = open(doclistpath,'r').readlines()
  termlist = open(termpath,'r').readlines()
  for term in termlist:
    grams = getngrams(term, n)
    for gram in grams:
      if gram.endswith('\n'):
        gram = gram[:-2]
      P = getP(doclist, gram)
      plist.append(gram + splitflag + str(P))
  write2file(outpath, plist)

if __name__ == "__main__":
  main()

