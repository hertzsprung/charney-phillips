#!/usr/bin/python3
'''
Compare analytic and numerical approximations of the Schaer tracer gradient.
'''

import numpy as np
import numpy.linalg as la
import math
import os

def b_position(index):
    x = 0.5*delta[0] + delta[0]*index[0] - 0.5*n[0]*delta[0]
    z = delta[1]*index[1]
    return (x, z)

def dump_scalar(b, f):
    for i in range(b.shape[0]):
        for k in range(b.shape[1]):
            x, z = b_position((i,k))
            if abs(b[i,k]) > 1e-14:
                print(x, z, b[i,k], file=f)

def dump_vector(b, f):
    for i in range(b.shape[0]):
        for k in range(b.shape[1]):
            x, z = b_position((i,k))
            if la.norm(b[i,k]) > 1e-14:
                print(x, z, b[i,k][0], b[i,k][1], file=f)

def init_schaer_radial(b, centre=(-50e3, 9e3), half_width=(25e3,3e3)):
    Ax = half_width[0]
    Az = half_width[1]
    x0 = centre[0]
    z0 = centre[1]
    for i in range(b.shape[0]):
        for k in range(b.shape[1]):
            x, z = b_position((i,k))
            r = math.sqrt(((x-x0)/Ax)**2 + ((z-z0)/Az)**2)
            if r <= 1:
                b[i,k] = math.cos(math.pi*r/2)**2

def init_schaer_radial_grad(b, centre=(-50e3, 9e3), half_width=(25e3,3e3)):
    Ax = half_width[0]
    Az = half_width[1]
    x0 = centre[0]
    z0 = centre[1]

    for i in range(b.shape[0]):
        for k in range(b.shape[1]):
            x, z = b_position((i,k))
            r = math.sqrt(((x-x0)/Ax)**2 + ((z-z0)/Az)**2)
            if r <= 1:
                b[i,k] = [-math.sin(math.pi*(x-x0)/Ax), -math.sin(math.pi*(z-z0)/Az)]

dx = 1e3
dz = 0.5e3
delta = (dx, dz)

nx = 300
nz = 50
n = (nx, nz)

directory = "build"

b = np.zeros((nx,nz+1))
grad_b_ana = np.full(b.shape, (0.0, 0.0), dtype="2f")

init_schaer_radial(b)
init_schaer_radial_grad(grad_b_ana)

with open(os.path.join(directory, "b.dat"), "w") as f:
    dump_scalar(b, f)

with open(os.path.join(directory, "grad_b_ana.dat"), "w") as f:
    dump_vector(grad_b_ana, f)
