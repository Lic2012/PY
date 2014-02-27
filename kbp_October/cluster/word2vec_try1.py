#!/usr/bin/python  
#-*-coding:utf-8-*- 
'''
Created on 2013Äê12ÔÂ24ÈÕ

@author: Administrator
@attention: use word2vec model to generate similarity between nils
'''
from gensim.models import word2vec
class simPrint():
    def __init__(self, nilfile = "/home/rte/Public/wangrui/wr/KBP_2013/data/cluster/combine_nil2013",
                 queryfile = "/home/rte/Public/wangrui/wr/KBP_2013/data/query/2013/query_info_2013"):
        self.nilfile = nilfile
        self.queryfile = queryfile
        self.nillist = []
        self.querydic= {}
        self.__setNil()
        self.__setIndex()
    def simBetween2(self, a,b):
        model=word2vec.Word2Vec.load("/home/rte/Public/wangrui/data/kbp/20131122_words2vect/1223model")
        return model.similarity(a,b)
    def printAll(self):
        while(True):
            content = raw_input("Input Nil:").strip("\r\n")
            if content == "EXIT" :break
            dic = {}
            for item in self.nillist:
                mention = self.querydic[item]
                dic[mention] = self.simBetween2(self.remode(content), self.remode(mention))
            for item in sorted(dic.iteritems(), key=lambda d:d[1], reverse = True ):
                print item[0],'\t',item[1]
            
    def __setNil(self):
        for line in open(self.nilfile):
            c = line.strip("\r\n")
            self.nillist.append(c)
    def __setIndex(self):
        for line in open(self.queryfile):
            c = line.strip("\r\n").split("\t")
            Id = c[0]
            name = c[1]
            self.querydic[Id] = name
    '''
    other application
    '''
    def remode(self,s):
        if s == "V-C-U": s ="V"
        if s == "Bosnia- Herzegovina": s = "Herzegovina"
        if s == "T. Tech" : s = "Tech"
        if s == "America's Finest City" : s = "America_Finest_City"
        if s == "B's" : s= "B"
        if s == "Gateway to the West" : return "'Gateway_to_the_West"
        return s.replace(' ','_').replace('.','')
if __name__ == '__main__':
    simprint = simPrint()
    simprint.printAll()