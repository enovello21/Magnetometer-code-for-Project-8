#TEn11 mode
import numpy as np
import matplotlib.pylab as plt
from scipy.special import jvp,jnp_zeros

def T(r,theta,a,n,z):        
    return jvp(n,z*r/a,1)*np.cos(n*theta)   

def R(r,theta,a,n,z):
    return n*a*jvp(n,z*r/a,0)*np.sin(n*theta)/(z*r)
#a is the radius of the cavity
a = 4
n=0

z=jnp_zeros(n,1)
rlist=np.arange(0.1,a+0.1,0.1)   
thetalist=np.arange(0,2*np.pi+np.pi/10,np.pi/10)
rmesh,thetamesh = np.meshgrid(rlist, thetalist) #Generate a mesh

FullFunction = ((T(rmesh,thetamesh,a,n,z))**2+(R(rmesh,thetamesh,a,n,z))**2)**(0.5)
fig, ax = plt.subplots(dpi=120,subplot_kw=dict(projection='polar'))
ax.contourf(thetamesh, rmesh, FullFunction, 100,cmap='plasma')
