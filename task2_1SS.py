import RPi.GPIO as GPIO
import time

D = [26,19,13,6,5,11,9,10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(D,GPIO.OUT)
GPIO.output(D,0)
bin_depth = 8
def bin_convert(n):
    p = int(n/256)
    q = n%256
    X = bin(q+p)[2:].zfill(8)
    X = list(map(int, X))
    return X

def num2dac(rep_num):
        while rep_num != 0 :
            for value in range(0,255):
                print(value)
                N = [0]*8
                N = bin_convert(value)
                GPIO.output(D, N)
                time.sleep(0.01)
            for value in range(255,-1,-1) :
                print(value)
                N = [0]*8
                N = bin_convert(value)
                GPIO.output(D, N)
                time.sleep(0.01)
            rep_num -= 1



print('Кол-во повторений')
rep_num = int(input())
num2dac(rep_num)


GPIO.cleanup
