import numpy as np
import math

# Parameters
resolution = 101
x_momenta = np.linspace(-math.pi, math.pi, resolution)
y_momenta = np.linspace(-10, 10, resolution)
momenta_labels = np.linspace(0, resolution-1, resolution, dtype=int)
dkx = (x_momenta[2] - x_momenta[1])
dky = (y_momenta[2] - y_momenta[1])
beta = 0
N = 42
invL = 1
delt = 0.001
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


# lambda > 1 mu
# fix x => [-pi,pi]
# N ~ [-10,9,....0,....9,10]