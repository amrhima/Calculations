import numpy as np
import Constants as C

def getEnergy(N, B, n, x, y):
    return np.load(f"Cache/{N}/B{B}/En_{n}.npy")[y][x]

def getK(N, B, n, x, y):
    return np.load(f"Cache/{N}/B{B}/Kn_{n}.npy")[y][x]

def get_E(n, x, y):
    return getEnergy(C.N, C.beta, n, x, y)

def get_K(n, x, y):
    return getK(C.N, C.beta, n, x, y)

M = get_K(0,50,90)
N = get_K(1,50,90)
E1 = get_E(0,50,90)
E2 = get_E(1,50,90)
H = C.sigmaX.dot(M)
# print(M)
# print(E1)
# print(N)
# print(E2)
R = np.conj(M).dot(N)
L = np.conj(H).dot(N)
print(np.abs(R))
print(np.abs(L))
