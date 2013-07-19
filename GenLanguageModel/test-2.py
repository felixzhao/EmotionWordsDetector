import common
import operator
import sys
import reference as ref


def main():
  doclistpath = 'e:\\testset.txt'
  testset = open(doclistpath,'r').readlines()
  dictpath = 'e:\\pos-dict.txt'
  dictset = open(dictpath, 'r').readlines()
  filemappingpath = 'e:\\filenamemapping.txt'
  filenameset = open(filemappingpath,'r').readlines()

  termset = {}
  start = 95
  r = 5

  dict = ref.getdict(dictset)
  for d in range(start, start+r):
    doc = testset[d]
    filename = filenameset[d].replace('.xml','').replace('\n','')
    termset = ref.getres(filename, doc, dict, termset)
  outlist = sorted(termset.iteritems(), key=operator.itemgetter(1))
  outlist = outlist[:-100]

  outpath = 'e:\\res.txt'
  for oterm in outlist:
    outlist.append(str(oterm[0]) + ' , ' + str(oterm[1]))

  common.write2file(outpath, outlist)

if __name__ == "__main__":
  main()
