#!/usr/bin/python  
#-*-coding:utf-8-*- 
'''
Created on 2013Äê11ÔÂ13ÈÕ

@author: Administrator

'''
import os

class Path():
    kbPath = "C:\Users\Administrator\Desktop\candidate_0728.info"
    systemResultPath = "C:\Users\Administrator\Desktop\SystemResult_pre"
    queryInfoPath = "C:\Users\Administrator\Desktop\QueryInfo"
    NERtaggerPath = "C:\Users\Administrator\Desktop\NERtagger"
    goldStandardPath = "C:\Users\Administrator\Desktop\GoldStandard.tab"
    expandPath = "C:\Users\Administrator\Desktop\QueryExpand"
    def test(self):
        print os.path.isfile(self.kbPath),
        print os.path.isfile(self.systemResultPath),
        print os.path.isfile(self.queryInfoPath),
        print os.path.isfile(self.NERtaggerPath),
        print os.path.isfile(self.goldStandardPath),
        print os.path.isfile(self.goldStandardPath),
class Query():
    id  = ""
    name = ""
    nerTagger = ""
    expandName = ""
    genre = ""
    wiki = ""
    source = ""
    
    linkId_system = ""
    linkName_system = ""
    linkId_gold = ""
    linkName_gold = ""
    ner_gold = ""

class QueryCollection():
    querycnt = 0
    querylist = []
    def queryAppend(self, q):
        self.querylist.append(q)
        self.querycnt+=1
    def findNameIs(self, Id):
        for query in self.querylist:
            if query.id==Id:
                return query
        print "not find query!"
    def addEntityName(self, dic):
        for query in self.querylist:
            if query.linkId_system.startswith("N"):
                query.linkName_system = "NIL"
            else:
                query.linkName_system = dic[query.linkId_system]
            if query.linkId_gold.startswith("N"):
                query.linkName_gold = "NIL"
            else:
                query.linkName_gold = dic[query.linkId_gold]
    def output(self, outfile):
        for query in self.querylist:
            outfile.write(query.id+"\t"+query.linkId_gold+"\t"+query.name+"\t"+query.linkName_gold+"\t"+query.ner_gold+"\t"+query.genre+"\t"+query.wiki+"\t"+query.source+"\n")
            if query.expandName!="":
                outfile.write("             "+"\t"+query.linkId_system+"\t"+query.name+"\t"+query.linkName_system+"\t"+query.nerTagger+"\t"+query.expandName+"\n")
            else:
                outfile.write("             "+"\t"+query.linkId_system+"\t"+query.name+"\t"+query.linkName_system+"\t"+query.nerTagger+"\t"+"NULL"+"\n")

    def outputExpand(self, outfile):
        for query in self.querylist:
            if query.expandName!="":
                outfile.write(query.id+"\t"+query.linkId_gold+"\t"+query.name+"\t"+query.linkName_gold+"\t"+query.ner_gold+"\t"+query.genre+"\t"+query.wiki+"\t"+query.source+"\n")
                outfile.write("             "+"\t"+query.linkId_system+"\t"+query.name+"\t"+query.linkName_system+"\t"+query.nerTagger+"\t"+query.expandName+"\n")


if __name__ == '__main__':
    Path().test()
    qc  = QueryCollection() #initialize
    path = Path()
    #query info
    query_f = open(path.queryInfoPath)
    for line in query_f:
        #print line
        chunk = line.strip("\n\r").split("\t")
        queryId = chunk[0]
        queryName = chunk[1]
        q = Query()
        q.id = queryId
        q.name = queryName
        qc.queryAppend(q)
#     for item in qc.querylist:
#         print item.id + " " +item.name
    #ner tagger
    nerTagger_f = open(path.NERtaggerPath)
    for line in nerTagger_f:
        chunk = line.strip("\n\r").split("\t")
        queryId = chunk[0]
        queryName = chunk[1]
        nerTagger = chunk[2]
        q = qc.findNameIs(queryId)
        q.nerTagger = nerTagger
#     for item in qc.querylist:
#        print item.id + " " +item.name+" "+item.nerTagger     
    #expand name
    expandName_f = open(path.goldStandardPath)
    for line in expandName_f:
        chunk = line.strip("\n\r").split("\t")
        queryId = chunk[0]
        linkId = chunk[1]
        ner_gold = chunk[2]
        source = chunk[3]
        genre = chunk[4]
        wiki = chunk[5]
        q = qc.findNameIs(queryId)
        q.linkId_gold = linkId
        q.ner_gold = ner_gold
        q.genre = genre
        q.wiki = wiki
        q.source = source
#     for item in qc.querylist:
#        print item.id + " " +item.linkId_gold+" "+item.ner_gold+" "+item.genre+" "+ item.wiki+" " + item.source  
    #system result
    systemResult_f = open(path.systemResultPath)
    for line in systemResult_f:
        chunk = line.strip("\n\r").split("\t")
        queryId = chunk[0]
        try:
            linkId = chunk[1]
        except IndexError:
            print line
        q = qc.findNameIs(queryId)
        q.linkId_system = linkId
#     for item in qc.querylist:
#        print item.id + " " +item.linkId_system
    # expand file
    expand_f = open(path.expandPath)
    for line in expand_f:
        chunk = line.strip("\n\r").split("\t")
        queryId = chunk[0]
        queryName = chunk[1]
        queryExpand = chunk[2]
        q = qc.findNameIs(queryId)
        q.expandName = queryExpand
#     for item in qc.querylist:
#         if item.expandName!="":
#             print item.id + " " +item.expandName
    # kb entity name
    kbPath_f = open(path.kbPath)
    kb_dic = {}
    for line in kbPath_f:
        chunk = line.strip("\n\r").split("\t")
        kb_dic[chunk[2]] = chunk[0]
    qc.addEntityName(kb_dic)
    
    
    ##output
    outfile = open("C:\Users\Administrator\Desktop\ExpansionAnalysis",'w')
    qc.output(outfile)
    outfile_exp = open("C:\Users\Administrator\Desktop\ExpansionAnalysis_onlyExpand_pre",'w')
    qc.outputExpand(outfile_exp)
    