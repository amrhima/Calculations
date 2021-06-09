import numpy as np
import Constants as C
import math

resolution = C.resolution
dx = C.dx
delta = 1e-5
E0 = (C.N/2)

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
            if (a != 0) and Em[j][i] != En[j][i]:
                dE = (np.real(Em[j][i]-En[j][i]))
                c = deltaFunc(omega, Em[j][i], En[j][i])
                res += 1.j*((a*c)*dx*dx)

    return res


def conductivity2(i, j, b, omega):
    res = 0
    for m in range(C.N):
        for n in range(C.N):
            if m == n:
                res = res
            elif m > n:
                N = np.load(f"Cache/{C.N}/B{b}/Kn_{n}.npy")
                K = np.load(f"Cache/{C.N}/B{b}/Kn_{m}.npy")
                # En = np.load(f"Cache/{C.N}/B{b}/En_{n}.npy")
                # Em = np.load(f"Cache/{C.N}/B{b}/En_{m}.npy")
                sigmaX = np.load(f"Cache/{C.N}/Sx.npy")
                M = sigmaX.dot(K[j][i])
                a = np.absolute(np.conj(N[j][i]).dot(M))**2
                # c = (En[j][i] - Em[j][i]) * (En[j][i] - Em[j][i] - (omega + (delta * 1.j)))
                c = math.pi /  omega
                res -= ((a*c))
            else:
                N = np.load(f"Cache/{C.N}/B{b}/Kn_{n}.npy")
                K = np.load(f"Cache/{C.N}/B{b}/Kn_{m}.npy")
                # En = np.load(f"Cache/{C.N}/B{b}/En_{n}.npy")
                # Em = np.load(f"Cache/{C.N}/B{b}/En_{m}.npy")
                sigmaX = np.load(f"Cache/{C.N}/Sx.npy")
                M = sigmaX.dot(K[j][i])
                a = np.absolute(np.conj(N[j][i]).dot(M))**2
                # b = (En[j][i] - Em[j][i]) * (En[j][i] - Em[j][i] - (omega + (delta * 1.j)))
                c = math.pi /  omega
                res += ((a*c))

    return res