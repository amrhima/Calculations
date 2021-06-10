import numpy as np
import matplotlib.pyplot as plt
import Constants as C
import EigenVs as Eig

resolution = C.resolution
min = C.min
max = C.max


def plot(b):
    kx = C.momenta
    ky = C.momenta
    X, Y = np.meshgrid(kx, ky)
    fig = plt.figure()
    n=int(C.N/2)
    ax = plt.axes(projection='3d')
    F = Eig.getEigenVs()[0]
    W = np.real(F[:,:,n])
    Z = np.real(F[:,:,n-1])

    ax.plot_surface(X, Y, W)
    ax.plot_surface(X, Y, Z)
    ax.set_xlabel('kx')
    ax.set_ylabel('ky')
    ax.set_zlabel('E')
    return plt


def plotDelta():
    kx = C.momenta
    ky = C.momenta
    X, Y = np.meshgrid(kx, ky)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    F = Eig.getEigenVs()[0]
    W = np.real(F[:,:,0])
    Z = np.real(F[:,:,1])
    dE = W - Z
    U = C.delta(dE-10)
    ax.plot_surface(X, Y, U)
    ax.set_xlabel('kx')
    ax.set_ylabel('ky')
    ax.set_zlabel('delta')
    return plt

