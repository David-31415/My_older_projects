
# #Quantum vs. Classical1 vs. Classical2 power for the circular case

# figure(num=None, figsize=(15, 7), dpi=80, facecolor='w', edgecolor='k')
# max=50

# #powerq    
# n0=2
# n1=1
# l=1

# m = Decimal(9.109*(10**(-31)))
# hbar = Decimal(1.0546*(10**(-34)))
# e = Decimal(1.602*(10**(-19)))
# c = Decimal(2.998*(10**8))
# epsilon0 = Decimal(8.854*(10**(-12)))
# ecgs = Decimal(4.803*10**-10)
# Ry = Decimal(3.2898*10**15)
# mcgs = Decimal(9.109*10**-28)
# hbarcgs = Decimal(1.055*10**-27)
# acgs = Decimal(5.2917*10**-9)

# powerqs = []
# for n0 in range(2, max+1, 1):
#     n0=n0
#     n1=n0-1
#     l=n0-1
#     x = (-4*n0*n1)/((n0-n1)**2)
#     dif1 = Decimal((-1)**(n1-l)/(4*Decimal((math.factorial(2*l-1)))))
#     dif2 = Decimal(((math.factorial(n0+l)*math.factorial((n1+l-1)))//(math.factorial(n0-l-1)*math.factorial(n1-l)))).sqrt()
#     dif3 = Decimal((Decimal((4*n0*n1)**(l+1)))*(Decimal((n0-n1)**(n0+n1-2*l-2)))/((n0+n1)**(n0+n1)))
#     dif4 = Decimal(sc.hyp2f1((1+l-n0), (l-n1), (2*l), x))
#     dif5 = Decimal((((n0-n1)/(n0+n1))**2)*sc.hyp2f1((l-1-n0), (l-n1), (2*l), x))
#     dif = dif1*dif2*dif3*(dif4-dif5)
#     n0=Decimal(n0)
#     n1=Decimal(n1)
#     l=Decimal(l)
#     freqq = m*e**4/(Decimal(2)*(Decimal(4*np.pi)*epsilon0)**2*hbar**3)*((Decimal(1)/n1**2)-(Decimal(1)/n0**2))
#     f = Decimal(1/3)*l/Decimal(2*l+1)*freqq/(Ry*Decimal(2*np.pi))*dif**2
#     einstein = Decimal(8*10**9)*(freqq/(Decimal(2*np.pi)*Ry))**2*f
#     powerq = hbar*freqq*einstein
#     powerqs.append(float(powerq))
# n0 = np.arange(2, max+1)
# plt.plot(n0, np.log10(powerqs), 'ro', markersize=7, label="Quantum", zorder=3)

# #powerc

# n0=2
# l=n0-1
# k=1

# m = 9.109*(10**(-31))
# hbar = 1.0546*(10**(-34))
# e = 1.602*(10**(-19))
# c = 2.998*(10**8)
# epsilon0 = 8.854*(10**(-12))

# n0 = np.arange(2, max+1)
# l=n0-1
# epsilon = np.sqrt((1-(l*(l+1)/(n0**2)))) #unitless
# z = k*epsilon #unitless

# def J(z):
#     return special.jv(k, z)
# Jprime = misc.derivative(J, z, dx=1e-6)
# Jsquared = (J(z))**2
# freqc = m*e**4/((4*np.pi*epsilon0)**2*hbar**3*n0**3)
# a = (n0**2)*4*np.pi*epsilon0*(hbar**2)/(m*(e**2)) #meters
# P1 = (e**2)/(3*(c**3)*np.pi*epsilon0)
# P2 = ((k*freqc)**4)*(a**2)/(k**2)
# P3 = Jprime**2
# P4 = ((1-(epsilon**2))/(epsilon**2))*Jsquared
# P = P1*P2*(P3+P4)
# powerc = (2/3)*freqc**4*hbar**4*4*np.pi*epsilon0*n0**4/(m**2*c**3*e**2)
# plt.plot(n0, np.log10(P), 'bo', markersize=7, label = "Semi-Classical ($\u2113=n-1$)")
# plt.plot(n0, np.log10(powerc), 'go', markersize=7, label = "Semi-Classical ($\epsilon=0$)")
# plt.xlabel('Initial Value of $n$')
# plt.ylabel('Spectral Power Density [watts]')
# plt.title('Log10 of Circular Orbit Radiation')
# plt.legend()
# plt.grid(True)
# plt.show()
# print(powerqs)
# print(P)
# print(powerc)

# #Quantum vs. Classical Frequency for the circular case

# figure(num=None, figsize=(15, 7), dpi=80, facecolor='w', edgecolor='k')
# m = 9.109*(10**(-31))
# hbar = 1.0546*(10**(-34))
# e = 1.602*(10**(-19))
# c = 2.998*(10**8)
# epsilon0 = 8.854*(10**(-12))
# wstar = m*e**4/((4*np.pi*epsilon0)**2*hbar**3)
# n = np.arange(2, 51, 1)
# wq = wstar*(1/2)*(1/(n-1)**2-1/n**2)
# wc = wstar/n**3
# plt.plot(n, np.log10(wq), 'ro', markersize=7, label="Quantum", zorder=2)
# plt.plot(n, np.log10(wc), 'bo', markersize=7, label="Semi-Classical", zorder=1)
# plt.title('Log10 of Circular Orbit Angular Frequencies')
# plt.xlabel('Initial Value of $n$')
# plt.ylabel('Angular Frequencies [radians/second]')
# plt.legend()
# plt.grid(True)
# plt.show()
# print(wq)
# print(wc)

# figure(num=None, figsize=(15, 7), dpi=80, facecolor='w', edgecolor='k')

# l = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
# freqmaxq = [252994779959093.5315186779299, 120182070167174.0680441576421, 36988681751372.99494489205527, 15805913064561.36213823721248, 7697676246643.033791192296582, 4075482938091.409581935727136, 2273415967989.337281247896825, 1329787256791.593628038634382, 793512596185.5772036835506944, 542254500442.7466011393950483, 322714248631.6707736133655506, 223195839175.6542303091337840, 175752813353.7280840428359817, 129769520955.0185329667557849, 85186686063.48536973929807437, 85186686063.48536973929807437, 41948011298.00942408068737707, 41948011298.00942408068737707, 41948011298.00942408068737707]
# freqqlog=[math.log10(y) for y in freqmaxq]  
# freqmaxc = [359565292048647.25, 50947369006663.07, 15701541137495.512, 6735134751083.602, 3470866988288.4814, 1983352564736.2754, 1239595352960.172, 826396901973.448, 578477831381.4136, 413198450986.724, 289238915690.7068, 206599225493.362, 165279380394.6896, 123959535296.01721, 82639690197.3448, 82639690197.3448, 41319845098.6724, 41319845098.6724, 41319845098.6724]
# freqclog=[math.log10(y) for y in freqmaxc]
# plt.plot(l, freqqlog, 'ro', markersize=7, label='Quantum', zorder=2)
# plt.plot(l, freqclog, 'bo', markersize=7, label='Semi-Classical', zorder=1)
# plt.xlabel('Values of $\u2113$')
# plt.ylabel('Angular Frequencies [radians/second]')
# plt.title('Log10 of Maximum Angular Frequencies for Transition from $n=100$')
# plt.legend()
# plt.grid(True)
# plt.show()

# freqmaxcsc = np.zeros(len(freqmaxc))
# freqmaxqsc = np.zeros(len(freqmaxc))

import pynverse
import numpy as np
from pynverse import inversefunc
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import scipy

figure(num=None, figsize=(15, 7), dpi=80, facecolor='w', edgecolor='k')

n = 11
l = 10

m = 9.109*(10**(-31))
hbar = 1.0546*(10**(-34))
e = 1.602*(10**(-19))
c= 2.998*10**8
epsilon0 = 8.854*(10**(-12))
epsilon = np.sqrt((1-(l*(l+1)/(n**2))))
epsilon99 = np.sqrt((1-(99*(100)/(n**2))))
freqc = m*e**4/((4*np.pi*epsilon0)**2*hbar**3*n**3)
a0 = 4*np.pi*epsilon0*(hbar**2)/(m*(e**2))
a = (n**2)*a0
b = n*np.sqrt(l*(l+1))*a0
b99 = n*np.sqrt(99*100)*a0
u_vals = []
x = lambda u : (u-epsilon*np.sin(u))/freqc
tau=2*np.pi/freqc
tau1=1.5205*10**-10
s=1000
for i in range(s):
    t = np.linspace(tau/3000,tau/2.3,num=s)
    invx = inversefunc(x, y_values=t[i]) #y~t
    u_vals.append(invx)
r = 1.89*10**10*np.sqrt(a**2*(np.cos(u_vals)-epsilon)**2+(b*np.sin(u_vals))**2)
#rcirc = [a]*s
#rl99 = np.sqrt(a**2*(np.cos(u_vals)-epsilon99)**2+(b99*np.sin(u_vals))**2)
plt.rcParams["font.size"] = "20"
plt.ylabel('Charge Density')
plt.xlabel('Radius [Bohr Radii]')
plt.title('Charge Density vs. Radius for n = 100, l = 50')
dudt = freqc/(1-epsilon*np.cos(u_vals))
drdt = np.sin(u_vals)*dudt/r*(-a**2*(np.cos(u_vals)-epsilon)+b**2*np.cos(u_vals))
plt.plot(r, drdt, "k")
#plt.plot(t, r, "r", label = "Radius")
#plt.plot(t, rl99, "b", label = "l = 99")
#plt.plot(t, rcirc, "g", label = "$\epsilon$ = 0")
#plt.legend()
#plt.show()
#v = np.sqrt((a*np.sin(u_vals))**2+(b*np.cos(u_vals))**2)*freqc/(1-epsilon*np.cos(u_vals))
#vcirc = [a*freqc]*s
#vl99 = np.sqrt((a*np.sin(u_vals))**2+(b99*np.cos(u_vals))**2)*freqc/(1-epsilon99*np.cos(u_vals))

#plt.xlabel('Time [seconds]')
#plt.ylabel('Velocity [meters/second]')
#plt.title('Velocity Versus Time for n = 100')
#plt.plot(t, v, "b", label = "Velocity")
#plt.plot(t, vl99, "b", label = "l = 99")
#plt.plot(t, vcirc, "g", label = "$\epsilon$ = 0")
#plt.legend()

#r = np.linspace(0, 20000, 10000)
#L = scipy.special.assoc_laguerre(2*r/n, n-l-1, k=2*l+1)
#R = r**2*((2*r/n)**(l)*np.exp(-r/n)*L)**2
#plt.plot(r, R/(10**197), "r")
plt.show()

#acircsqu = [a**2*freqc**4]*s
#der = freqc/(1-epsilon*np.cos(u_vals))
#dder = -epsilon*np.sin(u_vals)*freqc**2/(1-epsilon*np.cos(u_vals))**3
#xddot = -a*np.cos(u_vals)*der**2-a*np.sin(u_vals)*dder
#yddot = -b*np.sin(u_vals)*der**2+b*np.cos(u_vals)*dder
#asquared = xddot**2 + yddot**2

#der99 = freqc/(1-epsilon99*np.cos(u_vals))
#dder99 = -epsilon99*np.sin(u_vals)*freqc**2/(1-epsilon99*np.cos(u_vals))**3
#xddot99 = -a*np.cos(u_vals)*der99**2-a*np.sin(u_vals)*dder99
#yddot99 = -b99*np.sin(u_vals)*der99**2+b99*np.cos(u_vals)*dder99
#asquared99 = xddot99**2 + yddot99**2

#plt.xlabel('Time [seconds]')
#plt.ylabel('Acceleration Squared [meters/second$^2$]$^2$')
#plt.title('Acceleration Squared Versus Time for n = 100')

#plt.plot(t, asquared, "r", label = 'l = 50')
#plt.plot(t, asquared99, "b", label = 'l = 99')
#plt.plot(t, acircsqu, "g", label = '$\epsilon$ = 0')
#plt.legend()
#plt.show()

#accel = np.sqrt(asquared)
#accell99 = np.sqrt(asquared99)
#acirc = [a*freqc**2]*s
#plt.plot(t, accel, "r", label='l = 50')
#plt.plot(t, accell99, "b", label='l = 99')
#plt.plot(t, acirc, "g", label = "$\epsilon$ = 0")
#plt.plot(t, v**2/r, "k", label = '$v^2/r$')
#plt.xlabel('Time [seconds]')
#plt.ylabel('Acceleration [meters/second$^2$]')
#plt.title('Acceleration Versus Time for n = 100')  
#plt.legend()
#plt.show() 

#dy = np.trapz(asquared, u_vals)
#dy*e**2/(6*np.pi*epsilon0*c**3)
#print(acirc[498])

import pynverse
import numpy as np
from pynverse import inversefunc
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import scipy
import math

figure(num=None, figsize=(15, 7), dpi=80, facecolor='w', edgecolor='k')

n = 100
l = 50
#a = 5.29*10**-11
a = 1
r = np.linspace(0, 20000, 10000)
#N = -((2/n)**3*math.factorial(n-l-1)/(2*n*math.factorial(n+l)**3))**(1/2)
L = scipy.special.assoc_laguerre(2*r/n, n-l-1, k=2*l+1)
R = r**2*((2*r/n)**(l)*np.exp(-r/n)*L)**2
plt.plot(r, R, "b")
plt.show()

import pynverse
import numpy as np
from pynverse import inversefunc
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import scipy
import math

figure(num=None, figsize=(15, 7), dpi=80, facecolor='w', edgecolor='k')

n = 10
l = 3.066
m = 9.109*(10**(-31))
hbar = 1.0546*(10**(-34))
h = 2*np.pi*hbar
e = 1.602*(10**(-19))
c= 2.998*10**8
epsilon0 = 8.854*(10**(-12))
epsilon = np.sqrt((1-(l**2)/(n**2)))
freqc = m*e**4/((4*np.pi*epsilon0)**2*hbar**3*n**3)
a0 = 1 #4*np.pi*epsilon0*(hbar**2)/(m*(e**2))
a = (n**2)*a0
b = n*np.sqrt(l**2)*a0
u_vals = []
x = lambda u : (u-epsilon*np.sin(u))/freqc
tau=2*np.pi/freqc
tau1=1.5205*10**-10
s=5000
for i in range(s):
    t = np.linspace(0,tau/2,num=s)
    invx = inversefunc(x, y_values=t[i]) #y~t
    u_vals.append(invx)
r = np.sqrt(a**2*(np.cos(u_vals)-epsilon)**2+(b*np.sin(u_vals))**2)
figure(num=None, figsize=(15, 7), dpi=80, facecolor='w', edgecolor='k')
plt.rcParams["font.size"] = "20"
#plt.ylabel('Charge Density')
#plt.xlabel('Radius [Bohr Radii]')
#plt.title(f'Charge Density vs. Radius for n = 100, l = {l}')
x = a*np.cos(u_vals)-a*epsilon
z = b*np.sin(u_vals)
dudt = freqc/(1-epsilon*np.cos(u_vals))
drdt = np.sin(u_vals)*dudt/r*(-a**2*(np.cos(u_vals)-epsilon)+b**2*np.cos(u_vals))
v = dudt*np.sqrt(a**2*(np.sin(u_vals)**2)+b**2*(np.cos(u_vals)**2))
plt.plot(r, 1/v, "k")
plt.ylabel('Inverse Velocity [Bohr Radii/Second]')
plt.xlabel('Radius [Bohr Radii]')
plt.title(f'Inverse Velocity vs. Radius for n = {n}, l = {l}')
#plt.plot(r, v, "r")
#r = np.linspace(0, 20000, 10000)
#L = scipy.special.assoc_laguerre(2*r/n, n-l-1, k=2*l+1)
#R = (r)**2*((2*r/n)**(l)*np.exp(-r/n)*L/(4.7*10**184))**2
#plt.plot(r, R, "r")
plt.show()
print(r[14])
print(r[26])
print(r[49])
print(r[89])
print(r[155])
print(r[263])
print(r[439])
print(r[727])
print(r[1230])
print(r[2564])
print(r[4922])

print('A=' + str(h/(m*a0*v[14])))
print("B=" + str(h/(m*a0*v[26])))
print("C=" + str(h/(m*a0*v[49])))
print("D=" + str(h/(m*a0*v[89])))
print("E=" + str(h/(m*a0*v[155])))
print("F=" + str(h/(m*a0*v[263])))
print("G=" + str(h/(m*a0*v[439])))
print("H=" + str(h/(m*a0*v[727])))
print("I=" + str(h/(m*a0*v[1230])))
print("J=" + str(h/(m*a0*v[2564])))
print("K=" + str(h/(m*a0*v[4922])))

import pylab
import pynverse
import numpy as np
from pynverse import inversefunc
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import scipy

figure(num=None, figsize=(8, 5), dpi=80, facecolor='w', edgecolor='k')

n = 100
l = 1/2

m = 9.109*(10**(-31))
hbar = 1.0546*(10**(-34))
e = 1.602*(10**(-19))
c= 2.998*10**8
epsilon0 = 8.854*(10**(-12))
epsilon = np.sqrt((1-(l*(l+1)/(n**2))))
freqc = m*e**4/((4*np.pi*epsilon0)**2*hbar**3*n**3)
a0 = 1 #4*np.pi*epsilon0*(hbar**2)/(m*(e**2))
a = (n**2)*a0
b = n*np.sqrt(l*(l+1))*a0

u_vals = []
x = lambda u : (u-epsilon*np.sin(u))/freqc
tau=2*np.pi/freqc
s=1000
for i in range(s):
    t = np.linspace(0,tau,num=s)
    invx = inversefunc(x, y_values=t[i])
    u_vals.append(invx)
dist = a*(np.cos(u_vals)-epsilon)
print(-sum(dist*t)/sum(t))
print(3/2*n**2)

x = np.linspace(-(a*epsilon+a), a-a*epsilon, 1000)
y = b*np.sqrt(1-((x+a*epsilon)/a)**2)
y1 = -b*np.sqrt(1-((x+a*epsilon)/a)**2)
plt.plot(x, y, "b")
plt.plot(x, y1, "b")
plt.plot(sum(dist*t)/sum(t), 0, "ko")
plt.xlabel("z [Bohr Radii]")
plt.ylabel("x [Bohr Radii]")
plt.title(f"n = {n}, l = {l}")
#pylab.ylim([-15, 15])
#pylab.xlim([-30, 7])
plt.grid(True)
plt.show()

import pylab
figure(num=None, figsize=(15, 7), dpi=80, facecolor='w', edgecolor='k')

#l=1

n = 10
l = 1

epsilon = np.sqrt((1-((l**2)/((n-1)**2))))
a0 = 1
a = ((n-1)**2)*a0
b = (n-1)*np.sqrt((l**2))*a0

x = np.linspace(a*epsilon-a, a+a*epsilon, 1000)
y = b*np.sqrt(1-((x-a*epsilon)/a)**2)
y1 = -b*np.sqrt(1-((x-a*epsilon)/a)**2)

x2l_1 = 4.557364727032397
y2l_1 = 3.1307948628910514
x4l_1 = 20.263957774416866
y4l_1 = 6.017265574834252
x6l_1 = 49.41000576243926
y6l_1 = 8.310716575309906
x8l_1 = 101.46866622121073
y8l_1 = 8.693157458018936
x10l_1 = 101.46866622121073
y10l_1 = -8.693157458018936
x12l_1 = 49.41000576243926
y12l_1 = -8.310716575309906
x14l_1 = 20.263957774416866
y14l_1 = -6.017265574834252
x16l_1 = 4.557364727032397
y16l_1 = -3.1307948628910514
x18l_1 = -0.50155281
y18l_1 = 0

plt.plot(x, y, "b")
plt.plot(x, y1, "b")
plt.plot(x2l_1, y2l_1, "ro")
plt.plot(x4l_1, y4l_1, "ro")
plt.plot(x6l_1, y6l_1, "ro")
plt.plot(x8l_1, y8l_1, "ro")
plt.plot(x10l_1, y10l_1, "ro")
plt.plot(x12l_1, y12l_1, "ro")
plt.plot(x14l_1, y14l_1, "ro")
plt.plot(x16l_1, y16l_1, "ro")
plt.plot(x18l_1, y18l_1, "ro")

#l=2

n = 10
l = 2

epsilon = np.sqrt((1-((l**2)/((n-1)**2))))
a0 = 1
a = ((n-1)**2)*a0
b = (n-1)*np.sqrt((l**2))*a0

x = np.linspace(a*epsilon-a, a+a*epsilon, 1000)
y = b*np.sqrt(1-((x-a*epsilon)/a)**2)
y1 = -b*np.sqrt(1-((x-a*epsilon)/a)**2)

x2l_2 = 3.1025317765003555
y2l_2 = 6.30272213135449
x4l_2 = 19.13841207667449
y4l_2 = 12.132236626170835
x6l_2 = 48.83594848537168
y6l_2 = 16.707589601830765
x8l_2 = 101.86663349342962
y8l_2 = 17.266192531379474
x10l_2 = 101.86663349342962
y10l_2 = -17.266192531379474
x12l_2 = 48.83594848537168
y12l_2 = -16.707589601830765
x14l_2 = 19.13841207667449
y14l_2 = -12.132236626170835
x16l_2 = 3.1025317765003555
y16l_2 = -6.30272213135449
x18l_2 = -2.02532051347
y18l_2 = 0

plt.plot(x, y, "b")
plt.plot(x, y1, "b")
plt.plot(x2l_2, y2l_2, "ro")
plt.plot(x4l_2, y4l_2, "ro")
plt.plot(x6l_2, y6l_2, "ro")
plt.plot(x8l_2, y8l_2, "ro")
plt.plot(x10l_2, y10l_2, "ro")
plt.plot(x12l_2, y12l_2, "ro")
plt.plot(x14l_2, y14l_2, "ro")
plt.plot(x16l_2, y16l_2, "ro")
plt.plot(x18l_2, y18l_2, "ro")

#l=3

n = 10
l = 3

epsilon = np.sqrt((1-((l**2)/((n-1)**2))))
a0 = 1
a = ((n-1)**2)*a0
b = (n-1)*np.sqrt((l**2))*a0

x = np.linspace(a*epsilon-a, a+a*epsilon, 1000)
y = b*np.sqrt(1-((x-a*epsilon)/a)**2)
y1 = -b*np.sqrt(1-((x-a*epsilon)/a)**2)

x2l_3 = 0.67642206884159
y2l_3 = 9.613970284367795
x4l_3 = 17.230057658368008
y4l_3 = 18.450411271990163
x6l_3 = 47.90838078607997
y6l_3 = 25.278617866640932
x8l_3 = 102.59642833505619
y8l_3 = 25.54526487185065
x10l_3 = 102.59642833505619
y10l_3 = -25.54526487185065
x12l_3 = 47.90838078607997
y12l_3 = -25.278617866640932
x14l_3 = 17.230057658368008
y14l_3 = -18.450411271990163
x16l_3 = 0.67642206884159
y16l_3 = -9.613970284367795
x18l_3 = -4.63246763185
y18l_3 = 0

plt.plot(x, y, "b")
plt.plot(x, y1, "b")
plt.plot(x2l_3, y2l_3, "ro")
plt.plot(x4l_3, y4l_3, "ro")
plt.plot(x6l_3, y6l_3, "ro")
plt.plot(x8l_3, y8l_3, "ro")
plt.plot(x10l_3, y10l_3, "ro")
plt.plot(x12l_3, y12l_3, "ro")
plt.plot(x14l_3, y14l_3, "ro")
plt.plot(x16l_3, y16l_3, "ro")
plt.plot(x18l_3, y18l_3, "ro")

#l=4

n = 10
l = 4

epsilon = np.sqrt((1-((l**2)/((n-1)**2))))
a0 = 1
a = ((n-1)**2)*a0
b = (n-1)*np.sqrt((l**2))*a0

x = np.linspace(a*epsilon-a, a+a*epsilon, 1000)
y = b*np.sqrt(1-((x-a*epsilon)/a)**2)
y1 = -b*np.sqrt(1-((x-a*epsilon)/a)**2)

x2l_4 = -2.881079092804024
y2l_4 = 13.10617868012439
x4l_4 = 14.509153590564953
y4l_4 = 25.106438539934633
x6l_4 = 46.68591983986166
y6l_4 = 34.11387011667419
x8l_4 = 103.72263887893736
y8l_4 = 33.22919990804424
x10l_4 = 103.72263887893736
y10l_4 = -33.22919990804424
x12l_4 = 46.68591983986166
y12l_4 = -34.11387011667419
x14l_4 = 14.509153590564953
y14l_4 = -25.106438539934633
x16l_4 = -2.881079092804024
y16l_4 = -13.10617868012439
x18l_4 = -8.43968026531
y18l_4 = 0

plt.plot(x, y, "b")
plt.plot(x, y1, "b")
plt.plot(x2l_4, y2l_4, "ro")
plt.plot(x4l_4, y4l_4, "ro")
plt.plot(x6l_4, y6l_4, "ro")
plt.plot(x8l_4, y8l_4, "ro")
plt.plot(x10l_4, y10l_4, "ro")
plt.plot(x12l_4, y12l_4, "ro")
plt.plot(x14l_4, y14l_4, "ro")
plt.plot(x16l_4, y16l_4, "ro")
plt.plot(x18l_4, y18l_4, "ro")

#l=5

n = 10
l = 5

epsilon = np.sqrt((1-((l**2)/((n-1)**2))))
a0 = 1
a = ((n-1)**2)*a0
b = (n-1)*np.sqrt((l**2))*a0

x = np.linspace(a*epsilon-a, a+a*epsilon, 1000)
y = b*np.sqrt(1-((x-a*epsilon)/a)**2)
y1 = -b*np.sqrt(1-((x-a*epsilon)/a)**2)

x2l_5 = -7.700203459837836
y2l_5 = 16.92842624556691
x4l_5 = 10.922745837609575
y4l_5 = 32.28434547192637
x6l_5 = 45.25498283161491
y6l_5 = 43.29349164769498
x8l_5 = 105.2496958812813
y8l_5 = 39.77017459417766
x10l_5 = 105.2496958812813
y10l_5 = -39.77017459417766
x12l_5 = 45.25498283161491
y12l_5 = -43.293491647694983
x14l_5 = 10.922745837609575
y14l_5 = -32.28434547192637
x16l_5 = -7.700203459837836
y16l_5 = -16.92842624556691
x18l_5 = -13.6501670381
y18l_5 = 0

plt.plot(x, y, "b")
plt.plot(x, y1, "b")
plt.plot(x2l_5, y2l_5, "ro")
plt.plot(x4l_5, y4l_5, "ro")
plt.plot(x6l_5, y6l_5, "ro")
plt.plot(x8l_5, y8l_5, "ro")
plt.plot(x10l_5, y10l_5, "ro")
plt.plot(x12l_5, y12l_5, "ro")
plt.plot(x14l_5, y14l_5, "ro")
plt.plot(x16l_5, y16l_5, "ro")
plt.plot(x18l_5, y18l_5, "ro")

#l=6

n = 10
l = 6

epsilon = np.sqrt((1-((l**2)/((n-1)**2))))
a0 = 1
a = ((n-1)**2)*a0
b = (n-1)*np.sqrt((l**2))*a0

x = np.linspace(a*epsilon-a, a+a*epsilon, 1000)
y = b*np.sqrt(1-((x-a*epsilon)/a)**2)
y1 = -b*np.sqrt(1-((x-a*epsilon)/a)**2)

x2l_6 = -14.075834506373027
y2l_6 = 21.273318206927513
x4l_6 = 6.371757306652006
y4l_6 = 40.24798442108949
x6l_6 = 43.816550775513974
y6l_6 = 52.85979915929519
x8l_6 = 106.871342582601
y8l_6 = 44.216547054020786
x10l_6 = 106.871342582601
y10l_6 = -44.216547054020786
x12l_6 = 43.816550775513974
y12l_6 = -52.85979915929519
x14l_6 = 6.371757306652006
y14l_6 = -40.24798442108949
x16l_6 = -14.075834506373027
y16l_6 = -21.273318206927513
x18l_6 = -20.6261646075
y18l_6 = 0

plt.plot(x, y, "b")
plt.plot(x, y1, "b")
plt.plot(x2l_6, y2l_6, "ro")
plt.plot(x4l_6, y4l_6, "ro")
plt.plot(x6l_6, y6l_6, "ro")
plt.plot(x8l_6, y8l_6, "ro")
plt.plot(x10l_6, y10l_6, "ro")
plt.plot(x12l_6, y12l_6, "ro")
plt.plot(x14l_6, y14l_6, "ro")
plt.plot(x16l_6, y16l_6, "ro")
plt.plot(x18l_6, y18l_6, "ro")

#l=7

n = 10
l = 7

epsilon = np.sqrt((1-((l**2)/((n-1)**2))))
a0 = 1
a = ((n-1)**2)*a0
b = (n-1)*np.sqrt((l**2))*a0

x = np.linspace(a*epsilon-a, a+a*epsilon, 1000)
y = b*np.sqrt(1-((x-a*epsilon)/a)**2)
y1 = -b*np.sqrt(1-((x-a*epsilon)/a)**2)

x2l_7 = -22.576540064382314
y2l_7 = 26.495640147839897
x4l_7 = 0.7471569231471132
y4l_7 = 49.46397492720873
x6l_7 = 42.69818755548364
y6l_7 = 62.675273435205035
x8l_7 = 107.35154168368824
y8l_7 = 45.18844005043554
x10l_7 = 107.35154168368824
y10l_7 = -45.18844005043554
x12l_7 = 42.69818755548364
y12l_7 = -62.675273435205035
x14l_7 = 0.7471569231471132
y14l_7 = -49.46397492720873
x16l_7 = -22.576540064382314
y16l_7 = -26.495640147839897
x18l_7 = -30.0883117546
y18l_7 = 0

plt.plot(x, y, "b")
plt.plot(x, y1, "b")
plt.plot(x2l_7, y2l_7, "ro")
plt.plot(x4l_7, y4l_7, "ro")
plt.plot(x6l_7, y6l_7, "ro")
plt.plot(x8l_7, y8l_7, "ro")
plt.plot(x10l_7, y10l_7, "ro")
plt.plot(x12l_7, y12l_7, "ro")
plt.plot(x14l_7, y14l_7, "ro")
plt.plot(x16l_7, y16l_7, "ro")
plt.plot(x18l_7, y18l_7, "ro")

#l=8

n = 10
l = 8

epsilon = np.sqrt((1-((l**2)/((n-1)**2))))
a0 = 1
a = ((n-1)**2)*a0
b = (n-1)*np.sqrt((l**2))*a0

x = np.linspace(a*epsilon-a, a+a*epsilon, 1000)
y = b*np.sqrt(1-((x-a*epsilon)/a)**2)
y1 = -b*np.sqrt(1-((x-a*epsilon)/a)**2)

x2l_8 = -34.55956915411903
y2l_8 = 33.552071729823076
x4l_8 = -6.05858708448431
y4l_8 = 60.92391545142549
x6l_8 = 42.49412864335966
y6l_8 = 71.84064167776569
x8l_8 = 103.38969481606973
y8l_8 = 41.38568142896117
x10l_8 = 103.38969481606973
y10l_8 = -41.38568142896117
x12l_8 = 42.49412864335966
y12l_8 = -71.84064167776569
x14l_8 = -6.05858708448431
y14l_8 = -60.92391545142549
x16l_8 = -34.55956915411903
y16l_8 = -33.552071729823076
x18l_8 = -43.8920493694
y18l_8 = 0

plt.plot(x, y, "b")
plt.plot(x, y1, "b")
plt.plot(x2l_8, y2l_8, "ro")
plt.plot(x4l_8, y4l_8, "ro")
plt.plot(x6l_8, y6l_8, "ro")
plt.plot(x8l_8, y8l_8, "ro")
plt.plot(x10l_8, y10l_8, "ro")
plt.plot(x12l_8, y12l_8, "ro")
plt.plot(x14l_8, y14l_8, "ro")
plt.plot(x16l_8, y16l_8, "ro")
plt.plot(x18l_8, y18l_8, "ro")

#l=9

n = 10
l = 9

epsilon = np.sqrt((1-((l**2)/((n-1)**2))))
a0 = 1
a = ((n-1)**2)*a0
b = (n-1)*np.sqrt((l**2))*a0

x = np.linspace(a*epsilon-a, a+a*epsilon, 1000)
y = b*np.sqrt(1-((x-a*epsilon)/a)**2)
y1 = -b*np.sqrt(1-((x-a*epsilon)/a)**2)

x2l_9 = -62.04460158661877
y2l_9 = 52.0717525531621
x4l_9 = -14.056452632859514
y4l_9 = 79.77102318122901
x6l_9 = 40.503672934105374
y6l_9 = 70.14593700883195
x8l_9 = 76.11703620068614
y8l_9 = 27.69831763886455
x10l_9 = 76.11703620068614
y10l_9 = -27.69831763886455
x12l_9 = 40.503672934105374
y12l_9 = -70.14593700883195
x14l_9 = -14.056452632859514
y14l_9 = -79.77102318122901
x16l_9 = -62.04460158661877
y16l_9 = -52.0717525531621
x18l_9 = -81
y18l_9 = 0

plt.plot(x, y, "b")
plt.plot(x, y1, "b")
plt.plot(x2l_9, y2l_9, "ro")
plt.plot(x4l_9, y4l_9, "ro")
plt.plot(x6l_9, y6l_9, "ro")
plt.plot(x8l_9, y8l_9, "ro")
plt.plot(x10l_9, y10l_9, "ro")
plt.plot(x12l_9, y12l_9, "ro")
plt.plot(x14l_9, y14l_9, "ro")
plt.plot(x16l_9, y16l_9, "ro")
plt.plot(x18l_9, y18l_9, "ro")

plt.plot(0, 0, "ko")
pylab.ylim([-85, 85])
pylab.xlim([-85, 170])
plt.show()

#Automated version of the above

import pynverse
import numpy as np
from pynverse import inversefunc
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import scipy
import math
from array import array

n = 10
l = 9
m = 1 #9.109*(10**(-31))
hbar = 1 #1.0546*(10**(-34))
h = 2*np.pi*hbar
e = 1 #1.602*(10**(-19))
epsilon0 = 1/(4*np.pi) #8.854*(10**(-12))
epsilon = np.sqrt((1-(l**2)/((n-1)**2)))
freqc = m*e**4/((4*np.pi*epsilon0)**2*hbar**3*(n-1)**3)
a0 = 1 #4*np.pi*epsilon0*(hbar**2)/(m*(e**2))
a = ((n-1)**2)*a0
b = (n-1)*np.sqrt(l**2)*a0
u_vals = []
x1 = lambda u : (u-epsilon*np.sin(u))/freqc
tau=2*np.pi/freqc
s=80000
for i in range(s):
    t = np.linspace(0,tau,num=s)
    invx = inversefunc(x1, y_values=t[i])
    u_vals.append(invx)
    
dudt = freqc/(1-epsilon*np.cos(u_vals))
v = dudt*np.sqrt(a**2*(np.sin(u_vals)**2)+b**2*(np.cos(u_vals)**2))
integrand = v*np.sqrt(a**2*(np.sin(u_vals)**2)+b**2*(np.cos(u_vals)**2))

ar = []

for i in range(s):
    a = np.trapz(integrand[0:i], x=u_vals[0:i], dx=1)
    ar.append(a)
area = np.array(ar)
pi2 = np.abs(area-2*np.pi).argmin()
pi4 = np.abs(area-4*np.pi).argmin()
pi6 = np.abs(area-6*np.pi).argmin()
pi8 = np.abs(area-8*np.pi).argmin()
x = a*(np.cos(u_vals)-epsilon)
y = b*np.sin(u_vals)

x2l = x[pi2]
y2l = y[pi2]
x4l = x[pi4]
y4l = y[pi4]
x6l = x[pi6]
y6l = y[pi6]
x8l = x[pi8]
y8l = y[pi8]
x10l = x8l
y10l = -y8l
x12l = x6l
y12l = -y6l
x14l = x4l
y14l = -y4l
x16l = x2l
y16l = -y2l
x18l = x[0]
y18l = 0

x = np.linspace(a*epsilon-a, a+a*epsilon, 1000)
y = b*np.sqrt(1-((x-a*epsilon)/a)**2)
y1 = -b*np.sqrt(1-((x-a*epsilon)/a)**2)

plt.plot(x, y, "b")
plt.plot(x, y1, "b")
plt.plot(x2l, y2l, "ro")
plt.plot(x4l, y4l, "ro")
plt.plot(x6l, y6l, "ro")
plt.plot(x8l, y8l, "ro")
plt.plot(x10l, y10l, "ro")
plt.plot(x12l, y12l, "ro")
plt.plot(x14l, y14l, "ro")
plt.plot(x16l, y16l, "ro")
plt.plot(x18l, y18l, "ro")
