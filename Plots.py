import numpy as np
import matplotlib.pyplot as plt
import Constants as C
# import EigenVs as Eig

def plotEnergyVsY():
    N = int(C.N/2)
    mid = int((C.resolution-1)/2)
    ky = C.y_momenta
    F = np.load(f"Data/E_{C.beta}_{C.N}.npy")
    W = np.real(F[:,mid,N-1])
    Z = np.real(F[:,mid,N])
    G = np.real(F[:,mid,N-2])
    H = np.real(F[:,mid,N+1])
    plt.plot(ky, W)
    plt.plot(ky, Z)
    plt.plot(ky, G)
    plt.plot(ky, H)
    return plt

def plotEnergyVsX():
    N = int(C.N/2)
    mid = int((C.resolution-1)/2)
    kx = C.x_momenta
    F = np.load(f"Data/E_{C.beta}_{C.N}.npy")
    print(F[mid,mid,N])
    print(F[mid,mid,N-1])
    W = np.real(F[mid,:,N-1])
    Z = np.real(F[mid,:,N])
    G = np.real(F[mid,:,N-2])
    H = np.real(F[mid,:,N+1])
    plt.plot(kx, W)
    plt.plot(kx, Z)
    plt.plot(kx, G)
    plt.plot(kx, H)
    return plt

def PlotEnergy3D():
    N = int(C.N/2)
    kx = C.x_momenta
    ky = C.y_momenta
    X, Y = np.meshgrid(kx, ky)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    F = np.load(f"Data/E_{C.beta}_{C.N}.npy")
    W = np.real(F[:,:,N-1])
    Z = np.real(F[:,:,N])
    ax.plot_surface(X, Y, W)
    ax.plot_surface(X, Y, Z)
    ax.set_xlabel('kx')
    ax.set_ylabel('ky')
    ax.set_zlabel('E')
    return plt

plotEnergyVsY().savefig(f"EnergyGraphs/Ey_{C.beta}_{C.N}-.png")
# plotEnergyVsX().savefig(f"EnergyGraphs/Ex_{C.beta}_{C.N}-.png")