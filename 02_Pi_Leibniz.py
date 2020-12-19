import math

pi = 0
f = open('plik2.txt', 'w')

for i in range(1,10**7+1):
    
    pi+= 4*(-1)**(i-1)*(1/(2*(i-1)+1))

    if i <= 100  or i==10**3 or i==10**4 or i==10**5 or i==10**6 or i==10**7:
       f.write(str(i))
       f.write(') ')
       f.write(str(pi))
       f.write(', ')
       f.write(str(pi/math.pi))
       f.write('\n')


f.close()
