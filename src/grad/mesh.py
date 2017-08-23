import numpy as np
import numpy.linalg as la

class Mesh:
    def __init__(self, nCells, delta):
        self.delta = delta
        nx, nz = nCells
        self.shape = (nx, nz+1) # for Charney--Phillips staggering

    def position(self, index):
        x = 0.5*self.delta[0] + self.delta[0]*index[0] - 0.5*self.shape[0]*self.delta[0]
        z = self.delta[1]*index[1]
        return (x, z)

class ScalarField:
    def __init__(self, mesh, initialiser):
        self.mesh = mesh
        self.shape = mesh.shape
        self.f = np.zeros(self.shape)

        for i in range(self.shape[0]):
            for k in range(self.shape[1]):
                self.f[i,k] = initialiser(self.mesh, (i, k))

    def __getitem__(self, key):
        return self.f.__getitem__(key)

    def dumpTo(self, filename):
        with open(filename, "w") as file:
            for i in range(self.shape[0]):
                for k in range(self.shape[1]):
                    x, z = self.mesh.position((i,k))
                    if abs(self[i,k]) > 1e-14:
                        print(x, z, self[i,k], file=file)

class VectorField:
    def __init__(self, mesh, initialiser):
        self.mesh = mesh
        self.shape = self.mesh.shape
        self.f = np.full(self.shape, (0.0, 0.0), dtype="2f")

        for i in range(self.shape[0]):
            for k in range(self.shape[1]):
                self.f[i,k] = initialiser(self.mesh, (i, k))

    def dumpTo(self, filename):
        with open(filename, "w") as file:
            for i in range(self.shape[0]):
                for k in range(self.shape[1]):
                    x, z = self.mesh.position((i,k))
                    if la.norm(self.f[i,k]) > 1e-14:
                        print(x, z, self.f[i,k][0], self.f[i,k][1], file=file)

