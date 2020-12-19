import random
import math

x = []
y = []
No = 0
Nk = 0
f = open('plik1.txt', 'w')

for i in range(1,10**6+1):
   x.append(random.uniform(-1,1))
   y.append(random.uniform(-1,1))

   Nk+=1

   if ((x[i-1]**2+y[i-1]**2)**0.5) <= 1 : No+=1
   
   pi = No/Nk*4

   if i <= 100  or i==10**3 or i==10**4 or i==10**5 or i==10**6:
       f.write(str(i))
       f.write(') ')
       f.write(str(pi))
       f.write(', ')
       f.write(str(pi/math.pi))
       f.write('\n')


f.close()
