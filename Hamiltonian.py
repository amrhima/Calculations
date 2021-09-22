import numpy as np
import math
import Constants as C

def m_lTerm(m, l, kx, ky, B, N):
    if int(m/2) == int(l/2) and m != l:
        n = int((m+l)/4) - int((N-1)/4)
        return ((n*2*math.pi*C.invL+kx)+(m-l)*1.j*ky)
    if (int((m-2)/2) == int(l/2) or int(m/2) == int((l-2)/2) ) and (m-l)%2 == 1:
        if m%2 == 0:
            return -B*C.invL*0.5*1.j
        return B*C.invL*0.5*1.j
    return 0

def H(kx, ky, N, B):
    a = np.zeros(N)
    for m in range(N):
        b = []
        for l in range(N):
            b.append(m_lTerm(m,l, kx, ky, B, N))
        a = np.c_[a,b]
    res = np.matrix(a[:,1:])
    return res


# print(H(0,0,6,0))