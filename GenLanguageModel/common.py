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
