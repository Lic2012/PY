#!/usr/bin/python  
#-*-coding:utf-8-*- 
'''
Created on 2013Äê11ÔÂ26ÈÕ

@author: Administrator
'''

'''
@Description: deal with punctuation mark
'''
import re
import sys
#@return : regular expression
def punc():
    fpunc = open("C:\\Users\\Administrator\\Desktop\\punc")
#    fpunc = open("/home/rte/Public/wangrui/data/kbp/20131122_words2vect/punc")
    puncList = []
    for line in fpunc:
        puncList.append(line.strip("\n\r"))
    fpunc.close()
    s = "["+puncList[0]
    for item in puncList[1:]:
        s += "|"+item
    s += "]"
    reg =  re.compile(s)
    return reg
#replace punctuation to space
def rmPunc(l, reg):
    newline = re.sub(reg, " ", l)
    return newline
'''
@Description: remove stop-words
'''
def stpw():
    fstpw = open("C:\\Users\\Administrator\\Desktop\\stpwords")
#    fstpw = open("/home/rte/Public/wangrui/data/kbp/20131122_words2vect/stpwords")
    stpList = []
    for line in fstpw:
        stpList.append(line.strip("\n\r"))
    fstpw.close()
    s =  "("+"\'s|s\'|"+'\\b'+stpList[0]
    for item in stpList[1:]:
        s += '\\b'+"|"+'\\b'+item
    s += '\\b'+")"
    print s
    reg = re.compile(s, re.IGNORECASE)
    return reg
#replace stop-words to null 
def rmStpw(l, reg):
    newline = re.sub(reg, "", l)
    return newline

'''
@Description: 
'''


if __name__ == '__main__':
    reg1 = punc()
    reg2 = stpw()
    f = open(sys.argv[1])
    f_out = open(sys.argv[2], 'w')
    for line in f:
        line1 =  rmPunc(line, reg1)
        f_out.write(rmStpw(line1, reg2))
    f_out.close()
    f.close()
     
#     