#!/usr/bin/env python3
import numpy as np
import numpy.linalg as la
import math
import os

def init_schaer_radial(b, position, centre=(-50e3, 9e3), half_width=(25e3,3e3)):
    Ax = half_width[0]
    Az = half_width[1]
    x0 = centre[0]
    z0 = centre[1]
    for i in range(b.shape[0]):
        for k in range(b.shape[1]):
            x, z = position((i,k))
            r = math.sqrt(((x-x0)/Ax)**2 + ((z-z0)/Az)**2)
            if r <= 1:
                b[i,k] = math.cos(math.pi*r/2)**2

def dump(b, position, f):
    for i in range(b.shape[0]):
        for k in range(b.shape[1]):
            x, z = position((i,k))
            if abs(b[i,k]) > 1e-14:
                print(x, z, b[i,k], file=f)

def b_position(index):
    x = 0.5*delta[0] + delta[0]*index[0] - 0.5*n[0]*delta[0]
    z = delta[1]*index[1]
    return (x, z)

def c_position(index):
    x = 0.5*dx + dx*index[0] - 0.5*n[0]*dx
    z = dz*index[1]
    return (x, z+0.5*dz)

def calculate_reconstruction_coeffs():
    B = np.zeros((2, 2))
    B[0, 0] = 1
    B[0, 1] = -0.5*dz
    B[1, 0] = 1
    B[1, 1] = 0.5*dz

    Binv = la.pinv(B)
    return Binv[0]

def reconstruct(b):
    c = np.zeros((b.shape[0], b.shape[1]-1))
    coeffs = calculate_reconstruction_coeffs()
    for i in range(c.shape[0]):
        for k in range(c.shape[1]):
            b_values = [b[i,k], b[i,k+1]]
            c[i,k] = np.dot(coeffs, b_values)
    return c

dx = 1e3
dz = 0.5e3
delta = (dx, dz)

nx = 300
nz = 50
n = (nx, nz)

b = np.zeros((nx,nz+1))
init_schaer_radial(b, b_position)

directory = "build"

c = reconstruct(b)

c_analytic = np.zeros((nx,nz))
init_schaer_radial(c_analytic, c_position)
c_error = c - c_analytic

with open(os.path.join(directory, "cerr.dat"), "w") as f:
    dump(c_error, c_position, f)
