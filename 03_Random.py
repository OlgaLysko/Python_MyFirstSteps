import math
import time
import random

A = 15
rzuty=0
miejsce=0

while abs(miejsce)<A:

    time.sleep(0.01)
    
    b=random.randint(0, 1)
    rzuty+= 1
       
    if miejsce<=0:
        print(' '*10,'|',' '*(A-abs(miejsce)-1),'*',' '*(abs(miejsce)+A), '|', miejsce)
    else:
        print(' '*10,'|',' '*A,' '*(miejsce-1),'*',' '*(A-miejsce-1),'|', miejsce)

    if b==0: miejsce+= -1
    else: miejsce+= 1

print('Ilosc rzutow: ', rzuty)

