#!/bin/bash
#service bluetooth stop
#bluetoothd --compat &
#obexpushd -B -n &

sudo obexpushd -B -o /home/PredatorPythonServer/_files -n
