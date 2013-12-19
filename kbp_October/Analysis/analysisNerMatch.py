#!/usr/bin/python  
#-*-coding:utf-8-*- 
'''
Created on 2013Äê11ÔÂ22ÈÕ

@author: Administrator
'''

if __name__ == '__main__':
    f = open("C:\\Users\\Administrator\\Desktop\\ExpansionAnalysisRawSystem")
    f_kb = open("C:\\Users\\Administrator\\Desktop\\candidate_0728.info")
    f_nerQ = open("C:\\Users\\Administrator\\Desktop\\query_3sentence_middle_distsim_4class")
    nerDic_kb ={}
    for line in f_kb:
        chunk = line.strip("\n\r").split("\t")
        nerDic_kb[chunk[2]] = chunk[1]
    nerDic_q = {}
    for line in f_nerQ:
        chunk = line.strip("\n\r").split("\t")
        nerDic_q[chunk[0]] = chunk[2]
        
    cnt = 0 # query ner tagger differ from answer ner tagger
    while(True):
        line1 = f.readline().strip("\n\r")
        if not line1:
            break
        line2 = f.readline().strip("\n\r")
        c1 = line1.split("\t")
        c2 = line2.lstrip(" \t").split("\t")
        queryId = c1[0]
        queryName = c1[2]
        entityName = c1[3]
        systemName = c2[2]
        nerG = c1[4] # golden standards ner tagger(may differ from kb tagger)
        nerS = c2[3] #kb ner tagger on system
        if c1[1].startswith("E"): nerK = nerDic_kb[c1[1]] #kb ner tagger on answer
        else: nerK = "NIL"
        nerQ = nerDic_q[c1[0]] #standford ner tagger on query
        
        if nerQ != nerK and nerK != "NIL":
            print queryId+"\t"+queryName+"\t"+nerQ+"\t-->\t"+entityName+"\t"+nerK
            cnt += 1
    print "number",cnt