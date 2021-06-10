import numpy as np
from numpy.core.function_base import linspace
import Constants as C
import math

resolution = C.resolution
dx = C.dx
delta = 1e-5
E0 = (C.N/2)
delt = 1
def delta(x):
    return delt/(x**2 + delt**2)


def deltaFunc(w, E1, E2):
    return 1/((E1-E2-(w + delta*1.j)) + 1/(E1-E2))

def conductivity(n, m, b, omega):
    if m > E0 and n > E0:
        return 0
    if m < E0 and n < E0:
        return 0
    if m == n:
        return 0
    if m > n:
        return 0
    res = 0
    N = np.load(f"Cache/{C.N}/B{b}/Kn_{n}.npy")
    K = np.load(f"Cache/{C.N}/B{b}/Kn_{m}.npy")
    En = np.load(f"Cache/{C.N}/B{b}/En_{n}.npy")
    Em = np.load(f"Cache/{C.N}/B{b}/En_{m}.npy")
    for j in range(resolution):
        for i in range(resolution):
            M = C.sigmaX.dot(K[j][i])
            a = np.absolute(np.conj(N[j][i]).dot(M))**2
            dE = (np.real(Em[j][i]-En[j][i]))
            c = delta(dE-omega)
            res += 1.j*((a*c)*dx*dx)

    return res


def conductivity2(n, m, i, j, b):
    N = np.load(f"Cache/{C.N}/B{b}/Kn_{n}.npy")
    K = np.load(f"Cache/{C.N}/B{b}/Kn_{m}.npy")
    En = np.load(f"Cache/{C.N}/B{b}/En_{n}.npy")
    Em = np.load(f"Cache/{C.N}/B{b}/En_{m}.npy")
    Ans = np.zeros((100, 100))
    print(Ans.shape)
    for ky in j:
        for kx in i:
            M = C.sigmaX.dot(K[ky][kx])
            a = np.absolute(np.conj(N[ky][kx]).dot(M))**2
            Ans[j][i] = a
    
    return Ans

# kx = linspace(0, resolution-2, 99, dtype=int)
# ky = linspace(0, resolution-2, 99, dtype=int)
# print(conductivity2(1,1,kx,ky,0))