# PredatorPythonServer für den C.H.I.P.

Python Version des Arduino Predator Servers

Überwacht einen konfigurierbaren Ordner auf .action-Dateien.

Gültige .action-Dateien werden ausgeführt und gelöscht.

Beispiel:
```
START
LED 1 ON
LED 2 ON
LED 3 ON
SERVO X 045
SERVO Y 090
SLEEP 5
LED 1 OFF
LED 2 OFF
LED 3 OFF
END
```

Die .action Dateien gelangen via Bluetooth-OBEX auf den C.H.I.P., siehe startObexServer.sh

Konfiguration und Mapping von LED Nr / Servo auf GPIO Port in config.py

Start mit `python main.py`


Benötigt folgende Abhängigkeiten:

CHIP_IO Python Library: https://github.com/xtacocorex/CHIP_IO

ObexPushD : https://sourceforge.net/projects/obexpushd/
