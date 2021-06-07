import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import shape
# Own Imports
import EigenVs
import Constants as C

resolution = C.resolution
max = C.max
min = C.min
b = C.beta
n = C.N

def eigV(N, kx, ky):
    res2 = EigenVs.eigVs(kx,ky,n,b)
    res = res2[0][N]
    return res

def eigVs(N, kx, ky):
    j=np.array([])
    for i in kx:
        k = eigV(N, i, ky)
        j = np.append(j, k)
    res = np.array([j])
    return res

def eigVs3D(N, kx, ky):
    j=np.zeros((1,resolution))
    for i in ky:
        k = eigVs(N,kx,i)
        j = np.concatenate((j, k), axis=0)
    
    res = np.delete(j, 0, 0)
    return res


x = np.linspace(min, max, resolution)
y = np.linspace(min, max, resolution)

for m in range(n):
    W = eigVs3D(m,x,y)
    np.save(f"Cache/{C.N}/B{b}/En_{m}", W)