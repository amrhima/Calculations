import numpy as np
import Constants as C

resolution = C.resolution
dx = C.dx
delta = 1e-4
E0 = (C.N/2)

def conductivity(n, m, b, omega):
    l = 1
    if m > E0 and n > E0:
        return 0
    if m < E0 and n < E0:
        return 0
    if m == n:
        return 0
    if m > n:
        l = -1
    res = 0
    N = np.load(f"Cache/{C.N}/B{b}/Kn_{n}.npy")
    K = np.load(f"Cache/{C.N}/B{b}/Kn_{m}.npy")
    En = np.load(f"Cache/{C.N}/B{b}/En_{n}.npy")
    Em = np.load(f"Cache/{C.N}/B{b}/En_{m}.npy")
    sigmaX = np.load(f"Cache/{C.N}/Sx.npy")
    for j in range(resolution):
        for i in range(resolution):
            M = sigmaX.dot(K[j][i])
            a = np.absolute(np.conj(N[j][i]).dot(M))**2
            # b = (En[j][i] - Em[j][i]) * (En[j][i] - Em[j][i] - (omega + (delta * 1.j)))
            b = omega
            res += ((a/b)*dx*dx)

    return res*l