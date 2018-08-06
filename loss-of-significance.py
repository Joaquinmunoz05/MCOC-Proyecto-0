import numpy as np
from matplotlib import pyplot


n=0.001

y = n
z = n

Y=[y]
Z=[z]
for i in range (200):
    b=(Y[-1])
    b1 = b**3 + b**2 + b      #Ecuaciones cubicas
    Y.append(np.float16(b1))  
    c=(Z[-1])
    c1 = c**3 + c**2 + c
    
    Z.append(np.float64(c1))

print Y[-1]
print Z[-1]  
error=[]
for i in range(len(Y)):
    error.append((Z[i]-Y[i]))    #diferencia entre cada valor
pyplot.plot(error)
pyplot.ylabel("Variacion")
pyplot.show()
pyplot.plot(Y,'b')
pyplot.plot(Z,'r')
pyplot.show()
