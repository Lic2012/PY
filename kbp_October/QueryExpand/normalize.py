#!/usr/bin/python  
#-*-coding:utf-8-*- 
'''
Created on 2013年12月17日

@author: Administrator
'''
import unicodedata
class Normal():
    latinDic_jianyin = {'Á': 'A', 'É':'E', 'Í':'I', 'Ó':'O', 'Ú':'U', 'Ý':'Y'}
    def __init__(self):
        pass
    def norm_yangxue(self, string):
        aim = string.replace(" ","")
        aim = aim.replace("(","")
        aim = aim.replace(")","")
        aim = aim.replace(".","")
        aim = aim.replace(",","")
        aim = aim.replace("'","")
        aim = aim.replace("\"","")
        aim = aim.replace(";","")
        aim = aim.replace("-","")
        aim = aim.replace("_","")
        aim = aim.replace(":","")
        aim = aim.lower()
        return aim
    def unicode_wangrui(self, s):
        return unicodedata.normalize('NFKD',s.decode()).encode('ascii','ignore')
    def latin_wangrui(self, s):
        pass
    def textOnScreen(self):
        while(1):
            content = raw_input("Input KB name:")
            if content == "EXIT": break
            print self.unicode_wangrui(content)
#             print self.norm_yangxue(content)
if __name__ == '__main__':
    nor = Normal()
    nor.textOnScreen()