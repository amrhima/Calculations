import numpy as np
import Hamlitonian

def eigVs(kx,ky, n, b):
    A = Hamlitonian.hamiltonian(kx, ky, n, b)
    e = np.linalg.eig(A)
    return e