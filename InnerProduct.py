import numpy as np
import time
import Constants as C
import EigenVs as Eig
import math


[E,V] = Eig.getEigenVs()

def conductivity(n, m, kx, ky, omega):
    Kn = (V[kx][ky][n]).reshape((1,C.N))
    Km = V[kx][ky][m]
    En = E[kx][ky][n]
    Em = E[kx][ky][m]
    M = C.sigmaX(C.N).dot(Km).reshape((C.N,1))
    a = np.absolute(np.conj(Kn).dot(M))**2
    dE = (np.real(Em-En))
    c = C.delta(dE-omega)
    res = (a*c)/omega
    return res

# print(conductivity(5,4,30,30,0))

def conductivityIntegrated(n, m, omega):
    start = time.time()
    km = C.momenta_labels
    kn = C.momenta_labels
    kx = C.momenta
    ky = C.momenta
    integrand = np.zeros((C.resolution, C.resolution))
    for x in km:
        for y in kn:
            integrand[x][y] = conductivity(n,m,x,y,omega)

    sigmaxx = np.trapz(kx, np.trapz(ky, integrand))
    end = time.time()
    print(f"integrated: {end - start}")
    return sigmaxx

# print(conductivityIntegrated(0,0,3))