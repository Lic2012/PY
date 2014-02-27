#!/usr/bin/python  
#-*-coding:utf-8-*- 
'''
Created on 2013Äê12ÔÂ24ÈÕ

@author: Administrator
@attention: 's 
'''

if __name__ == '__main__':
    pattern = "[\.|\?|!|,|:|;|\(|\)|\[|\]|\{|\}|\||\"|/|\\|\$|\-|<|>|&|@|\*|\d+|(')^s]"
    newline = re.sub(reg, " ", l)