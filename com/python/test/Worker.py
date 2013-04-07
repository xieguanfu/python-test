'''
Created on 2013-4-5

@author: gf
'''

class Worker:
    '''
    classdocs
    '''
    def __init__(self,name):
       self.name=name;
       
    def call(self):
          print("name="+self.name); 
          
    def show(self,**av):     
         for v in av:
             print(v);
             print(av[v]);
        
if __name__=='__main__' :  
    Worker("aa").call();
    Worker("aa").show(tt='weag')


