import numpy as np
import InnerProduct as IP
import matplotlib.pyplot as plt
import Constants as C
import math

def conductivity2(omega):
    res = 0
    for n in range(C.mu):
        for m in range(C.mu,C.N):
            res += np.real(IP.conductivityIntegrated(n, m, omega))
    return res

def condOmega(omega):
    res = np.zeros(omega.shape[0])
    i=0
    for o in omega:
        res[i] = conductivity2(o)
        i += 1

    return res

def saveSigma():
    Omega = np.linspace(1, 20, 100)
    Sigma = condOmega(Omega)
    np.save(f"Data/sigma_{C.beta}_{C.N}.npy", Sigma)

def plotR(beta):
    Omega = np.linspace(1, 20, 100)
    eps = 137/(4*math.pi)
    Sigma = np.abs(np.load(f"Data/sigma_{beta}_{C.N}.npy")*math.pi/2)
    R = (Sigma**2)/((Sigma + 2*eps*math.cos(math.pi/3))**2)
    plt.plot(Omega, R)
    plt.ylabel("R")
    plt.ylim(-0.1,1)
    plt.xlabel("Omega")
    plt.savefig(f"R_{beta}_{C.N}.png")

saveSigma()