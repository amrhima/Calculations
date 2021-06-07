import numpy as np

resolution = 100
min = -8
max = 8
x = np.linspace(min, max, resolution)
dx = (x[1] - x[0])
beta = 0
N = 20
invL = 1