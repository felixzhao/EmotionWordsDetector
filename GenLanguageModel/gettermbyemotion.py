def write2file(outpath, outlist):
  out = '\n'.join(outlist)
  f = open(outpath, 'w')
  f.write(out)
  f.close()

def main():
  termpath = 'C:\\Users\\zhaoqua\\Documents\\GitHub\\EmotionWordsDetector\\traning-set\\term_L7.txt'
  pospath = 'C:\\Users\\zhaoqua\\Documents\\GitHub\\EmotionWordsDetector\\traning-set\\pos.txt'
  negpath = 'C:\\Users\\zhaoqua\\Documents\\GitHub\\EmotionWordsDetector\\traning-set\\neg.txt'
  doclist = open(termpath,'r').readlines()
  poslist = []
  neglist = []
  for line in doclist:
    if line.endswith('\n'):
      line = line[:-1]
    if line.endswith('positive}}'):
      poslist.append(line)
    elif line.endswith('negative}}'):
      neglist.append(line)
  write2file(pospath, poslist)
  write2file(negpath, neglist)    

if __name__ == "__main__":
  main()
