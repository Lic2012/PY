#!/usr/bin/python  
#-*-coding:utf-8-*- 
'''
Created on 2013��12��24��

@author: Administrator
@attention: 's 
'''

if __name__ == '__main__':
    pattern = "[\.|\?|!|,|:|;|\(|\)|\[|\]|\{|\}|\||\"|/|\\|\$|\-|<|>|&|@|\*|\d+|(')^s]"
    newline = re.sub(reg, " ", l)