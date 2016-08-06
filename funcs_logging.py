from config import *
import time

def startLog():
   f = open(FILE_LOGGING, 'w');
   f.write("gestartet " + time.strftime("%d.%m.%Y %H:%M:%S") + "\r\n");
   #f.write("GPIO = " + str(gpio_port) + "\n");
   #f.write("Max Schleife = " + str(max_schleife) + "\n");
   #f.write("Timeout = " + str(sleep_secs) + "\n");
   f.flush();
   f.close();
   return;

def appendLog(logme):
   f = open(FILE_LOGGING, 'a');
   f.write(time.strftime("%d.%m.%Y %H:%M:%S") + " : " + logme + "\r\n");
   f.flush();
   f.close();
   return ;

