import RPi.GPIO as GPIO
import time

D = [26,19,13,6,5,11,9,10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(D,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.output(D,0)
GPIO.output(17,1)
bin_depth = 8
try:
    def bin_convert(n):
        p = int(n/256)
        q = n%256
        X = bin(q+p)[2:].zfill(8)
        X = list(map(int, X))
        return X

    def num2dac(value):
        if value == -1:
            exit
        else:    
            print(3.26 * (value/255))
            p = int(value/256)
            q = value%256
            N = [0]*8
            N = bin_convert(q + p)
            GPIO.output(D, N)
            time.sleep(0.01)

    while True:
        print('Введите число(-1 для выхода):')
        j = int(input())
        num2dac(j)

finally:
    GPIO.cleanup