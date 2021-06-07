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


print(get_E(0,0,0))
print(get_E(C.N,C.resolution,C.resolution))
