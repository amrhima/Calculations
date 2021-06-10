import numpy as np
import Constants as C

#sigma_x
def m_lTerm2(m, l):
    if int(m/2) == int(l/2) and m != l:
        return 1
    return 0

#block sigma_x
def m_lTerm(m, l):
    if (int((m-2)/2) == int(l/2) or int(m/2) == int((l-2)/2) ) and (m-l)%2 == 0 and m != l:
        return 1
    return 0
def sigmaX2(N):
    a = np.zeros(N)
    for m in range(N):
        b = []
        for l in range(N):
            b.append(m_lTerm2(m,l))
        a = np.c_[a,b]
    res = np.matrix(a[:,1:])
    return res

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
Sx2 = sigmaX2(C.N)
np.save(f"Cache/{C.N}/Sx.npy", Sx2)
print(Sx2)