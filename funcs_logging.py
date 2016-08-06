from config import *
import time

def startLog():
   f = open(FILE_LOGGING, 'w');
   f.write("gestartet " + time.strftime("%d.%m.%Y %H:%M:%S") + "\r\n");
   f.flush();
   f.close();
   return;

def appendLog(logme):
   f = open(FILE_LOGGING, 'a');
   f.write(time.strftime("%d.%m.%Y %H:%M:%S") + " : " + logme + "\r\n");
   f.flush();
   f.close();
   return ;

