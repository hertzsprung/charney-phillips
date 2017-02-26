#!/usr/bin/env python3
import numpy as np
import numpy.linalg as la
import math
import os

class PositionStencil:
    def __init__(self, b, index):
        i, k = index

        self.origin = b_position(index)
        self.points = [(0.0, 0.0)]

        if i > 0:
            self.add(b, (i-1, k))

        if i < b.shape[0]-1:
            self.add(b, (i+1, k))

        if k > 0:
            self.add(b, (i, k-1))

        if k < b.shape[1]-1:
            self.add(b, (i, k+1))

    def add(self, b, index):
        position = list(b_position(index))
        position[0] -= self.origin[0]
        position[1] -= self.origin[1]

        self.points.append(position)

    def to_matrix(self):
#        terms = 4 if len(self.points) > 3 else 3
        terms = 3
        B = np.zeros((len(self.points), terms))

        for pointi, point in enumerate(self.points):
            B[pointi, 0] = 1
            B[pointi, 1] = point[0]
            B[pointi, 2] = point[1]
#            if terms > 3:
#                B[pointi, 3] = point[0]*point[1]

        return B

class ValueStencil:
    def __init__(self, b, index):
        i, k = index

        self.values = [b[i, k]]

        if i > 0:
            self.add(b, (i-1, k))

        if i < b.shape[0]-1:
            self.add(b, (i+1, k))

        if k > 0:
            self.add(b, (i, k-1))

        if k < b.shape[1]-1:
            self.add(b, (i, k+1))

    def add(self, b, index):
        self.values.append(b[index[0], index[1]])

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

def dump(b, f):
    for i in range(b.shape[0]):
        for k in range(b.shape[1]):
            x, z = b_position((i,k))
            if abs(b[i,k]) > 1e-14:
                print(x, z, b[i,k], file=f)

def b_position(index):
    x = 0.5*delta[0] + delta[0]*index[0] - 0.5*n[0]*delta[0]
    z = delta[1]*index[1]
    return (x, z)

def grad(b):
    grad_b = np.full(b.shape, (0.0, 0.0), dtype="2f")

    for i in range(b.shape[0]):
        for k in range(b.shape[1]):
            stencil = ValueStencil(b, (i, k))

            a_2 = np.dot(Binv[i,k][1], stencil.values) # d/dx
            a_3 = np.dot(Binv[i,k][2], stencil.values) # d/dz

            grad_b[i,k] = (a_2, a_3)

    return grad_b

def three_stage_runge_kutta(b, Uf, dt):
    b_old = np.copy(b)
    grad_b_old = grad(b_old)

    for corr in range(3):
        grad_b = grad(b)

        for i in range(b.shape[0]):
            for k in range(b.shape[1]):
                b[i,k] = b_old[i,k] - 0.5*dt*(np.dot(Uf[i,k], grad_b[i,k]) + np.dot(Uf[i,k], grad_b_old[i,k]))

    return b

def create_Binv_matrix(b):
    Binv = np.full(b.shape, None, dtype='O')
    for i in range(b.shape[0]):
        for k in range(b.shape[1]):
            stencil = PositionStencil(b, (i, k))
            B = stencil.to_matrix()

            Binv[i,k] = la.pinv(B)                

    return Binv

dx = 1e3
dz = 0.5e3
delta = (dx, dz)

nx = 300
nz = 50
n = (nx, nz)

U = 10.0
b = np.zeros((nx,nz+1))
Uf = np.full((nx,nz+1), (U, 0.0), dtype='2f')
Binv = create_Binv_matrix(b)

init_schaer_radial(b)

t = 0
T = 10000
dt = 25
directory = "build"

while t < T:
    if t % 1000 == 0:
        with open(os.path.join(directory, str(t) + ".b.dat"), "w") as f:
            dump(b, f)

        b_analytic = np.zeros((nx,nz+1))
        init_schaer_radial(b_analytic, centre=(-50e3+t*U, 9e3))
        b_error = b - b_analytic

        with open(os.path.join(directory, str(t) + ".berr.dat"), "w") as f:
            dump(b_error, f)

    b = three_stage_runge_kutta(b, Uf, dt)

    t += dt
    print("t =",t, "min(b) =", np.amin(b), "max(b) =", np.amax(b))

with open(os.path.join(directory, str(t) + ".b.dat"), "w") as f:
    dump(b, f)

b_analytic = np.zeros((nx,nz+1))
init_schaer_radial(b_analytic, centre=(-50e3+t*U, 9e3))
b_error = b - b_analytic

with open(os.path.join(directory, str(t) + ".berr.dat"), "w") as f:
    dump(b_error, f)
