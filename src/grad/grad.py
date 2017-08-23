#!/usr/bin/python3
'''
Compare analytic and numerical approximations of the Schaer tracer gradient.
'''

import numpy as np
import numpy.linalg as la
import math
import os
from grad_schemes import *

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
        self.f = np.zeros(self.mesh.shape)

        for i in range(self.f.shape[0]):
            for k in range(self.f.shape[1]):
                self.f[i,k] = initialiser(self.mesh.position((i, k))) 

    def dumpTo(self, filename):
        with open(filename, "w") as file:
            for i in range(self.f.shape[0]):
                for k in range(self.f.shape[1]):
                    x, z = self.mesh.position((i,k))
                    if abs(self.f[i,k]) > 1e-14:
                        print(x, z, self.f[i,k], file=file)

class VectorField:
    def __init__(self, mesh, initialiser):
        self.mesh = mesh
        self.f = np.full(self.mesh.shape, (0.0, 0.0), dtype="2f")

        for i in range(self.f.shape[0]):
            for k in range(self.f.shape[1]):
                self.f[i,k] = initialiser(self.mesh.position((i, k))) 

    def dumpTo(self, filename):
        with open(filename, "w") as file:
            for i in range(self.f.shape[0]):
                for k in range(self.f.shape[1]):
                    x, z = self.mesh.position((i,k))
                    if la.norm(self.f[i,k]) > 1e-14:
                        print(x, z, self.f[i,k][0], self.f[i,k][1], file=file)

class SchaerRadial:
    def __init__(self, centre=(-50e3, 9e3), halfWidth=(25e3,3e3)):
        self.centre = centre
        self.halfWidth = halfWidth

    def value(self, p):
        Ax = self.halfWidth[0]
        Az = self.halfWidth[1]
        x0 = self.centre[0]
        z0 = self.centre[1]
        x, z = p
        r = math.sqrt(((x-x0)/Ax)**2 + ((z-z0)/Az)**2)
        if r <= 1:
            return math.cos(math.pi*r/2)**2
        else:
            return 0
    
    def gradient(self, p):
        Ax = self.halfWidth[0]
        Az = self.halfWidth[1]
        x0 = self.centre[0]
        z0 = self.centre[1]
        x, z = p
        r = math.sqrt(((x-x0)/Ax)**2 + ((z-z0)/Az)**2)
        if r <= 1:
            return [-math.sin(math.pi*(x-x0)/Ax), -math.sin(math.pi*(z-z0)/Az)]
        else:
            return 0

directory = "build"
mesh = Mesh(nCells=(300, 50), delta=(1e3, 0.5e3))
tracer = SchaerRadial()
b = ScalarField(mesh, tracer.value)
grad_b_analytic = VectorField(mesh, tracer.gradient)

b.dumpTo(os.path.join(directory, 'b.dat'))
grad_b_analytic.dumpTo(os.path.join(directory, 'grad_b_analytic.dat'))

