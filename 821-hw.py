import RPi.GPIO as GPIO
import time
import glob
import os

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

def RCtime(RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(.1)
    GPIO.setup(RCpin, GPIO.IN)
    while GPIO.input(RCpin) == GPIO.LOW:
        reading += 1
    return reading

BUTTON_PIN = 23
LDR_PIN = 21
BUZZER_PIN = 24
TEMP_THRESHOLD = 28.0
LIGHT_THRESHOLD = 4000


GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

lockout = False


def startSensing(channel):
    global lockout
    if lockout:
        return
    lockout = True
    print "Start sensing..."
    while True:
        temp_c, tempf = read_temp()
        print temp_c
        if temp_c > TEMP_THRESHOLD:
            break
    shout()
    


def shout():
    global lockout
    print "Start BUZZZZZZZ....."
    p = GPIO.PWM(BUZZER_PIN, 50)
    p.start(15)
    p.ChangeFrequency(600)
    while True:
        val = RCtime(LDR_PIN)
        print(val)
        if val > LIGHT_THRESHOLD:
            break
    p.stop
    print "STOP!!"
    lockout = False


GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=startSensing, bouncetime=500)

try:
    while True:
        None
except:
    GPIO.cleanup()
GPIO.cleanup()
