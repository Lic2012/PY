#!/usr/bin/python  
#-*-coding:utf-8-*- 
'''
Created on 2013Äê11ÔÂ25ÈÕ

@author: Administrator
'''
import os
if __name__ == '__main__':
    #nil file
    fin = open("/home/rte/Public/wangrui/wr/KBP_2013/data/cluster/combine_nil2013")
    src_dir ="/home/rte/Public/wangrui/wr/KBP_2013/data/query_text_2013/"
    des_dir = "/home/rte/Public/wangrui/data/kbp/20131125_nilsysQueryBackgroundDoc/"
    for line in fin:
        c = line.strip("\n\r").split("\t")
        os.system("cp "+src_dir+c[0]+" "+des_dir+c[0])
    fin.close