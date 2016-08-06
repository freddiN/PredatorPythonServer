from funcs_logging import *
from funcs_file import *
from config import *
from funcs_GPIO import *
import time

#main: while schlife, thread sleep 100ms
startLog();
GPIOSetup();

while True:
	watchFolder();
	time.sleep(MAIN_SLEEP);

GPIOShutdown();
