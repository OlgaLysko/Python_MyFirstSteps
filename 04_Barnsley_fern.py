import matplotlib.pyplot as plt
import random

x0 = []
y0 = []
x0.append(0)
y0.append(0)

for i in range(0, 10**6-1):

    r = random.randint(1,100)

    if r>=1 and r<=85:
        x0.append(0.85*x0[i] + 0.04*y0[i])
        y0.append(-0.04*x0[i] + 0.85*y0[i] +1.6)
    if r>=86 and r<=92:
        x0.append(0.2*x0[i] - 0.26*y0[i])
        y0.append(0.23*x0[i] + 0.22*y0[i] + 1.6)
    if r>=93 and r<=99:
        x0.append(-0.15*x0[i] + 0.28*y0[i])
        y0.append(0.26*x0[i] + 0.24*y0[i] + 0.44)
    if r==100:
        x0.append(0)
        y0.append(0.16*y0[i])


plt.plot(x0, y0, ',', color='Lime')
plt.gca().set_facecolor("black")
plt.show()
