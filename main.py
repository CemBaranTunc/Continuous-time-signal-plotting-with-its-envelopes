#In this python module, I have defined, calculated and plotted an x(t) function which it's formula is: "x(t) = 2e^(-0.5t)*e(J2πt)" by using NumPy and Matplotlib.

import matplotlib.pyplot as plt
import numpy as np

#Upper envelope of x(t) has defined in the function right below.
def ub(t):
   return 2*np.e**(-0.5*t)

ubx = np.linspace(0, 10, num = 1000)
uby = ub(ubx)

#Lower envelope of x(t) has defined in the function right below.
def lb(t):
   return -2*np.e**(-0.5*t)

lbx = np.linspace(0, 10, num = 1000)
lby = lb(lbx)

#Real part of the x(t) has defined in the function right below.
def f(t):
   return 2*np.e**(-0.5*t)*np.cos(2*np.pi*t)

fx = np.linspace(0, 10, num = 1000)
fy = f(fx)

#Imaginary part of the x(t) has defined in the function right below.
def i(t):
   return 2*np.e**(-0.5*t)*np.sin(2*np.pi*t)

ix = np.linspace(0, 10, num = 1000)
iy = i(ix)

#Finally, I have plotted the x(t) function with it's envelopes, the real part and the imaginary part by using Matplotlib library.
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
