import numpy as np

# Parameters for calculation
resolution = 101
min = -10
max = 10
momenta = np.linspace(min, max, resolution)
momenta_labels = np.linspace(0, resolution-1, resolution, dtype=int)
dx = (momenta[2] - momenta[1])
beta = 2.5
N = 10
invL = 1
delt = 0.05
mu = int(N/2)

# Pauli Sigma_x
def m_lTerm2(m, l):
    if int(m/2) == int(l/2) and m != l:
        return 1
    return 0
def sigmaX(N):
    a = np.zeros(N)
    for m in range(N):
        b = []
        for l in range(N):
            b.append(m_lTerm2(m,l))
        a = np.c_[a,b]
    res = np.matrix(a[:,1:])
    return res

# Delta function
def delta(x):
    return delt/(x**2 + delt**2)