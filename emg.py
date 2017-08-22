from __future__ import print_function
import time
import grovepi
import os

WIDTH = 30

def draw(arr):
    MIDDLE = 350
    os.system('clear')
    board = [ [' ' for i in range(WIDTH)] for i in range(len(arr))]
    for i in range(len(arr)):
        idx = MIDDLE-arr[i]
        if idx > WIDTH-1:
            idx = WIDTH-1
        elif idx < 0:
            idx = 0
        board[i][idx] = '*'
    for i in range(WIDTH):
        for j in range(len(arr)):
            print(board[j][i], end='')
        print('')

sensor = 14
grovepi.pinMode(sensor,"INPUT")

arr = []

while True:
    try:
        val = grovepi.analogRead(sensor)
        arr.append(val)
        if len(arr) > 120:
            arr.pop(0)
        draw(arr)
        print(val)
        time.sleep(0.2)
    except KeyboardInterrupt:
        break
    except IOError:
        print("Error")

