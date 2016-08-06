from funcs_logging import *
from funcs_GPIO import *
from config import *
import os

def deleteFile(filename):
        appendLog("deleteFile " + str(filename));
        os.remove(filename);

#timestamp dateien ueberwachen
def watchFolder():
	appendLog('watchFolder checking folder ' + str(FILE_FOLDER_WATCH));
	listfiles = [];
 	for name in os.listdir(FILE_FOLDER_WATCH):
    if os.path.isfile(os.path.join(FILE_FOLDER_WATCH, name)):
		  listfiles.append(os.path.join(FILE_FOLDER_WATCH, name));		

	appendLog('watchFolder size=' + str(len(listfiles)));
	if len(listfiles) > 0:
		for f in listfiles:
			parseFile(f);

# auf START und ENDe pruefen
# alles in eine Liste schreiben
# wenn START und ENDE da sind: alles an einen handler geben	
def parseFile(filename):
	appendLog('parseFile von ' + filename);
	if not filename.endswith('.action'):
		appendLog('parseFile ignored ' + filename + ' : wrong filetype');
		return;
    
  listAction = [];
  with open(filename, 'r') as fp:
    for line in fp:
			if len(line) > 0 and not line.startswith('#'):   #leerzeilen und kommentare
        appendLog('line:>' + line.strip() + '<');
				listAction.append(line.strip());
       
  if len(listAction) > 0 and listAction.pop(0) == "START" and listAction.pop() == "END":
    appendLog("Start and END found");
    deleteFile(filename);
    handleAction(listAction);
  else:
    appendLog("invalid file");