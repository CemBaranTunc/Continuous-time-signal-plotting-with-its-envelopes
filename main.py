#x(t) = 2e^(-0.5t)*e(J2πt)

import matplotlib.pyplot as plt
import numpy as np

def ub(t):
   return 2*np.e**(-0.5*t)

ubx = np.linspace(0, 10, num = 1000)
uby = ub(ubx)

def lb(t):
   return -2*np.e**(-0.5*t)

lbx = np.linspace(0, 10, num = 1000)
lby = lb(lbx)

def f(t):
   return 2*np.e**(-0.5*t)*np.cos(2*np.pi*t)

fx = np.linspace(0, 10, num = 1000)
fy = f(fx)

def i(t):
   return 2*np.e**(-0.5*t)*np.sin(2*np.pi*t)

ix = np.linspace(0, 10, num = 1000)
iy = i(ix)

plt.plot(ubx, uby, '--r', label = 'Envelopes')
plt.plot(lbx, lby, '--r')
plt.plot(fx, fy, 'b', label = 'Re{x(t)} = 2e$^{-0.5t}$cos(2πt)')
plt.plot(ix, iy, 'g', label = 'Im{x(t)} = 2e$^{-0.5t}$sin(2πt)')

plt.title('x(t) = 2e$^{-0.5t}$e$^{J(2πt)}$', style = 'italic')
plt.xlabel('t', style = 'italic')
plt.ylabel('x(t)', style = 'italic')
plt.grid(True)
plt.legend(loc = 'upper right')
plt.show()