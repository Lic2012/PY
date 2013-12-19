#!/usr/bin/python  
#-*-coding:utf-8-*- 
'''
Created on 2013Äê12ÔÂ17ÈÕ

@author: Administrator
'''
class LossInKB():
    def __init__(self):
        self.big = []
        self.small = []
        self.readSmall()
        self.readBig()
        
    def readSmall(self,fb = "C:\\Users\\Administrator\\Desktop\\candidate_info_0313"):

        for line in open(fb):
            c = line.strip("\r\n").split("\t")
            ID = int(c[0].lstrip("E0"))
            self.small.append(ID)

    def readBig(self, fs = "C:\\Users\\Administrator\\Desktop\\candidate_0728.info"):
        for line in open(fs):
            c = line.strip("\r\n").split("\t")
            ID = int(c[2].lstrip("E0"))
            self.big.append(ID)

    def notIn(self):
        for item in self.small:
            self.big.remove(item)
        if len(self.big):
            print self.big
    
if __name__ == '__main__':
    loss = LossInKB()
    loss.notIn()