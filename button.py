import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(23, GPIO.IN)

cnt = 0

def callback(channel):
    global cnt
    print cnt
    cnt += 1

GPIO.add_event_detect(23, GPIO.FALLING, callback=callback, bouncetime=200)  

try:
    while True:
        a = 1
except:
    GPIO.cleanup()
GPIO.cleanup()

