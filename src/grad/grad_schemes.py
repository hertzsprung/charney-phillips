import numpy as np
import numpy.linalg as la
from mesh import *

class Stencil:
    def __init__(self, indices, f, origin):
        self.indices = indices
        self.points = [f.mesh.position(index) for index in indices]
        self.points = [(x - origin[0], z - origin[1]) for x, z in self.points]
        self.f = f

    def values(self):
        return [self.f[index] for index in self.indices]

class StencilType:
    def __init__(self, indices):
        self.indices = indices

    def stencilFor(self, f, index):
        indices = []

        for p in self.indices:
            i = index[0] + p[0]
            k = index[1] + p[1]

            if i >= 0 and i < f.shape[0] and k >=0 and k < f.shape[1]:
                indices.append((i,k))

        return Stencil(indices, f, index)

class GradScheme:
    def __init__(self, stencilType, basis):
        self.stencilType = stencilType
        self.basis = basis

    def grad(self, f):
        Binv = np.full(f.shape, None, dtype='O')
        for i in range(f.shape[0]):
            for k in range(f.shape[1]):
                stencil = self.stencilType.stencilFor(f, (i, k))
                Binv[i,k] = self.basis.inverseMatrix(stencil.points)

        def initialiser(mesh, index):
            stencil = self.stencilType.stencilFor(f, index)
            return self.basis.gradient(Binv[index], stencil.values())

        return VectorField(f.mesh, initialiser)

    def __repr__(self):
        return "grad_{points}_{basis}".format(
                points=len(self.stencilType.indices),
                basis=self.basis.__class__.__name__)
