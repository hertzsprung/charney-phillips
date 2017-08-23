import numpy as np
import numpy.linalg as la
from mesh import *

class PositionStencil:
    def __init__(self, f, index):
        i, k = index
        mesh = f.mesh

        self.origin = mesh.position(index)
        self.points = []

        if i > 0:
            self.add(mesh, (i-1, k))

        if i < f.shape[0]-1:
            self.add(mesh, (i+1, k))

        if k > 0:
            self.add(mesh, (i, k-1))

        if k < f.shape[1]-1:
            self.add(mesh, (i, k+1))

    def add(self, mesh, index):
        position = list(mesh.position(index))
        position[0] -= self.origin[0]
        position[1] -= self.origin[1]

        self.points.append(position)

    def to_matrix(self):
        B = np.zeros((len(self.points), 3))

        for pointi, point in enumerate(self.points):
            B[pointi, 0] = 1
            B[pointi, 1] = point[0]
            B[pointi, 2] = point[1]

        return B

class ValueStencil:
    def __init__(self, f, index):
        i, k = index

        self.values = []

        if i > 0:
            self.add(f, (i-1, k))

        if i < f.shape[0]-1:
            self.add(f, (i+1, k))

        if k > 0:
            self.add(f, (i, k-1))

        if k < f.shape[1]-1:
            self.add(f, (i, k+1))

    def add(self, f, index):
        self.values.append(f[index[0], index[1]])

class Grad4Point:
    def grad(self, f):
        Binv = np.full(f.shape, None, dtype='O')
        for i in range(f.shape[0]):
            for k in range(f.shape[1]):
                stencil = PositionStencil(f, (i, k))
                B = stencil.to_matrix()

                Binv[i,k] = la.pinv(B)

        def initialiser(mesh, index):
            i, k = index
            stencil = ValueStencil(f, index)

            a_2 = np.dot(Binv[i,k][1], stencil.values) # d/dx
            a_3 = np.dot(Binv[i,k][2], stencil.values) # d/dz

            return (a_2, a_3)

        return VectorField(f.mesh, initialiser)

