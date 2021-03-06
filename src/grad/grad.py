#!/usr/bin/python3
'''
Compare analytic and numerical approximations of the Schaer tracer gradient.
'''

import numpy as np
import math
import os

from basis import *
from grad_schemes import *
from mesh import *

class SchaerRadial:
    def __init__(self, centre=(-50e3, 9e3), halfWidth=(25e3,3e3)):
        self.centre = centre
        self.halfWidth = halfWidth

    def value(self, mesh, index):
        Ax = self.halfWidth[0]
        Az = self.halfWidth[1]
        x0 = self.centre[0]
        z0 = self.centre[1]
        x, z = mesh.position(index)
        r = math.sqrt(((x-x0)/Ax)**2 + ((z-z0)/Az)**2)
        if r <= 1:
            return math.cos(math.pi*r/2)**2
        else:
            return 0
    
    def gradient(self, mesh, index):
        Ax = self.halfWidth[0]
        Az = self.halfWidth[1]
        x0 = self.centre[0]
        z0 = self.centre[1]
        x, z = mesh.position(index)
        r = math.sqrt(((x-x0)/Ax)**2 + ((z-z0)/Az)**2)
        if r <= 1:
            return (
                -math.pi*(x-x0)/(Ax**2*r)*math.sin(math.pi*r),#d/dx
                -math.pi*(z-z0)/(Az**2*r)*math.sin(math.pi*r) #d/dz
            )
        else:
            return 0

def l2error(numeric, analytic):
    differenceSquared = 0
    analyticSquared = 0

    for i in range(analytic.shape[0]):
        for k in range(analytic.shape[1]):
            differenceSquared += (numeric[i,k] - analytic[i,k])**2
            analyticSquared += analytic[i,k]**2

    return math.sqrt(differenceSquared/analyticSquared)

def linferror(numeric, analytic):
    maxMagDifference = 0
    maxMagAnalytic = 0

    for i in range(analytic.shape[0]):
        for k in range(analytic.shape[1]):
            magDifference = abs(numeric[i,k] - analytic[i,k])
            magAnalytic = abs(analytic[i,k])

            if magDifference > maxMagDifference:
                maxMagDifference = magDifference

            if magAnalytic > maxMagAnalytic:
                maxMagAnalytic = magAnalytic

    return maxMagDifference / maxMagAnalytic

def dump_errors(numeric, analytic):
    x_numeric = numeric.component(0)
    x_analytic = analytic.component(0)

    print("l2", l2error(x_numeric, x_analytic))
    print("linf", linferror(x_numeric, x_analytic))

directory = "build"
mesh = Mesh(nCells=(300, 50), delta=(1e3, 0.5e3))
tracer = SchaerRadial()
b = ScalarField(mesh, tracer.value)
grad_b_analytic = VectorField(mesh, tracer.gradient)

b.dumpTo(os.path.join(directory, 'b.dat'))
grad_b_analytic.dumpTo(os.path.join(directory, 'grad_b_analytic.dat'))

point5 = StencilType([(0, 0), (-1, 0), (1, 0), (0,-1), (0, 1)])
point6 = StencilType([(0, 0), (-1, 0), (0, 1), (-1, 1), (0, -1), (-1, -1)])
point9 = StencilType([
    (0, 0), (-1, 0), (1, 0),
    (0, 1), (-1, 1), (1, 1),
    (0, -1), (-1, -1), (1, -1)
])
point12 = StencilType([
        (0, 0), (-2, 0), (-1, 0), (1, 0),
        (0, 1), (-2, 1), (-1, 1), (1, 1),
        (0, -1), (-2, -1), (-1, -1), (1, -1)
])

schemes = [
    GradScheme(point5, Bilinear()),
    GradScheme(point6, Bilinear()),
    GradScheme(point9, Bilinear()),
    GradScheme(point12, Bilinear()),
    GradScheme(point5, Quadratic()),
    GradScheme(point6, Quadratic()),
    GradScheme(point9, Quadratic()),
]

for scheme in schemes:
    print(scheme)
    grad_b_numeric = scheme.grad(b)
    grad_b_numeric.dumpTo(os.path.join(directory, "{scheme}.dat".format(scheme=scheme)))
    dump_errors(grad_b_numeric, grad_b_analytic)
    print()


