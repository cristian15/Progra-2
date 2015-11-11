import pylab as plt
import random as RA


def lowpass(v, a):
	f[0] = v[0]
	for i in range(1, 100):
		f[i] = a*v[i] + (1.0 - a)*f[i-1]
	return f
	

a = [.1, .3, .5, .7, .9]
ve = []
f = []

# completa array con distribucion normal media 10 desviacion estandar 0.5
for i in range(10000):
	ve.append(RA.gauss(10, .5))	
	f.append(0.0)

# ---- Grafico 1 ---- #
f = lowpass(ve, a[0])
plt.figure(1)
plt.subplot(211)
plt.plot(ve)
plt.plot(f)
# ------------------ #
# ---- Grafico 2 ---- #
f = lowpass(ve, a[1]) 
plt.subplot(212)
plt.plot(ve)
plt.plot(f)
# ------------------ #

# ---- Grafico 3 ---- #
f = lowpass(ve, a[2])
plt.figure(2)
plt.subplot(211)
plt.plot(ve)
plt.plot(f)
# ------------------ #
# ---- Grafico 4 ---- #
f = lowpass(ve, a[3]) 
plt.subplot(212)
plt.plot(ve)
plt.plot(f)
# ------------------ #
# ---- Grafico 5 ---- #
f = lowpass(ve, a[4])
plt.figure(3)
plt.subplot(211)
plt.plot(ve)
plt.plot(f)

plt.show()
