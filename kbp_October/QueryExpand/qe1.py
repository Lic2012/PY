#!/usr/bin/python  
#-*-coding:utf-8-*- 
'''
Created on 2014年2月26日

@author: Administrator
'''
import string
class query():
    a_flag = 0 #1 equals is acronym
    name = ""
    id = ""
    can = []    
    def __init__(self):
        pass
    def acronym(self, s):
        upp = string.uppercase
        for chara in s:
            if chara not in upp:
                return 0
        return 1
         
            
        
class candidate():
    pass

if __name__ == '__main__':
    f = open("C:\Users\Administrator\Desktop\query_info_2013")
    
    q = query()
    
    q_dic = {}
    acronym_list = []
    for line in f:
        c = line.strip("\r\n").split("\t")
        queryname = c[1]
        queryid = c[0]
        ###build a dic  key is id value is queryname
        q_dic[queryid] = queryname
        if q.acronym(queryname):## if they are in query format
            acronym_list.append([queryid,queryname])

    print acronym_list
    print len(acronym_list)
#     background = "D:\\桌面待分类\\query_text_2013\\"        
#     for queryid in acronym_list:
#         f = open(background + queryid)
#         wordList = []
#         for line in f:
#             c = line.strip("\r\n").split(" ")
#             wordList.extend(c)
#         for i in range(len(wordList)):
#             if wordList[i]=="( "+queryid+" )":
#                 print queryid
    