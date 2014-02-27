#!/usr/bin/python  
#-*-coding:utf-8-*- 
'''
Created on 2013Äê12ÔÂ20ÈÕ

@author: Administrator
'''
import MySQLdb
class mySQL():
    def __init__(self):
        pass
    def search1(self):
        db = MySQLdb.connect(host="host_name", db="mysql", user="root", passwd="mysql")
        c = db.cursor()
        n = c.execute('''select * from S where NAME like '%Obama'''')
        for row in n.fetchall():
            for col in row:
                print col
    def search2(self):
        pass
    
    #other applications

if __name__ == '__main__':
    my_sql = mySQL()
    my_sql.search1()