# -*- coding: utf-8 -*-
"""
DIFFERENCE CALCULATOR

Created on Sat Jan 30 11:35:10 2021

@author: Dr. Waller
"""

from numpy import zeros, linspace, math
import matplotlib.pyplot as plt
from scipy import stats


dB = zeros(5)

# changeable vector
B = [490,390,295,232,182]

Bgraph = zeros(5)
Bexp = zeros(5)
t = linspace(0,4,5)
dt = 5
t_actual = linspace(0,4*dt,5)

for i in range (1,5):
    dB[i] = B[i] - B[i-1]
    Bgraph[i] = B[i-1]
    
print(B, Bgraph)
slope, intercept, r_value, p_value, std_err = stats.linregress(Bgraph, dB)

plt.figure(1)
plt.plot(Bgraph, dB, 'bo', Bgraph, intercept + slope*Bgraph)

plt.xlabel('B'); plt.ylabel('dB')
plt.legend(['data','regression line'], loc='upper left')
filestem= 'growth1_%dsteps' %5
plt.savefig('%s.png' % filestem); plt.savefig('%s.pdf' % filestem)

print('slope = ', slope, 'intercept = ', intercept)
plt.show()
plt.close()
plt.figure(2)
plt.xlabel('time');plt.ylabel('B')
tdouble = math.log(2)/math.log(1+slope)*dt
print('tdouble = ', tdouble)

K=math.log(2)/tdouble
Bexp[0] = B[0]

for i in range(0,5):
    Bexp[i] = B[0] * math.exp(K * t_actual[i])

plt.plot(t_actual, B, 'bo-', t_actual, B[0]*(1+slope)**t, t_actual, Bexp, 'ro')
plt.legend(['data', 'equation', 'exponential'], loc='upper left')
plt.figure(3)

















