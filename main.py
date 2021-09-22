import numpy as np
import Conductivity as IP
import matplotlib.pyplot as plt
import Constants as C
import math

def conductivity2(omega):
    res = 0
    for n in range(C.mu-5,C.mu):
        for m in range(C.mu,C.mu+4):
            res += IP.conductivityIntegrated(m, n, omega)

    return res

def condOmega(omega):
    res = np.zeros(omega.shape[0], dtype=np.complex_)
    i=0
    for o in omega:
        res[i] = conductivity2(o)
        i += 1

    return res

def saveSigma():
    Omega = np.linspace(0.1, 20, 100)
    Sigma = condOmega(Omega)
    np.save(f"Data/sigma_{C.beta}_{C.N}.npy", Sigma)

def plotR(beta):
    Omega = np.linspace(0.1, 20, 100)
    eps = 137/(4*math.pi)
    print(eps)
    Sigma = (np.load(f"Data/sigma_{beta}_{C.N}.npy"))
    A = (np.real(Sigma))
    # R = (A / (A + 2*eps))**2
    plt.plot(Omega, A)
    # plt.ylim(-1,1)
    plt.ylabel("Sigma")
    plt.xlabel("Omega")
    return plt

# saveSigma()
plotR(0).show()