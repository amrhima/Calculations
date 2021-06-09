import numpy as np
import InnerProduct as IP
import matplotlib.pyplot as plt
import Constants as C

def conductivity(b,omega):
    res = 0
    for m in range(C.N):
        for n in range(C.N):
            res += np.real(IP.conductivity(n, m, b, omega))
    return res

def conductivity2(b,omega):
    res = 0
    for n in range(C.resolution):
        for m in range(C.resolution):
            res += np.real(IP.conductivity2(n, m, b, omega))*(C.dx**2)
    return res

Omega = np.linspace(1, 50, 250)
Sigma = conductivity(0, Omega)
plt.plot(Omega, Sigma)
plt.ylabel("Sigma")
plt.xlabel("Omega")
plt.show()