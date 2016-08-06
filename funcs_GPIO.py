from funcs_logging import *
from config import *
import CHIP_IO.GPIO as GPIO
import CHIP_IO.SOFTPWM as SPWM
import time

def GPIOSetup():
	GPIO.setup(GPIO_LED_1, GPIO.OUT);
	GPIO.setup(GPIO_LED_2, GPIO.OUT);
	GPIO.setup(GPIO_LED_3, GPIO.OUT);
	GPIO.setup(GPIO_SERVO_X, GPIO.OUT);
	GPIO.setup(GPIO_SERVO_Y, GPIO.OUT);

def GPIOShutdown():
	GPIO.cleanup();

def handleAction(actions):
	appendLog('handleAction size=' + str(len(actions)));
	for action in actions:
		if action.startswith('LED'):
			handleLED(action[4:]);
		elif action.startswith('SERVO'):
			handleServo(action[6:]);
		elif action.startswith('SLEEP'):
			handleSleep(action[6:]);
		else:
			appendLog('Unknown action:' + action);

def handleSleep(action):
	appendLog('handleSleep >' + action + '<');
	time.sleep(int(action));

def handleLED(led):
	appendLog('handleLED >' + led + '<');
	nLED = led[0:1];
        actionLED = led[2:];
	appendLog('handleLED nr=' + nLED + ' action=' + actionLED);
	
	strPort = '';
	nAction = 0;

	if nLED == '1':
		strPort = GPIO_LED_1;
	elif nLED == '2':
                strPort = GPIO_LED_2;
	elif nLED == '3':
                strPort = GPIO_LED_3;

	if actionLED == 'ON':
		nAction = GPIO.HIGH;
	elif actionLED == 'OFF':
		nAction = GPIO.LOW;

	GPIO.output(strPort, nAction);


def handleServo(servo):
	appendLog('handleServo ' + servo);
	axis = servo[0:1];
	angle = servo[2:];
	appendLog('handleServo axis=' + axis + ' angle=' + angle);
	
	strPort = '';

	if axis == 'X':
		strPort = GPIO_SERVO_X;
	elif axis == 'Y':
		strPort = GPIO_SERVO_Y;

	#SPWM.start(strPort, 50)
	#SPWM.set_duty_cycle(strPort, 25.5)
	#SPWM.set_frequency(strPort, 10)
	#SPWM.stop(strPort)
