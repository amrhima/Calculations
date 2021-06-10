import numpy as np

resolution = 101
min = -10
max = 10
x = np.linspace(min, max, resolution)
dx = (x[2] - x[1])
beta = 0
N = 10
invL = 0
sigmaX = np.load(f"Cache/{N}/Sx.npy")