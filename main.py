import numpy as np
import InnerProduct as IP
import matplotlib.pyplot as plt
import Constants as C

def conductivity2(omega):
    res = 0
    # for n in range(C.N):
    #     for m in range(C.N):
    n=int(C.N/2)
    m=int(C.N/2)-1
    res += np.real(IP.conductivityIntegrated(n, m, omega))
    return res

def condOmega(omega):
    res = np.zeros(omega.shape[0])
    i=0
    for o in omega:
        res[i] = conductivity2(o)
        i += 1

    return res


Omega = np.linspace(1, 20, 100)

Sigma = condOmega(Omega)
plt.plot(Omega, Sigma)
plt.ylabel("Sigma")
plt.xlabel("Omega")
plt.show()