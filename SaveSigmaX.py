import numpy as np
import Constants as C

def m_lTerm(m, l):
    if int(m/2) == int(l/2) and m != l:
        return 1
    return 0

def sigmaX(N):
    a = np.zeros(N)
    for m in range(N):
        b = []
        for l in range(N):
            b.append(m_lTerm(m,l))
        a = np.c_[a,b]
    res = np.matrix(a[:,1:])
    return res

Sx = sigmaX(C.N)
np.save(f"Cache/{C.N}/Sx.npy", Sx)