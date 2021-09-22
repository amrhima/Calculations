import numpy as np
import time
import Constants as C
import math


def loadEigenVs():
    Energy = np.load(f"Data/E_{C.beta}_{C.N}.npy")
    States = np.load(f"Data/V_{C.beta}_{C.N}.npy")
    return [Energy,States]

[E,V] = loadEigenVs()

def conductivity(n, m, kx, ky, omega):
    Kn = (V[kx][ky][:,n]).reshape((1,C.N))
    Km = V[kx][ky][:,m]
    En = E[kx][ky][n]
    Em = E[kx][ky][m]
    M = C.sigmaX(C.N).dot(Km).reshape((C.N,1))
    a = (np.abs(np.conj(Kn).dot(M)))**2
    dE = (np.real(En-Em))
    print(f"dE: {dE}")
    dW = (dE - (omega + C.delt*1.j)) 
    print(f"del_term: {1/dW}")
    c = 1.j*(1/dW - 1/dE)
    print(f"C: {c}")
    # print(f"A: {a}")
    res = (a*c)/omega
    return res

# print(conductivity(5,4,30,30,0))

def conductivityIntegrated(n, m, omega):
    start = time.time()
    km = C.momenta_labels
    kn = C.momenta_labels
    kx = C.x_momenta
    ky = C.y_momenta
    integrand = np.zeros((C.resolution, C.resolution), dtype=np.complex_)
    for x in km:
        for y in kn:
            integrand[x][y] = conductivity(n,m,x,y,omega)

    sigmaxx = np.trapz(np.trapz(integrand,x=ky), x=kx)
    end = time.time()
    print(f"integrated: {end - start}")
    return sigmaxx

# print(np.real(E[50,10,21] - E[50,10,20]))
# print(np.real(E[50,50,:]))

print(conductivity(21,20,50,10,16))
# print(conductivityIntegrated(23,18,12.566370614359176))