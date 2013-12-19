#!/usr/bin/python  
#-*-coding:utf-8-*- 
'''
Created on 2013年11月22日

@author: Administrator
'''
#analysis for word2vect
#@system nil  and gold nil , print as same gold nil cluster
import re
import sys
class analysisNil():
    def __init__(self, goldPath="/home/rte/Public/wangrui/data/kbp/KBP2013Official/tac_2013/LDC2013E90_TAC_2013_KBP_English_Entity_Linking_Evaluation_Queries_and_Knowledge_Base_Links/data/tac_2013_kbp_english_entity_linking_evaluation_KB_links.tab",
                  queryPath = "/home/rte/Public/wangrui/data/kbp/20131114_analysis_ExpandAndNer/QueryInfo",
                  nilPath = "/home/rte/Public/wangrui/wr/KBP_2013/data/cluster/nil_cluster_method1-2013-12-05",
                  expandPath ="/home/rte/Public/wangrui/wr/KBP_2013/data/query/2013/query_expand_2013"):
        self.nilPath = nilPath
        self.q_dic = {}#key: ID ; value name
        self.g_dic = {}#key: queryID; value goldID
        self.exp_dic = {}#key:queryID; value expandname
        #@function :__buildNilResDic __buildSysResDic
        self.nilresR_dic = {}#key is sys-nil-cluster result; value queryId list// reverse
        self.golresR_dic = {}# key is gold standard nil class number; value is queryId list// reverse
        self.nilres_dic = {}#key is queryId, value is sys-nilcluster result

        self.__setQdic(queryPath)
        self.__setGdic(goldPath)
        self.__buildGolResDic(goldPath)
        self.buildNilResDic(nilPath)
        self.setExpandic(expandPath)

    def __setQdic(self, queryPath):
        #whole nil queries
        #prepare the query info dic

        for line in open(queryPath):
            c = line.strip("\n\r").split("\t")
            queryId = c[0]
            queryName = c[1]
            self.q_dic[queryId] = queryName
            
    def __setGdic(self, goldPath):
        fg = open(goldPath)        
        #prepare the gold
        for lg in fg:
            cg = lg.strip("\n\r").split("\t")
            queryId = cg[0]
            goldId = cg[1]
            self.g_dic[queryId] = goldId
    def setExpandic(self, expandPath):
        reg = self.punc()
        for line in open(expandPath):
            c = line.strip("\n\r").split("\t")
            queryId = c[0]
            expandName = self.rmPunc(c[2], reg)
            self.exp_dic[queryId] = expandName
    def buildNilResDic(self, nilPath):
        f = open(nilPath)
        for l in f:
            c = l.strip("\n\r").split("\t")
            queryId = c[0]
            nilId =  c[1]
            if not self.nilresR_dic.has_key(nilId):
                self.nilresR_dic[nilId]  = [queryId]
            else :
                self.nilresR_dic[nilId].append(queryId)
    def __buildGolResDic(self, goldPath):
        fg = open(goldPath)        
        #prepare the gold
        for lg in fg:
            cg = lg.strip("\n\r").split("\t")
            queryId = cg[0]
            goldId = cg[1]
            if not self.golresR_dic.has_key(goldId):
                self.golresR_dic[goldId] = [queryId]
            else : 
                self.golresR_dic[goldId].append(queryId)
    '''
    @mian applications
    '''
    #@description 找出那些id重复出现的query，生成错误
    def selectAppearMoreThanOnce(self, nilPath):
        f = open(nilPath)
        cnt_dic = {}
        allcorrect = 1 # 如果所有的出现次数都不大于1 ，该值为1 
        for l in f:
            c   = l.strip("\n\r").split("\t")
            queryId = c[0]
            if not cnt_dic.has_key(queryId):
                cnt_dic[queryId] = 1
            else:
                cnt_dic[queryId] += 1
               
        for keys in cnt_dic:
            if cnt_dic[keys] > 1:
                allcorrect = 0
                print keys,"\t"
        if allcorrect :
            print "All correct"
    #@description 系统生成的nil里有一部分是ent，一部分是nil；针对这部分nil，参照答案输出它们的聚类；
    def sameCluster(self, nilPath):
        fn = open(nilPath)
       
        all_nil = []
        for ln in fn:
            cn = ln.strip("\n\r").split("\t")
            queryId = cn[0]
            all_nil.append(queryId)
        
        for keys in all_nil:
            print self.q_dic[keys]," ",keys
            for keys1 in all_nil:
                if keys!=keys1:
                    if self.g_dic[keys] == self.g_dic[keys1]:
                        print self.q_dic[keys1]," ",keys1
            print "---------------------"
    #@description 系统生成的每一个nil 按照查询词ID 原始的表面字符串 扩充字符串  系统同类结果  答案同类结果输出， 目的是对扩充进行改进
    def sysCluster(self, nilPath):
        f = open(nilPath)
        for l in f:
            c = l.strip("\n\r").split("\t")
            queryId = c[0]
            nilId =  c[1]
            if self.exp_dic.has_key(queryId):
                expandname = self.exp_dic[queryId]
            else:
                expandname = "----"
            print queryId+"\t"+self.q_dic[queryId]+"\t"+expandname+"\n"
            ##add sth here
            print "\t"+nilId+"\t"+self.g_dic[queryId]
    #@description 将nil聚类的结果补充到系统提交最好的结果里，对新的结果进行评估,,,没有用！！！
    def nilToFinalRes(self, nilPath, outPath = "/home/rte/Public/wangrui/data/kbp/20131125_sysResults/2013-11-25-1" ,finalPath = "/home/rte/Public/wangrui/data/kbp/20131125_sysResults/SystemResult_finally"):
        fn = open(nilPath) 
        ff = open(finalPath)
        fo = open(outPath ,"w")
        nil_dic = {}
        final_dic = {}
        out_dic = {}
        #build nil dic , key is queryId , value is linked entities or cluster number
        for l in fn:
            c = l.strip("\n\r").split("\t")
            queryId = c[0]
            desLink = c[1]
            nil_dic[queryId] = desLink
        #build final answer dic, key is queryId , value is linked entities or cluster number
        for l in ff:
            c = l.strip("\n\r").split(" ")
            queryId = c[0]
            desLink = c[1]
            final_dic[queryId] = desLink
        cnt = 500
        for keys in final_dic:
            if cnt>0:
                out_dic[keys] = self.g_dic[keys]
                cnt -= 1
                continue
            if nil_dic.has_key(keys):
                out_dic[keys] = nil_dic[keys]
            else :
                out_dic[keys] = final_dic[keys]
        #write to outpath file
        for keys in out_dic:
            fo.write(keys+"\t"+out_dic[keys]+"\n")
        fn.close()
        ff.close()
        fo.close()

    '''
    @other applications
    '''
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
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Method not choose!:"
        print "Method 1: real nil in sys-nil and cluster them"
        print "Method 2: analysis each query , query ID , surface string, expand string, system same cluster, gold standard same cluster"
        print "Method 3: select queries appeared more than 1s"
        print "Method 4: add sys nil cluster result to finally result"
        print "Example: python analysisNil.py 1"
    else:
        ana = analysisNil()
        if sys.argv[1] == 1:
            #相同的聚类，对于sys生成的聚类结果，输出其中正确答案为nil的正确聚类结果，以-----分割
            ana.sameCluster()
        elif sys.argv[1] == 2:
            #系统生成的每一个nil 按照查询词ID 原始的表面字符串 扩充字符串  系统同类结果  答案同类结果输出， 目的是对扩充进行改进 还没弄完
            ana.sysCluster()
        elif sys.argv[1] == 3:
            #检查聚类的格式，将出现多于1次的queryId挑出来
            ana.selectAppearMoreThanOnce(ana.nilPath) 
        elif sys.argv[1] == 4:
            #将nil聚类结果和finally result结合
            ana.nilToFinalRes(ana.nilPath)
        else:
            print "Invalid Method number, Method number 1~4"
    