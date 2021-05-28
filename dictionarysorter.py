import string

alpabets = 'abcdefghijklmnopqrstuvwxyz'
rdict = dict([(x[1],x[0]) for x in enumerate(alpabets)])

n=0
fobj2 = open('dictionary/0_Allwords.txt', 'r')
word = fobj2.read().splitlines()

index = 0
fobj = open('%s.txt' % alpabets[0], 'w')
print(len(word))

for j in range(len(word)):
       if word[j].startswith(alpabets[index]):
              fobj.write(word[j])
              fobj.write('\n')
       else:
             fobj.close()
             index = rdict[word[j][0]]
             fobj = open('%s.txt' % alpabets[index], 'a')
             fobj.write(word[j]+"\n")



