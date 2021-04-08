import RPi.GPIO as GPIO
import time

D = [26,19,13,6,5,11,9,10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(D,GPIO.OUT)
GPIO.output(D,0)
bin_depth = 8
try:
    def bin_convert(n):
        N = bin_depth -1 
        p = 0
        X = []
        while N > 0:
            p = int(n/(2**N))
            if p ==1 :
                X.append(1)
                n -=2**N
            else:
                X.append(0)
            N -= 1
        X.append(n)
        return X

    def num2dac(value):
        if value == -1:
            exit
        else:    
            print(value)
            p = int(value/256)
            q = value%256
            N = [0]*8
            N = bin_convert(q + p)
            # for i in range(0,bin_depth):
            GPIO.output(D, N)
                # print(D[i], N[i])
            time.sleep(0.01)

    print('Введите число(-1 для выхода):')
    j = int(input())
    num2dac(j)

finally:
    GPIO.cleanup
