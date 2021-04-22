import RPi.GPIO as GPIO
import time

D = [26,19,13,6,5,11,9,10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(D,GPIO.OUT)
GPIO.output(D,0)
GPIO.setup(17,GPIO.OUT)
GPIO.output(17,1)
GPIO.setup(4,GPIO.IN)
bin_depth = 8
a = [0]*255
for i in range(255):
    a[i] = i
mid = 128
low = 0
up = 255
def bin_convert(n):
    p = int(n/256)
    q = n%256
    X = bin(q+p)[2:].zfill(8)
    X = list(map(int, X))
    return X

def num2dac(x):   
    N = [0]*8
    N = bin_convert(x)
    GPIO.output(D, N)
    time.sleep(0.01)
    if GPIO.input(4) == 0:
        return 1 
    else:
        return 0

while low != up - 1:
    mid = (low + up) // 2
    if num2dac(a[mid]) == 1 :
        up = mid 
    else:
        low = mid 
    print(3.26 * (a[mid]/255))

print(3.26 * (a[mid]/255))

GPIO.cleanup