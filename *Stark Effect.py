#import (make class eventually)
from  matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import fsolve
from scipy import integrate
import math
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

#steps and how long
nsteps = 10000
final= 5
dt = final/nsteps


#constants
#mu = 9.1044*(10**(-28))
#e = 4.80320425*(10**(-10))
mu = 3.1
e = -20
hbar = 1.05457266*(10**(-27))
h=hbar*2*math.pi
epsilon = 0


#create empty arrays
xi  = np.zeros(nsteps)
eta = np.zeros(nsteps)
phi = np.zeros(nsteps)

xidot  = np.zeros(nsteps)
etadot = np.zeros(nsteps)
phidot = np.zeros(nsteps)

p_xi  = np.zeros(nsteps)
p_eta = np.zeros(nsteps)
p_phi = np.zeros(nsteps)

p_xidot  = np.zeros(nsteps)
p_etadot = np.zeros(nsteps)
p_phidot = np.zeros(nsteps)



#start conditions *EDIT*    xi   eta   phi  p_xi  p_eta  p_phi
initial_values = np.array([1.8, 1.2, .25, 1.1, .008, 8.0])





#evaluate derivatives
def evaluate(pq,t):
    
    xi,eta,phi,p_xi,p_eta,p_phi=pq

    xidot  = 4*p_xi*xi/(mu*(eta+xi))
    etadot = 4*p_eta*eta/(mu*(eta+xi))
    phidot = p_phi/(eta*mu*xi)

    p_xidot =  -(e*epsilon)/2-(2*(e**2)/(eta + xi)**2)-((-(p_phi**2/(eta*xi**2))-(4*p_eta**2*eta/(eta+xi)**2)-(4*p_xi**2*xi/(eta+xi)**2)+(4* p_xi**2/(eta+xi)))/(2*mu)) 
    p_etadot = (e*epsilon)/2-(2*(e**2)/(eta + xi)**2)-((-(p_phi**2/(eta**2*xi))-(4*p_eta**2*eta/(eta+xi)**2)-(4*p_xi**2*xi/(eta+xi)**2)+(4*p_eta**2/(eta+xi)))/(2*mu)) 
    p_phidot = 0

    return[xidot,etadot,phidot,p_xidot,p_etadot,p_phidot]


#create time values array
t = np.linspace(0,final,nsteps)

#use ODE solver to calculate all values
pq_t = integrate.odeint(evaluate, initial_values, t)


#turn array into variable lists
swappedpq_t=pq_t.swapaxes(0,1)
xi = swappedpq_t[0]
eta = swappedpq_t[1]
phi = swappedpq_t[2]

p_xi = swappedpq_t[3]
p_eta = swappedpq_t[4]
p_phi = swappedpq_t[5]



#Graph orbit   
xaxis = np.sqrt(xi*eta)
yaxis = np.array((xi - eta)/2)
plt.plot(xaxis, yaxis, label = 'Orbit')

midpointx=.5*(max(xaxis)+min(xaxis))
midpointy=.5*(max(yaxis)+min(yaxis))
rangex=(max(xaxis)-min(xaxis))
rangey=(max(yaxis)-min(yaxis))

#plt.xlim(midpointx-2*rangex,midpointx+2*rangex)
#plt.ylim(midpointy-2*rangey,midpointy+2*rangey)
plt.xlabel('√(x\N{SUPERSCRIPT TWO}+y\N{SUPERSCRIPT TWO})')
plt.ylabel('Z')
plt.title('Stark Effect Orbit Graph')
plt.legend()
plt.show()





#solve bounding parabola values
def equations(vars):
        
    x, y , a , b = vars

    hamiltonian = (1/(2*mu))*((4/(xi[0] + eta[0]))*(p_xi[0]*xi[0]*p_xi[0]) + (4/(xi[0] + eta[0]))*p_eta[0]*eta[0]*p_eta[0] + p_phi[0]**2/(xi[0]*eta[0])) - (2*e**2)/(xi[0] + eta[0]) + (1/2)*e*epsilon*(xi[0] - eta[0])

    eq1 = -x-y+(-2*xi[0]*(p_xi[0]**2)-((p_phi[0]**2)/(2*xi[0])) + (mu*(e**2)) - ((mu*e*epsilon*(xi[0]**2))/2) + mu*hamiltonian*xi[0] - (mu*(e**2)))/(mu*hamiltonian) 
    eq2 = -(x*y)-(p_phi[0]**2)/(2*mu*hamiltonian)

    eq3 = -a-b+(-(-2*xi[0]*(p_xi[0]**2)-((p_phi[0]**2)/(2*xi[0])) + (mu*(e**2)) + ((mu*e*epsilon*(xi[0]**2))/2) + mu*hamiltonian*xi[0]) - (mu*(e**2)))/(mu*hamiltonian)
    eq4 = -(a*b)-(p_phi[0]**2)/(2*mu*hamiltonian)

    return [eq1, eq2, eq3, eq4]


#plot bounding parabolas
def plot_parabolas():
    maxxivalue, minxivalue, maxetavalue, minetavalue = fsolve(equations, (.5, .5,.5,.5))

    q = np.arange(-10.0, 10.0, 0.001)

    z1=(maxxivalue**2 - q**2)/(2*maxxivalue)
    z2=(minxivalue**2 - q**2)/(2*minxivalue)

    z3=(-maxetavalue**2 + q**2)/(2*maxetavalue)
    z4=(-minetavalue**2 + q**2)/(2*minetavalue)

    plt.plot(q,z1, label='max ξ')
    plt.plot(q,z2, label='min ξ')
    plt.plot(q,z3, label='max η')
    plt.plot(q,z4, label='min η')

    plt.plot(xaxis, yaxis, label = 'Orbit')


    plt.xlim(midpointx-2*rangex,midpointx+2*rangex)
    plt.ylim(midpointy-2*rangey,midpointy+2*rangey)
    plt.xlabel('√(x\N{SUPERSCRIPT TWO}+y\N{SUPERSCRIPT TWO})')
    plt.ylabel('Z')
    plt.title('Stark Effect: Bounding Parabolas')
    plt.legend()
    plt.show()






#plot 3d orbit
def threedorbit():
    ax = plt.axes(projection ='3d')
     
    zaxis = (xi-eta)/2
    xaxis = np.sqrt(xi*eta)*np.cos(phi)
    yaxis = np.sqrt(xi*eta)*np.sin(phi)
    c = xaxis + yaxis
    ax.scatter(xaxis, yaxis, zaxis, c = c)
    ax.scatter(0, 0, 0)

    ax.set_title('3d Scatter plot geeks for geeks')
    plt.show()



#calculate alpha values from quantum numbers
def print_alphas(qn1,qn2,qn3):
    n_xi=qn1
    n_eta=qn2
    n_phi=qn3
    n_principal=n_xi+n_eta+n_phi

    I_xi=n_xi*h
    I_eta=n_eta*h
    I_phi=n_phi*h

    alpha1 = -2*(math.pi)**2*mu*e**4/(I_xi+I_eta+I_phi)**2
    alpha2 = mu*e**2*(I_eta-I_xi)/(I_xi+I_eta+I_phi)
    alpha3 = I_phi/(2*math.pi)

    realalpha1 = (1/(2*mu))*((4/(initial_values[0] + initial_values[1]))*(initial_values[3]*initial_values[0]*initial_values[3]) + (4/(initial_values[0] + initial_values[1]))*initial_values[4]*initial_values[1]*initial_values[4] + initial_values[5]**2/(initial_values[0]*initial_values[1])) - (2*e**2)/(initial_values[0] + initial_values[1]) + (1/2)*e*epsilon*(initial_values[0] - initial_values[1])
    realalpha3 = initial_values[5]
    realalpha2 = .5*(4*initial_values[1]*initial_values[4]**2+realalpha3**2/initial_values[1]-2*mu*e**2-2*mu*realalpha1*initial_values[1])

    print("necessary_alpha, actual_alpha\n", alpha1,realalpha1,'\n',alpha2,realalpha2,'\n',alpha3,realalpha3)


#calculate eccentricity
def get_eccentricity_and_energy_from_quantum_numbers(qn1,qn2,qn3):
    n_xi=qn1
    n_eta=qn2
    n_phi=qn3
    n_principal=n_xi+n_eta+n_phi
    sigma1=1/n_principal*(math.sqrt(n_xi*(n_xi+n_phi)))
    sigma2=1/n_principal*(math.sqrt(n_eta*(n_eta+n_phi)))
    energy = -mu*e**4/(2*n_principal**2*hbar**2)+3*epsilon*hbar**2/(2*e*mu)*(n_xi-n_eta)*n_principal
    if(n_xi==0 or n_eta==0):
        eccentricity=math.sqrt(sigma1**2+sigma2**2)
        return (eccentricity, energy)
    return energy
