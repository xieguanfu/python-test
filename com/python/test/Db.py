import MySQLdb;
import logging;
import sys;
class Db:
    def __init__(self):
        pass;
    def  connection(self,user,password,dbName):
            try:
                db=MySQLdb.connect(host='127.0.0.1' ,user=user,passwd=password,db=dbName,charset='utf8');
                return db;
            except Exception ,e:
                print e;
                sys.exc_info();
               # logging.log(level, msg);
    
    
        