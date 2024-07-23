#TEn11 Quiver
import numpy as np
import matplotlib.pylab as plt
from scipy.special import jvp,jnp_zeros
a=4
n=1
z=jnp_zeros(n,1)
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

radii = np.arange(0.5, a+0.5,0.5)
thetas = np.arange(0, 2 * np.pi+np.pi/10,np.pi/10)
theta, r = np.meshgrid(thetas, radii)
U = n*a*jvp(n,z*r/a,0)*np.sin(n*theta)/(z*r) * np.cos(theta) - jvp(n,z*r/a,1)*np.cos(n*theta) * np.sin(theta)
V = n*a*jvp(n,z*r/a,0)*np.sin(n*theta)/(z*r) * np.sin(theta) + jvp(n,z*r/a,1)*np.cos(n*theta) * np.cos(theta)
C = np.hypot(U,V)



f = plt.figure()

ax = f.add_subplot(polar=True)
ax.quiver(theta,r,
          U, V, C,cmap='plasma')

plt.show()