import common
import operator
import sys

def getPdict(pvaluelist, splitflag):
  dict = {}
  for value in pvaluelist:
    if value.endswith('\n'):
      value = value[:-1]
    items = value.split(splitflag)
    dict[items[0]] = float(items[1])
  return dict
def getP(term,dict,n, min):
  grams = common.getngrams(term, n)
  p = 1
  for gram in grams:
    if dict.__contains__(gram) == True:
      p *= float(dict[gram])
    else:
      p *= min
  return p
def getoutlist(dict):
  outlist = []
  for key in dict.keys():
    outlist.append(key +','+ str(dict[key]))
  return outlist
def gettermfromtestset(testset, m):
  termlist = []
  for d in xrange(len(testset)):
    ldoc = doclist[d].split(' ')
    for i in xrange(len(ldoc)):
      termlist.append(' '.join(ldoc[i:i+m]))
  return termlist
def gettestPset(termlist, dict, n, min):
  pset = {}
  for term in termlist:
    p = getP(term, dict, n, min)
    pset[term] = p
  return pset

def gettestsetterm(filename, doc, dict,m,  n, min):
  termset = {}
  ldoc = doc.split(' ')
  for i in xrange(len(ldoc)):
    term = ldoc[i:i+m]
    p = getP(term,dict, n, min)
    termset[filename +',' +str(i+n-1)] = p
  return termset

def getdict(dictset):
  dict = {}
  for item in dictset:
    litem = item.split(',')
    dict[litem[0]] = litem[1][:-1]
  return dict

def getres(filename, doc, dict, termset):
  outlist = []
  n = 2
  m = 3
  min = 0.0000000001
  termset = gettestsetterm(filename, doc, dict,m, n, min)
  return termset

def main():
  doclistpath = 'e:\\testset.txt'
  testset = open(doclistpath,'r').readlines()
  dictpath = 'e:\\pos-dict.txt'
  dictset = open(dictpath, 'r').readlines()
  filemappingpath = 'e:\\filenamemapping.txt'
  filenameset = open(filemappingpath,'r').readlines()

  termset = {}
  start = 0
  r = 100

  dict = getdict(dictset)
  for d in range(start, start+r):
    doc = testset[d]
    filename = filenameset[d].replace('.xml','').replace('\n','')
    termset = getres(filename, doc, dict, termset)
  outlist = sorted(termset.iteritems(), key=operator.itemgetter(1))
  outlist = outlist[-100:]

  print outlist

  outpath = 'e:\\res.txt'
  outstr = ';'.join('%s,%s' % x for x in outlist)
  outf = open(outpath,'w')
  outf.write(outstr)

if __name__ == "__main__":
  main()
