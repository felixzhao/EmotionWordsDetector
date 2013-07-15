import sys
'''
	get term length equal m,

'''
def getterm(wordlist,m,start):
  termlist = []
  wordlist = wordlist.split(' ')
  for i in xrange(len(wordlist)):
    if(wordlist[i].startswith(start)):
      if i <= m - 1:
        termlist.append(' '.join(wordlist[:i + 1]))
      else:
        termlist.append(' '.join(wordlist[i-m+1:i + 1]))
  return termlist

def getAllTerms(inpath, m, start):
	docs = open(inpath,'r').readlines()
	termlist = []
	for doc in docs:
		term = getterm(doc, m , start)
		termlist.extend(term)
	return termlist

def write2file(outpath, outlist):
	out = '\n'.join(outlist)
	f = open(outpath, 'w')
	f.write(out)
	f.close()

def main(m):
	print m

	inpath = 'C:\\Users\\zhaoqua\\Documents\\GitHub\\EmotionWordsDetector\\traning-set\\practice.txt'
	outpath = 'e:\\term_L5.txt'
	start = '{{'
	wordlist = getAllTerms(inpath, int(m), start)	
	write2file(outpath, wordlist)
	
if __name__ == "__main__":
    main(sys.argv[1])