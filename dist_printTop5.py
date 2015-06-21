# -*- coding: UTF-8 -*-
from nltk.util import ngrams
import sys
import operator
#import string
#讀檔的n
n = int(sys.argv[2])
#print n
i = 0
mydict={}
temp=[]
#檔案名
fh = file(sys.argv[1],"r")
while True:
  line = fh.readline().lower()
  #去除標點符號
  if line =='':
    break
  
  else:
#    print line
#    print line.split()
    delte_mark = line.split()
    #print delte_mark
    for x in delte_mark:
    #print x[-1]
    #想用ascii 但找不到方法 所以直接判斷26英文字母的方式
      if x[-1]!='a' and x[-1]!='b' and x[-1]!='c' and x[-1]!='d' and x[-1]!='e' and x[-1]!='f' and x[-1]!='g'and x[-1]!='h'and x[-1]!='i'and x[-1]!='j'and x[-1]!='k'and x[-1]!='l'and x[-1]!='n'and x[-1]!='m'and x[-1]!='o'and x[-1]!='p'and x[-1]!='q'and x[-1]!='r'and x[-1]!='s'and x[-1]!='t'and x[-1]!='u'and x[-1]!='v'and x[-1]!='w'and x[-1]!='x'and x[-1]!='y'and x[-1]!='z':
    #if x[-1]!='f'  x[-1]!='d':
        x=x[:-1]
    #print x 
      temp.append(x)
      #print temp  
    delte_mark_line = " ".join(temp)
    #print delte_mark_line
    #讀完一行要把temp變空 讀下一行 不然會重覆
    temp=[]

    i += 1
    #print i
    sixgrams = ngrams(delte_mark_line.split(), n)
    for grams in sixgrams:
      #print grams
      if grams in mydict:
        #在位子0（出現次數）加一
        mydict[grams][0] += 1
        #然後在後面append出現位子
        mydict[grams].append(i)        
      else:
        #在位子0出現一次並加入i第幾行
        mydict[grams]=[1, i] 
fh.close()
#排序 key=operatand.itemgetter(1)是dict的value reverse=True是反的排
sorted_x = sorted(mydict.items(), key=operator.itemgetter(1),reverse=True)
#印出前5個
print sorted_x[0]
print
print sorted_x[1]
print
print sorted_x[2]
print
print sorted_x[3]
print
print sorted_x[4]
# print mydict[('Reed',)]
# print mydict[('I','was')]


