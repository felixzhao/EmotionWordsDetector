def getngrams(term,n):
  ngrams = []
  
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

def getPdict(pvaluelist, splitflag):
  dict = {}
  for value in pvaluelist:
    if value.endswith('\n'):
      value = value[:-1]
    items = value.split(splitflag)
    dict[items[0]] = float(items[1])
  return dict

def getP(term,dict,n, min):
  grams = getngrams(term, n)
  plist = []
  for gram in grams:
    if dict.__contains__(gram) == 'true':
      plist.append(dict(gram))
    else:
      plist.append(min)
  P = 1
  for onep in plist:
    P *= onep
  return P

def getoutlist(dict):
  outlist = []
  for key in dict.keys():
    outlist.append(key +','+ str(dict[key]))
  return outlist

def main():
  splitflag = '###'
  plist = []
  doclistpath = 'e:\\practice.txt'
  termpath = 'e:\\term.txt'
  pvaluepath = 'e:\\p.txt'
  outpath = 'e:\\res.txt'
  n = 2
  m = 3
  min = 0.0000000001
  limit = 0.1
  doclist = open(doclistpath,'r').readlines()
  pvaluelist = open(pvaluepath,'r').readlines()
  testset = doclist[-5:]
  dict = getPdict(pvaluelist, splitflag)
  pdict = {}

  for d in xrange(len(testset)):
    ldoc = doclist[d].split(' ')
    for i in xrange(len(ldoc)):
      term = ldoc[i:i+m]
      p = getP(term,dict, n, min)
      if p > limit:
        pdict[' '.join(term)] = str(d) + ',' + str(i) + ',' + str(p)
  outlist = getoutlist(dict)
  write2file(outpath, outlist)
  
      

if __name__ == "__main__":
  main()
