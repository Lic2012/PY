#!/usr/bin/python  
#-*-coding:utf-8-*- 
'''
Created on 2013Äê11ÔÂ28ÈÕ

@author: Administrator
'''


'''
@return : a dict , keys are query-IDs, value is query-Name
'''
import re
def queryDict(queryPath):
    #prepare the query info dict
    q_dic = {} #key: ID ; value name
    for line in open(queryPath):
        c = line.strip("\n\r").split("\t")
        queryId = c[0]
        queryName = c[1]
        q_dic[queryId] = queryName
    return q_dic
'''
@return : a dict , keys are query-IDs, value is ExpandName
'''
def expandDict(expandPath):
    exp_dic = {}
    for line in open(expandPath):
        c = line.strip("\n\r").split("\t")
        queryId = c[0]
        expandName = c[2]
        exp_dic[queryId] = expandName
    return exp_dic
'''
@return: 
@param nilPath:  contains all System-generated NILs
@param pairs: if nil is {A,B,C}, pairs is [[A,B],[A,C],[B,C]] 
@param line: if nil is {A,B,C}, line is [A,B,C]
'''
def nilPairs(nilPath):
    pairs = []
    line = []
    for line in open(nilPath):
        n = line.strip("\n\r")
        line.append(n)
    for i in range(len(line)):
        for j in range(i,len(line)):
            pairs.append([line[i], line[j]])
    return pairs

def generatePairs2(nilPath, queryPath, expandPath, output):
    q_dic = queryDict(queryPath)
    npairs = nilPairs(nilPath)
    exp_dic = expandDict(expandPath)
    reg = punc()
    
    fout = open(output, "w")
    for p in npairs:
        for item in p:
            if (exp_dic.has_key(item[1])):
                expandName = exp_dic[item[1]] # item[1] is query id
                q_dic[item[1]] = rmPunc(expandName, reg) #remove punc, such as ,.?" and so on
            if (exp_dic.has_key(item[2])):
                expandName = exp_dic[item[2]] # item[1] is query id
                q_dic[item[2]] = rmPunc(expandName, reg) #remove punc, such as ,.?" and so on
            fout.write(item[1]+"\t"+item[2]+"\t"+q_dic[item[1]]+"\t"+q_dic[item[2]]+"\n")
    fout.close()
    
def punc():
#    fpunc = open("C:\\Users\\Administrator\\Desktop\\punc")
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
#replace punctuation to space
def rmPunc(l, reg):
    newline = re.sub(reg, "", l)
    return newline
if __name__ == '__main__':
    #whole nil queries
    nilPath = "/home/rte/Public/wangrui/wr/KBP_2013/data/cluster/combine_nil2013"
    
    #query info
    queryPath ="/home/rte/Public/wangrui/data/kbp/20131114_analysis_ExpandAndNer/QueryInfo"

    #expand query info
    expandPath ="/home/rte/Public/wangrui/wr/KBP_2013/data/query/2013/query_expand_2013"
    #output file
    output = "/home/rte/Public/wangrui/data/kbp/20131125_analysis_NIL/nilpairs"
    #build query information dict

    generatePairs(nilPath, queryPath, expandPath, output)
    
    
    