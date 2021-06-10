import numpy as np
import matplotlib.pyplot as plt
from numpy.core.function_base import linspace
import Constants as C
import InnerProduct as IP

resolution = C.resolution
min = C.min
max = C.max

delt = 1
def delta(x):
    return delt/(x**2 + delt**2)

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


def plotDelta():
    x = np.linspace(min, max, resolution)
    y = np.linspace(min, max, resolution)
    X, Y = np.meshgrid(x, y)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    W = np.load(f"Cache/{2}/B{0}/En_{0}.npy")
    Z = np.load(f"Cache/{2}/B{0}/En_{1}.npy")
    dE = W - Z
    U = delta(dE-10)
    print(U)
    ax.plot_surface(X, Y, U)
    ax.set_xlabel('kx')
    ax.set_ylabel('ky')
    ax.set_zlabel('delta')
    return plt

def plotIP():
    x = np.linspace(min, max, resolution)
    y = np.linspace(min, max, resolution)
    X, Y = np.meshgrid(x, y)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    kx = linspace(0, resolution-1, 100, dtype=int)
    ky = linspace(0, resolution-1, 100, dtype=int)
    U = IP.conductivity2(0, 1, kx ,ky, 0)
    # print(ky)
    # ax.plot_surface(X, Y, U)
    # ax.set_xlabel('kx')
    # ax.set_ylabel('ky')
    # ax.set_zlabel('delta')
    # return plt


# plot(0).show()
plotDelta()