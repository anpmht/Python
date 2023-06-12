import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from math import acos, asin

def Function_of_z(phi_m, phi_p):
    return np.sin(phi_p)*np.cos(phi_m)

fig = plt.figure(figsize=(6, 6))

phi_m= np.linspace(0,20,90)
phi_p= np.linspace(0,20,90)

X, Y = np.meshgrid(phi_p, phi_m)
Z = Function_of_z(X, Y)

ax = fig.add_subplot(1, 1, 1, projection='3d')
p = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,cmap=matplotlib.cm.coolwarm, linewidth=0, antialiased=False)
cb = fig.colorbar(p, shrink=0.4)
plt.show()