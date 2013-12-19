#!/usr/bin/python  
#-*-coding:utf-8-*- 
'''
Created on 2013年11月21日

@author: Administrator
'''

class f():
    dir = "C:\\Users\\Administrator\\Desktop\\"
    name = "ExpansionAnalysisRawSystem"
        
if __name__ == '__main__':
    f = f()
    fin = open(f.dir+f.name)
    cnt = 0
    while(True):
        line1 = fin.readline().strip("\n\r")
        if not line1:
            break
        line2 = fin.readline().strip("\n\r")
        c1 = line1.split("\t")
        c2 = line2.lstrip(" \t").split("\t")
        queryId = c1[0]
        queryName = c1[2]
        entityName = c1[3]
        systemName = c2[2]
        nerG = c1[4]
        nerS = c2[3]
        #如果有Republic, Kingdom
        findList = ['Republic','Kingdom']
        
        for s in findList:
            if s.lower() in queryName.lower():
#                 if systemName == "NIL":
#                     cnt += 1
#                     print queryId," ",queryName," ",entityName," ", systemName," ",nerG
                if systemName != "NIL":
                    cnt += 1
                    print queryId," ",queryName," ",entityName," ", systemName," ",nerG
        
    print cnt