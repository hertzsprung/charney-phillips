import numpy as np
import numpy.linalg as la
from mesh import *

class Stencil:
    def __init__(self, indices, f, origin):
        self.indices = indices
        self.points = [f.mesh.position(index) for index in indices]
        self.points = [(x - origin[0], z - origin[1]) for x, z in self.points]
        self.f = f

    def matrix(self):
        B = np.zeros((len(self.points), 3))

        for pointi, point in enumerate(self.points):

            B[pointi, 0] = 1
            B[pointi, 1] = point[0]
            B[pointi, 2] = point[1]

        return B

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

class Grad4Point:
    def __init__(self):
        self.stencilType = StencilType([
                (-1, 0),
                ( 1, 0),
                ( 0,-1),
                ( 0, 1)
        ])

    def grad(self, f):
        Binv = np.full(f.shape, None, dtype='O')
        for i in range(f.shape[0]):
            for k in range(f.shape[1]):
                stencil = self.stencilType.stencilFor(f, (i, k))
                B = stencil.matrix()

                Binv[i,k] = la.pinv(B)

        def initialiser(mesh, index):
            i, k = index
            stencil = self.stencilType.stencilFor(f, index)

            a_2 = np.dot(Binv[i,k][1], stencil.values()) # d/dx
            a_3 = np.dot(Binv[i,k][2], stencil.values()) # d/dz

            return (a_2, a_3)

        return VectorField(f.mesh, initialiser)

