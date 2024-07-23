from scipy.special import jvp,jnp_zeros
import numpy as np
from matplotlib import pyplot as plt
n=1
µ=4*np.pi*10**(-7)
increments=10
us_freq=2*np.pi*2.45*10**9
Hammish_freq=2*np.pi*10**10
us_E_rho=[]
us_E_phi=[]
us_E=[]
Hammish_E_rho=[]
Hammish_E_phi=[]
Hammish_E=[]
if n==0:
    us_rad=0.09147515
    us_A=27.59382699
    Hammish_A=63.14674108
    Hammish_rad=0.01835640901
    print('TE011')
elif n==1:
    us_rad=0.0439
    us_A=67.11729276
    Hammish_A=198.90718699
    Hammish_rad=0.00888037
    print('TE111')
us_rho_values=np.linspace(0.001,us_rad,increments)
Hammish_rho_values=np.linspace(0.0001,Hammish_rad,increments)

def E_phi(a,µ,w,A,r,n):
    return 2*µ*w*A*a*np.cos(n*np.pi/4)*jvp(n,r*jnp_zeros(n,1)/a,1)/(jnp_zeros(n,1))
def E_rho(a,µ,w,A,r,n):
    return n*2*µ*w*A*a*a*np.sin(n*np.pi/4)*jvp(n,jnp_zeros(n,1)*r/a,0)/(r*(jnp_zeros(n,1))**2)
print('us')
print('phi, rho,  mag')
for i in range(0,increments):
    us_E_phi.append(E_phi(us_rad,µ,us_freq,us_A,us_rho_values[i],n))
    us_E_rho.append(E_rho(us_rad,µ,us_freq,us_A,us_rho_values[i],n))
    us_E.append(np.sqrt((us_E_phi[i])**2+(us_E_rho[i])**2))
    print( us_E_phi[i],'  ',us_E_rho[i],'  ',us_E[i])
print(' ')
print('Hammish')
print('phi,  rho,  mag')
for i in range(0,increments):
    Hammish_E_phi.append(E_phi(Hammish_rad,µ,Hammish_freq,Hammish_A,Hammish_rho_values[i],n))
    Hammish_E_rho.append(E_rho(Hammish_rad,µ,Hammish_freq,Hammish_A,Hammish_rho_values[i],n))
    Hammish_E.append(np.sqrt((Hammish_E_phi[i])**2+(Hammish_E_rho[i])**2))
    print( Hammish_E_phi[i],'  ',Hammish_E_rho[i],'  ',Hammish_E[i])
plt.plot(Hammish_rho_values,Hammish_E_phi, label='phi')
plt.plot(Hammish_rho_values,Hammish_E_rho, label='rho')
plt.plot(Hammish_rho_values,Hammish_E, label='mag')
plt.title('Hammish Fields')
plt.legend()
plt.show()
plt.plot(us_rho_values,us_E_phi, label='phi')
plt.plot(us_rho_values,us_E_rho, label='rho')
plt.plot(us_rho_values,us_E, label='mag')
plt.title('Our Fields')
plt.legend()
plt.show()