#encoding=utf-8
from symbol import if_stmt, try_stmt
from Worker import *;
import  math;
from _pyio import open
from locale import str
from sets import Set
from Db import *;
import os;
import re;
import logging as log

print 333;
try:
    1/0
except Exception ,e:
    log.error('error in test');
    log.critical('citical');
    log.basicConfig();
# file=open("C:/Users/gf/Desktop/kd.txt",mode="a",encoding= 'utf-8');
# file.write(u'wewweageag');
# file.close();
# db=Db().connection('root' ,'guanghuad' ,'bens');
# cur=db.cursor();
# cur.execute('select * from shop');
# for row in cur.fetchall():
#     #for value in row:
#      print(row[0]);
#          
# print dir(cur);
