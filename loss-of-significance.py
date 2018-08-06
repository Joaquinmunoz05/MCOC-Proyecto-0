import numpy as np
from matplotlib import pyplot


n=0.001

y = n
z = n

Y=[y]
Z=[z]
for i in range (200):
    b=(Y[-1])
    b1 = b**3 + b**2 + b
    Y.append(np.float16(b1))
    c=(Z[-1])
    c1 = c**3 + c**2 + c
    
    Z.append(np.float64(c1))

print Y[-1]
print Z[-1]  
error=[]
for i in range(len(Y)):
    error.append((Z[i]-Y[i]))
pyplot.plot(error)

pyplot.ylabel("Variacion")
pyplot.show()
pyplot.plot(Y,'b')
pyplot.plot(Z,'r')
pyplot.ylabel("Valor iteracion")
pyplot.show()
for i in range (8):
    print "valor float16:",Y[i*25], "Valor float64:", Z[i*25], "Diferencia:", error[i*25]
