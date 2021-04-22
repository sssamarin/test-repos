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
    i = 2    
    N = [0]*8
    N = bin_convert(x)
    GPIO.output(D, N)
    time.sleep(0.01)
    if GPIO.input(4) == 0:
        i = 1
    else:
        i = 0



print('Кол-во повторений')
rep_num = int(input())
num2dac(rep_num)


GPIO.cleanup

while low != up:
    mid = (low + up) // 2
    if a[mid] > 0 : 
        
if low == up:
    print(3.26 * (value/255))