import numpy as np
import matplotlib.pyplot as plt
import Constants as C

resolution = C.resolution
min = C.min
max = C.max

def plot(b):
    x = np.linspace(min, max, resolution)
    y = np.linspace(min, max, resolution)
    X, Y = np.meshgrid(x, y)
    fig = plt.figure()
    n=int(C.N/2)
    ax = plt.axes(projection='3d')
    W = np.load(f"Cache/{C.N}/B{b}/En_{n-1}.npy")
    Z = np.load(f"Cache/{C.N}/B{b}/En_{n}.npy")

    ax.plot_surface(X, Y, W)
    ax.plot_surface(X, Y, Z)
    ax.set_xlabel('kx')
    ax.set_ylabel('ky')
    ax.set_zlabel('E')
    return plt

def plot2D(b, j):
    x = np.linspace(min, max, resolution)
    y = x[j]
    W = np.load(f"Cache/{C.N}/B{b}/En_4.npy")
    Z = np.load(f"Cache/{C.N}/B{b}/En_5.npy")

    plt.plot(x, W[j])
    plt.legend(f"E")
    return plt


plot(0).show()