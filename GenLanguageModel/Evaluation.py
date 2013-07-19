def getAP(source):
  ap = []
  for s in source:
    l = s.split(' ')
    if l[2] != 'N/A':
      ap.append(s)
  return ap

def getAN(source):
  ap = []
  for s in source:
    l = s.split(' ')
    if l[2] == 'N/A':
      ap.append(s)
  return ap

def getCP(emotionwords, source):
  cp = []
  dict = Getdict(source)
  for e in emotionwords:
    le = e.split(' ')
    location = ' '.join(le[:2])
    if dict.__contains__(location) == True:
      cp.append(e + dict[location])
  return cp

def getCN(emotionwords, source):
  cn = []
  dict = Getdict(source)
  for e in emotionwords:
    le = e.split(' ')
    location = ' '.join(le[:2])
    if dict.__contains__(location) == False:
      cn.append(e)
  return cn

def geteva(ap, cp):
  res = []
  dict = Getdict(ap)
  for e in cp:
    le = e.split(' ')
    location = ' '.join(le[:2])
    if dict.__contains__(location) == True:
      res.append(e + dict[location])
  return len(res) 

def getP(tp, fp):
  return tp/(tp+fp)

def getR(tp, fn):
  return tp/(tp+fn)

def Getdict(source):
  dict = {}
  for s in source:
    l = s.split(' ')
    if l[2] != 'N/A':
      dict[' '.join(l[:2])] = l[-1]
  return dict

def main():
  sourcepath = 'e:\\sourceInfo.txt'
  source = open(sourcepath,'r').readlines()
  emotionwordpath = 'e:\\CanidateEmationWord_100th.txt'
  emotionwords = open(emotionwordpath,'r').readline().split(';')

  ap = getAP(source)
  an = getAN(source)
  cp = getCP(emotionwords, source)
  cn = getCN(emotionwords, source)

  tp = geteva(ap, cp)
  fp = geteva(an, cp)
  fn = geteva(ap, cn)
  tn = geteva(an, cn)

  P = getP(tp, fp)
  R = getR(tp, fn)

  print len(ap)
  print len(an)
  print len(cp)
  print len(cn)

  print tp
  print fp
  print fn
  print tn
  print P
  print R

if __name__ == "__main__":
  main()
