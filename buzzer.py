import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

# http://coopermaa2nd.blogspot.tw/2010/12/arduino-lab6.html
B0 = 31
C1 = 33
CS1 = 35
D1 = 37
DS1 = 39
E1 = 41
F1 = 44
FS1 = 46
G1 = 49
GS1 = 52
A1 = 55
AS1 = 58
B1 = 62
C2 = 65
CS2 = 69
D2 = 73
DS2 = 78
E2 = 82
F2 = 87
FS2 = 93
G2 = 98
GS2 = 104
A2 = 110
AS2 = 117
B2 = 123
C3 = 131
CS3 = 139
D3 = 147
DS3 = 156
E3 = 165
F3 = 175
FS3 = 185
G3 = 196
GS3 = 208
A3 = 220
AS3 = 233
B3 = 247
C4 = 262 # Do
CS4 = 277
D4 = 294 # Re
DS4 = 311
E4 = 330 # Mi
F4 = 349 # Fa
FS4 = 370
G4 = 392 # So
GS4 = 415
A4 = 440 # La
AS4 = 466
B4 = 494 # Si
C5 = 523 # Do
CS5 = 554
D5 = 587 # Re
DS5 = 622
E5 = 659 # Mi
F5 = 698 # Fa
FS5 = 740
G5 = 784 # So
GS5 = 831
A5 = 880 # La
AS5 = 932
B5 = 988 # Si
C6 = 1047 # Do
CS6 = 1109
D6 = 1175 # Re
DS6 = 1245
E6 = 1319 # Mi
F6 = 1397 # Fa
FS6 = 1480
G6 = 1568 # So
GS6 = 1661
A6 = 1760 # La
AS6 = 1865
B6 = 1976 # Si
C7 = 2093 # Do
CS7 = 2217
D7 = 2349
DS7 = 2489
E7 = 2637
F7 = 2794
FS7 = 2960
G7 = 3136
GS7 = 3322
A7 = 3520
AS7 = 3729
B7 = 3951
C8 = 4186
CS8 = 4435
D8 = 4699
DS8 = 4978

M_1 = C4
M_2 = D4
M_3 = E4
M_4 = F4
M_5 = G4
M_6 = A4
M_7 = B4
H_1 = C5
H_2 = D5
H_3 = E5
H_4 = F5
H_5 = G5
H_6 = A5
H_7 = B5

'''
http://www.chaodikong.com/article/2014/0917/article_26645.html
'''
def playLittleApple():
    p = GPIO.PWM(25, 50) # pin12(GPIO.BOARD) = GPIO14(GPIO.BCM)
    p.start(15) # 0 <= DV <= 100

    play(p, H_1, 0.5)
    play(p, H_1, 0.5)
    play(p, H_1, 0.5)
    play(p, H_1, 0.5)
    play(p, H_1, 0.5)
    play(p, H_1, 0.5)
    play(p, H_1, 0.5)
    play(p, M_6, 0.5)

    play(p, H_1, 0.5)
    play(p, H_1, 0.5)
    play(p, H_1, 0.5)
    play(p, H_1, 0.5)
    play(p, H_1, 0.5)
    play(p, H_1, 0.5)
    play(p, H_1, 0.5)
    play(p, M_5, 0.5)

    play(p, M_5, 0.5)
    play(p, M_5, 0.5)
    play(p, M_5, 0.5)
    play(p, M_5, 0.5)
    play(p, M_5, 0.5)
    play(p, M_6, 0.5)
    play(p, M_5, 0.5)
    play(p, M_6, 0.5)

    play(p, M_6, 4)

    play(p, H_1, 0.5)
    play(p, H_1, 0.5)
    play(p, H_1, 0.5)
    play(p, H_1, 0.5)
    play(p, H_1, 0.5)
    play(p, H_1, 0.5)
    play(p, H_1, 0.5)
    play(p, M_6, 0.5)

    play(p, H_1, 0.5)
    play(p, H_1, 0.5)
    play(p, H_1, 0.5)
    play(p, H_1, 0.5)
    play(p, H_1, 0.5)
    play(p, H_1, 0.5)
    play(p, H_1, 0.5)
    play(p, M_5, 0.5)

    play(p, M_5, 0.5)
    play(p, M_5, 0.5)
    play(p, M_5, 0.5)
    play(p, M_5, 0.5)
    play(p, M_5, 0.5)
    play(p, M_6, 0.5)
    play(p, M_5, 0.5)
    play(p, M_6, 0.5)

    play(p, M_6, 4)

    play(p, M_6, 0.5)
    play(p, M_6, 0.5)
    play(p, M_6, 0.5)
    play(p, M_7, 0.5)
    play(p, H_1, 0.5)
    play(p, H_3, 0.5)
    play(p, H_2, 0.5)
    play(p, H_1, 0.5)

    play(p, M_7, 0.5)
    play(p, M_6, 0.5)
    play(p, M_7, 0.5)
    play(p, M_6, 0.5)
    play(p, M_7, 0.5)
    play(p, M_7, 1.5)

    play(p, M_5, 0.5)
    play(p, M_5, 0.5)
    play(p, M_5, 0.5)
    play(p, M_6, 0.5)
    play(p, M_7, 0.5)
    play(p, H_2, 0.5)
    play(p, H_1, 0.5)
    play(p, M_7, 0.5)

    play(p, M_6, 0.5)
    play(p, M_5, 0.5)
    play(p, M_6, 0.5)
    play(p, M_5, 0.5)
    play(p, M_6, 2)

    play(p, M_6, 0.5)
    play(p, M_6, 0.5)
    play(p, M_6, 0.5)
    play(p, M_7, 0.5)
    play(p, H_1, 0.5)
    play(p, H_3, 0.5)
    play(p, H_2, 0.5)
    play(p, H_1, 0.5)

    play(p, M_7, 0.5)
    play(p, M_6, 0.5)
    play(p, M_7, 0.5)
    play(p, M_6, 0.5)
    play(p, M_7, 0.5)
    play(p, M_7, 1.5)

    play(p, M_5, 0.5)
    play(p, M_5, 0.5)
    play(p, M_5, 0.5)
    play(p, M_6, 0.5)
    play(p, M_7, 0.5)
    play(p, H_2, 0.5)
    play(p, H_1, 0.5)
    play(p, M_7, 0.5)

    play(p, H_1, 1)
    play(p, H_1, 1)
    play(p, H_1, 1)
    play(p, H_1, 1)

    play(p, H_3, 1)
    play(p, H_1, 1)
    play(p, H_2, 1)
    play(p, M_6, 1)

    play(p, H_3, 0.5)
    play(p, H_2, 0.5)
    play(p, H_1, 0.5)
    play(p, H_2, 0.5)
    play(p, M_6, 2)

    play(p, H_3, 1)
    play(p, H_1, 1)
    play(p, H_2, 1)
    play(p, H_2, 1)

    play(p, H_5, 0.5)
    play(p, H_3, 0.5)
    play(p, M_7, 1)
    play(p, H_1, 1)
    play(p, H_1, 0.5)    
    play(p, M_7, 0.5)  

    play(p, M_6, 1)
    play(p, M_7, 0.5)
    play(p, H_1, 0.5)
    play(p, H_2, 0.5)
    play(p, M_5, 0.5)
    play(p, M_5, 1) 

    play(p, H_6, 0.5)
    play(p, H_5, 0.5)
    play(p, H_3, 0.5)
    play(p, H_5, 0.5)
    play(p, H_3, 1)
    play(p, H_2, 1)

    play(p, H_1, 1)
    play(p, H_2, 0.5)
    play(p, H_3, 0.5)
    play(p, H_2, 0.5)
    play(p, H_3, 0.5)
    play(p, H_2, 0.5)  
    play(p, H_5, 0.5)  

    play(p, H_5, 1) 
    play(p, H_5, 1) 
    play(p, H_5, 1) 
    play(p, H_5, 1) 

    play(p, H_3, 1)
    play(p, H_1, 1)
    play(p, H_2, 1)
    play(p, M_6, 1)

    play(p, H_3, 0.5)
    play(p, H_2, 0.5)
    play(p, H_1, 0.5)
    play(p, H_2, 0.5)
    play(p, M_6, 2)

    play(p, H_3, 1)
    play(p, H_1, 1)
    play(p, H_2, 1)
    play(p, H_2, 0.5)
    play(p, H_2, 0.5)

    play(p, H_5, 0.5)
    play(p, H_3, 0.5)
    play(p, M_7, 1)
    play(p, H_1, 1)
    play(p, H_1, 0.5)    
    play(p, M_7, 0.5) 

    play(p, M_6, 1)
    play(p, M_7, 0.5)
    play(p, H_1, 0.5)
    play(p, H_2, 0.5)
    play(p, M_5, 0.5)
    play(p, M_5, 1) 

    play(p, H_6, 0.5)
    play(p, H_5, 0.5)
    play(p, H_3, 0.5)
    play(p, H_5, 0.5)
    play(p, H_3, 1)
    play(p, H_2, 1)

    play(p, H_1, 1)
    play(p, H_2, 0.5)
    play(p, H_3, 0.5)
    play(p, H_2, 0.5)
    play(p, M_5, 0.5)
    play(p, M_5, 1)  

    play(p, M_6, 1)
    play(p, M_6, 0.5)
    play(p, H_1, 0.5)
    play(p, M_6, 1)
    play(p, M_6, 1)

    p.stop
    GPIO.cleanup()

def play(p, frequency, tempo):
    p.ChangeFrequency(frequency)
    time.sleep(0.5 * tempo)

playLittleApple()

