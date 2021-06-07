import numpy as np
import Constants as C

resolution = C.resolution
min = C.min
max = C.max
h = C.dx * 2
B = C.beta

def derivativeKx(b,n,N):
    W1 = np.load(f"Cache/{C.N}/B{b}/Kn_{n}.npy")
    M=np.zeros((1,resolution-2,N))
    for j in range(resolution):
        m=np.zeros((1,N))
        for i in range(1,resolution-1):
            diff = W1[i-1][j] - W1[i+1][j]
            derivative = np.array([(diff / h)])
            m = np.concatenate((m, derivative), axis=0)
        
        d = np.array([np.delete(m, 0, 0)])
        M = np.concatenate((M, d), axis=0)
    
    return np.delete(M, 0, 0)

for n in range(C.N):
    K = derivativeKx(B,n,C.N)
    np.save(f"Cache/{C.N}/B{B}/Kn{n}_x", K)
