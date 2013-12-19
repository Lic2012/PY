#!/usr/bin/python  
#-*-coding:utf-8-*- 
'''
Created on 2013Äê12ÔÂ4ÈÕ

@author: Administrator
'''
import os
import re
class pCorpus():
    def __init__(self):
        self.flist = []
        self.__dirWalk()
        self.reg = re.compile("(\([^\(|^\)]*\))")
    def __dirWalk(self, des = "C:\\Users\\Administrator\\Desktop\\"):
        fnamelist = ['00','01']
        for fname in fnamelist:
            tri = os.walk(des+fname)
            for i in tri:
                for j in i[2]:
                    self.flist.append(i[0]+"\\"+j)
    def antiParse(self, out = "C:\\Users\\Administrator\\Desktop\\out.txt"):
        f = open(out, "a")
        for fname in self.flist:
            line_list = open(fname).readlines()
            line = ""
            for i in line_list:
                line += i.strip("\n\r")
            wordlist =  self.reg.findall(line)
            newline = ""
            for j in wordlist:
                c = j.strip("()").split(" ")
                tag = c[0]
                word = c[1]
                newline += word+"_"+tag+" "
            f.write(newline+"\n")
            #print line
        f.close()
if __name__ == '__main__':
    p = pCorpus()
    p.antiParse()