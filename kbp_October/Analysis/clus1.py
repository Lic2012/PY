#!/usr/bin/python  
#-*-coding:utf-8-*- 
'''
Created on 2013Äê12ÔÂ4ÈÕ

@author: Administrator
'''
import re
import time
import sys
class nil():
    q_dic = {} # id -> queryname
    l = []# nil id list
    exp_dic = {}
    
    def __init__(self, nilfile = "/home/rte/Public/wangrui/wr/KBP_2013/data/cluster/combine_nil2013", 
                 queryPath ="/home/rte/Public/wangrui/wr/KBP_2013/data/query/2013/query_info_2013", 
                 expandPath ="/home/rte/Public/wangrui/wr/KBP_2013/data/query/2013/query_expand_2013"):

        print "The default query path is : "+queryPath
        print "The default expand path is : "+expandPath
        print "The default nill path is : " +nilfile
        #initial nil list : l
        for line in open(nilfile):
            n = line.strip("\n\r")
            self.l.append(n)
        #initial query
        for line in open(queryPath):
            c = line.strip("\n\r").split("\t")
            queryId = c[0]
            queryName = c[1]
            self.q_dic[queryId] = queryName
        #initial expand
            reg = self.punc()
        for line in open(expandPath):
            c = line.strip("\n\r").split("\t")
            queryId = c[0]
            expandName = self.rmPunc(c[2], reg)
            self.exp_dic[queryId] = expandName
    ##remove punctuation
    def punc(self):
        fpunc = open("/home/rte/Public/wangrui/data/kbp/20131122_words2vect/punc")
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
    def rmPunc(self, l, reg):
        newline = re.sub(reg, "", l)
        return newline
    ## cluster method 1
    def cluster1(self):
        remode  = {}
        remode_list = []
        #starting in a cluster
        relation = []
        relation_nil = []
        for key in self.q_dic:
            if self.exp_dic.has_key(key):
                match = self.exp_dic[key]
            else:
                match = self.q_dic[key]
            remode[key] = match
            remode_list.append(key)
            
        for i in range(len(self.l)):
            flag = 1
            for j in range(i+1, len(self.l)):
                if remode[self.l[i]].lower() == remode[self.l[j]].lower():
                    flag = 0
                    if ([self.l[i],self.l[j]] not in relation) and ([self.l[j],self.l[i]] not in relation):
                        relation.append([self.l[i],self.l[j]])
            if flag == 1:
                relation_nil.append([self.l[i]])
        i = 0
        while i < len(relation):
            j = i + 1
            while j < len(relation):
                if relation[j][0] in relation[i]:
                    relation[i].append(relation[j][1])
                    relation.pop(j)
                    continue
                elif relation[j][1] in relation[i]:
                    relation[i].append(relation[j][0])
                    relation.pop(j)
                    continue
                j += 1
            i += 1
        print len(relation)
        print len(relation_nil)
        return relation + relation_nil
    
    def tofile(self,  method = 1, outdir = "/home/rte/Public/wangrui/wr/KBP_2013/data/cluster/"):
        print "the nil-cluster output dir is : " + outdir
        fname = "nil_cluster_" 
        self.date  = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        if method == 1:
            relation = self.cluster1()
            fname = fname + "method" + str(method) +"-" + self.date
            fout = open(outdir+fname, 'w')
            cnt = 1
            for item in relation:
                for item1 in item:
                    fout.write(item1+"\t"+"NIL"+str(cnt).zfill(4)+"\n")
                cnt += 1
            fout.close()
            
            self.nilOpath = outdir+fname
            print fname + " closed"
        else: pass
                
    def glue(self, ent = "/home/rte/Public/wangrui/wr/KBP_2013/data/classify/classify_result_2013_0411", 
             final = "/home/rte/Public/wangrui/data/kbp/20131125_sysResults/"):
        print "The default sys-ent-result file name is : " + ent
        print "The default finally result file name is :" + final + self.date
        list2 = open(self.nilOpath).readlines()
        list1 = open(ent).readlines()
        list1.extend(list2)
    
        f4 = open(final + self.date,"w")
        for line in list1:
            if len(line.strip('\n\r'))>0:
                c = line.strip("\r\n").split()
                f4.write(c[0] + '\t' + c[1] + '\n')
        f4.close()
        #print "glue cluster-result and rank-result done"                

if __name__ == '__main__':
    #whole nil queries
    #n.cluster1()
    if len(sys.argv) < 2:
        n = nil()
        n.tofile()
        n.glue()
    elif len(sys.argv) == 8:
        
        n = nil(sys.argv[1],sys.argv[2],sys.argv[3])
        n.tofile( sys.argv[5], sys.argv[4])
        n.glue(sys.argv[6], sys.argv[7])
    else:
        print "---------------------------Usage----------------------------"
        print "python clus1.py nilfile queryPath expandPath outdir method sysent finaldir"
        print "nilfile is system detected nils"
        print "queryPath is query infomation path"
        print "expandPath is query has expand path"
        print "outdir is write direction"
        print "method (int)is choose which clustering method"
        print "sysent is system entity linked result"
        print "finaldir is final result for evaluation combine sysent and nil-cluster result"
