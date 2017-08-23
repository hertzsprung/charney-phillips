#!/usr/bin/python3
'''
Compare analytic and numerical approximations of the Schaer tracer gradient.
'''

import numpy as np
import numpy.linalg as la
import math
import os
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
            return [-math.pi/(2*Ax)*math.sin(math.pi*(x-x0)/Ax), -math.pi/(2*Az)*math.sin(math.pi*(z-z0)/Az)]
        else:
            return 0

directory = "build"
mesh = Mesh(nCells=(300, 50), delta=(1e3, 0.5e3))
tracer = SchaerRadial()
b = ScalarField(mesh, tracer.value)
grad_b_analytic = VectorField(mesh, tracer.gradient)

grad_b_4point = Grad4Point().grad(b)

b.dumpTo(os.path.join(directory, 'b.dat'))
grad_b_analytic.dumpTo(os.path.join(directory, 'grad_b_analytic.dat'))
grad_b_4point.dumpTo(os.path.join(directory, 'grad_b_4point.dat'))
