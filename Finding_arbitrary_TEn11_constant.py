import scipy.integrate as integrate
from scipy.special import jvp,jnp_zeros
import numpy as np
a=0.01835640901#radius of cavity
d=0.1835640901#length of the cavity
n=0#TEn11 mode
#Comb_const is sqrt(1/(2*µ**2*epsilon)) 
Comb_const=189148761854
Power=1 #units in watts
Quality=10000 
angl_freq=2*np.pi*10**10
bessel_max_sqr=(jvp(n,jnp_zeros(n,1),0))**2+(jvp(n,jnp_zeros(n,1),1))**2
print(bessel_max_sqr)
def E(r,ø,z):
##Argument of integral E^2dv with constants factored out
##Constants are accounted for when calculating A+
##argument of sine is πz/d, second argument of jvp is jnp_zeros(0,1)*r/a
    return ((np.sin(np.pi*z/0.1835640901))**2)*((jvp(0,jnp_zeros(0,1)*r/0.01835640901,1))**2)*r
def E1_phi(r,ø,z):
    return (np.sin(np.pi*z/0.106))**2*(((jvp(1,jnp_zeros(1,1)*r/0.0439,1))**2)*((np.cos(ø))**2)*r)

def E1_rho(r,ø,z):
    return (np.sin(np.pi*z/0.106))**2*(0.0439*0.0439*(((jvp(1,jnp_zeros(1,1)*r/0.0439,0))**2)
    *((np.sin(ø))**2)/(r*(jnp_zeros(1,1))**2)))
#Below block integrates over the volume of cavity, finds A+ and finds fill factor
if n==0:
    I=integrate.tplquad(E,0,d,0,2*np.pi,0,a)
    A=Comb_const*jnp_zeros(0,1)*np.sqrt(Power*Quality/(I[0]*angl_freq**3))/a
    fill_factor=I[0]/(bessel_max_sqr*np.pi*d*a**2)
elif n==1:
    I=integrate.tplquad(E1_phi,0,d,0,2*np.pi,0,a)
    I1=integrate.tplquad(E1_rho,0,d,0,2*np.pi,0,a)
    A=Comb_const*jnp_zeros(1,1)*np.sqrt(Power*Quality/((I[0]+I1[0])*angl_freq**3))/a
    fill_factor=(I[0]+I1[0])/(bessel_max_sqr*np.pi*d*a**2)
print('A+ = ', A)
print('Fill Factor: ', fill_factor)