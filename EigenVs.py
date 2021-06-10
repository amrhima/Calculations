import numpy as np
import time
# Own Imports
import Constants as C
import Hamlitonian

def eigVs(kx,ky, n, b):
    A = Hamlitonian.H(kx, ky, n, b)
    e = np.linalg.eig(A)
    return e

def getEigenVs():
    resolution = C.resolution
    b = C.beta
    n = C.N
    lin = C.momenta
    start = time.time()
    K_x = C.momenta_labels
    K_y = C.momenta_labels
    Energy = np.zeros((resolution,resolution, C.N), dtype=np.complex_)
    State = np.zeros((resolution,resolution, C.N, C.N), dtype=np.complex_)
    for kx in K_x:
        for ky in K_y:
            [E, V] = eigVs(lin[kx],lin[ky],n,b)
            Energy[kx][ky] = E
            State[kx][ky] = V
    end = time.time()
    print(end - start)
    return [Energy,State]