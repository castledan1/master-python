from __future__ import division
import math
import matplotlib.pyplot as plt
import numpy as np

res = []
xArray = []

TG = 20
TC = 10
TW = 30
om = 3

P1 = .100
P2 = .0010
P3 = .00001
Q1 = 1000
Q2 = 2
Q3 = 1

plt.figure(figsize=(15, 10))
f, (ax, ax2) = plt.subplots(2, 1, sharey=False)


x = np.arange(-20,50.1,0.1)
ax.plot(x, np.exp( -0.5*( ( ( x-TG )/om )**2 ) ), linewidth=2)
ax.plot(x, np.exp( -0.5*( ( ( x-TC )/om )**2 ) ), linewidth=2)
ax.plot(x, np.exp( -0.5*( ( ( x-TW )/om )**2 ) ), linewidth=2)


x = []
y = []
ya=[]
for i in range(500):
    xi = i/10
    gauss1 = np.exp( -0.5*( ( ( xi-TC )/om )**2 ) )
    gauss2 = np.exp( -0.5*( ( ( xi-TG )/om )**2 ) )
    gauss3 = np.exp( -0.5*( ( ( xi-TW )/om )**2 ) )

    sal1 = (P1*xi+Q1)*gauss1
    sal2 = (P2*xi+Q2)*gauss2
    sal3 = (P3*xi+Q3)*gauss3

    a = gauss1+gauss2+gauss3
    b = sal1+sal2+sal3
    x.append( xi )
    y.append( a/b )

ax2 = plt.plot(x,y)
plt.show()