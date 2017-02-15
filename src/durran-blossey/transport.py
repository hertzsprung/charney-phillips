#!/usr/bin/env python3
import numpy as np

def ghost_x(f):
    f = np.insert(f, 0, f[0,:], axis=0)
    f = np.insert(f, f.shape[1], f[-1,:], axis=0)
    return f

def ghost_z(f):
    f = np.insert(f, 0, f[:,0], axis=1)
    f = np.insert(f, f.shape[1], f[:,-1], axis=1)
    return f

def interpolate_x(f):
    f_interp = np.zeros(np.subtract(f.shape, (1,0)))
    for i in range(f_interp.shape[0]):
        for k in range(f_interp.shape[1]):
            f_interp[i][k] = 0.5*(f[i][k] + f[i+1][k])

    return f_interp

def interpolate_z(f):
    f_interp = np.zeros(np.subtract(f.shape, (0,1)))
    for i in range(f_interp.shape[0]):
        for k in range(f_interp.shape[1]):
            f_interp[i][k] = 0.5*(f[i][k] + f[i][k+1])

    return f_interp

def grad_x(f, dx):
    # FIXME: dx will be different at boundaries?
    f_grad = np.zeros(np.subtract(f.shape, (1,0)))

    for i in range(f_grad.shape[0]):
        for k in range(f_grad.shape[1]):
            f_grad[i][k] = (f[i+1][k] - f[i][k])/dx

    return f_grad

def b_position(index, d, n):
    x = 0.5*d[0] + d[0]*index[0] - 0.5*n[0]*d[0]
    z = d[1]*index[1]
    return (x, z)

dx = 1e3
dz = 0.5e3
d = (dx, dz)

nx = 300
nz = 50
n = (nx, nz)

b = np.zeros((nx,nz+1))
u = np.zeros((nx+1,nz))
w = np.zeros((nx,nz+1))

t = 0
T = 10000
dt = 25

while t < T:
    u_z = interpolate_z(ghost_z(u))
    db_dx = grad_x(ghost_x(b), dx)
    b = b - dt * interpolate_x(u_z * db_dx)

    t += dt
    print("t =",t)
