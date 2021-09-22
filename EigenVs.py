import numpy as np
import time
from pathlib import Path
# Own Imports
import Constants as C
import Hamiltonian
import math

def eigVs(kx,ky, n, b):
    A = Hamiltonian.H(kx, ky, n, b)
    [E,V] = np.linalg.eigh(A)
    # idx = E.argsort()[::1]   
    # E = E[idx]
    # V = V[:,idx]
    return [E,V]

def saveEigenVs():
    resolution = C.resolution
    b = C.beta
    n = C.N
    start = time.time()
    K_x = C.momenta_labels
    K_y = C.momenta_labels
    Energy = np.zeros((resolution,resolution, C.N), dtype=np.complex_)
    State = np.zeros((resolution,resolution, C.N, C.N), dtype=np.complex_)
    for kx in K_x:
        for ky in K_y:
            [E, V] = eigVs(C.x_momenta[kx],C.y_momenta[ky],n,b)
            Energy[kx][ky] = E
            State[kx][ky] = V
    end = time.time()
    print(end - start)
    np.save(f"Data/E_{C.beta}_{C.N}.npy", Energy)
    np.save(f"Data/V_{C.beta}_{C.N}.npy", State)
    return [Energy,State]


# saveEigenVs()
A = Hamiltonian.H(0, 10, 42, 0)
E1 = eigVs(0,10,42,0)[0][21]
V1 = eigVs(0,10,42,0)[1][:,21]
# V2 = eigVs(0,10,42,0)[1][20].reshape(42,1)
R1 = A * V1
print((V1  * E1) - R1)
# print(R1)
# print(V1 * E1)