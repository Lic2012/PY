#!/usr/bin/python  
#-*-coding:utf-8-*- 
'''
Created on 2013Äê12ÔÂ17ÈÕ

@author: Administrator
'''
def process(fin, fout):
    f = open(fin)
    fo = open(fout,"w")
    for line in f:
        c = line.strip("\r\n\t").split("\t")
        for i in range(1,len(c)):
#             print c[0]+"\t"+c[i]
            fo.write(c[0]+"\t"+c[i]+"\n")
    f.close()
    fo.close()
    
if __name__ == '__main__':
    d = "C:\\Users\\Administrator\\Desktop\\"
    process(d + "candidate_nickname", d+"nickname")
    process(d + "candidate_formername", d+"formername")
    process(d + "candidate_relatedname", d+"relatedname")
    process(d + "candidate_anchorname", d+"anchorname")   