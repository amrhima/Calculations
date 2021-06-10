import numpy as np
import time
# Own Imports
import EigenVs
import Constants as C


def getEigenVs():
    resolution = C.resolution
    max = C.max
    min = C.min
    b = C.beta
    n = C.N

    start = time.time()

    K_x = np.linspace(0, resolution-1, 100, dtype=int)
    K_y = np.linspace(0, resolution-1, 100, dtype=int)
    Energy = np.zeros((resolution,resolution, C.N), dtype=np.complex_)
    State = np.zeros((resolution,resolution, C.N, C.N), dtype=np.complex_)
    for kx in K_x:
        for ky in K_y:
            [E, V] = EigenVs.eigVs(kx,ky,n,b)
            Energy[kx][ky] = E
            State[kx][ky] = V
    end = time.time()
    print(end - start)
    return [Energy,State]