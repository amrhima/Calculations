import numpy as np
import InnerProduct as IP
import matplotlib.pyplot as plt
import Constants as C

def conductivity(b,omega):
    res = 0
    for n in range(C.N):
        for m in range(C.N):
            res += np.real(IP.conductivity(n, m, b, omega))
    return res

Omega = np.linspace(1, 50, 250)
Sigma = conductivity(0, Omega)
plt.plot(Omega, Sigma)
plt.ylabel("Sigma")
plt.xlabel("Omega")
plt.show()