import numpy as np
import InnerProduct as IP
import matplotlib.pyplot as plt
import Constants as C

def conductivity2(omega):
    res = 0
    for n in range(C.mu):
        for m in range(C.mu, C.N):
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
np.save(f"sigma_{C.beta}_{C.N}.npy", Sigma)
# plt.plot(Omega, Sigma)
# plt.ylabel("Sigma")
# plt.xlabel("Omega")
# plt.savefig(f"{C.beta}-{C.N}.png")