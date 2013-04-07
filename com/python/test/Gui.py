 #coding=utf-8
import Tkinter;
import  MySQLdb;
class Gui(object):
    
    def __init__(self):
        top=Tkinter.Tk();
        quit=Tkinter.Button(top,text="退出",command=top.quit);
        quit.pack();
        Tkinter.mainloop(0);
        
gui=Gui();        
        