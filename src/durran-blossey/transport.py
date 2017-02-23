#!/usr/bin/env python3
import numpy as np
import math
import os

def ghost_x(f):
    f = np.insert(f, 0, f[0,:], axis=0)
    f = np.insert(f, f.shape[0], f[-1,:], axis=0)
    return f

def ghost_z(f):
    f = np.insert(f, 0, f[:,0], axis=1)
    f = np.insert(f, f.shape[1], f[:,-1], axis=1)
    return f

def interpolate_x(f):
    f_interp = np.zeros(np.subtract(f.shape, (1,0)))
    for i in range(f_interp.shape[0]):
        for k in range(f_interp.shape[1]):
            f_interp[i,k] = 0.5*(f[i,k] + f[i+1,k])

    return f_interp

def interpolate_z(f):
    f_interp = np.zeros(np.subtract(f.shape, (0,1)))
    for i in range(f_interp.shape[0]):
        for k in range(f_interp.shape[1]):
            f_interp[i,k] = 0.5*(f[i,k] + f[i,k+1])

    return f_interp

def grad_x(f, dx):
    # FIXME: dx will be different at boundaries?
    f_grad = np.zeros(np.subtract(f.shape, (1,0)))

    for i in range(f_grad.shape[0]):
        for k in range(f_grad.shape[1]):
            f_grad[i,k] = (f[i+1,k] - f[i,k])/dx

    return f_grad

def grad_z(f, dz):
    f_grad = np.zeros(np.subtract(f.shape, (0,1)))

    for i in range(f_grad.shape[0]):
        for k in range(f_grad.shape[1]):
            f_grad[i,k] = (f[i,k+1] - f[i,k])/dz

    return f_grad

def b_position(index, delta, n):
    x = 0.5*delta[0] + delta[0]*index[0] - 0.5*n[0]*delta[0]
    z = delta[1]*index[1]
    return (x, z)

def init_schaer_radial(b, delta, n, centre=(-50e3, 9e3), half_width=(25e3,3e3)):
    Ax = half_width[0]
    Az = half_width[1]
    x0 = centre[0]
    z0 = centre[1]
    for i in range(b.shape[0]):
        for k in range(b.shape[1]):
            x, z = b_position((i,k), delta, n)
            r = math.sqrt(((x-x0)/Ax)**2 + ((z-z0)/Az)**2)
            if r <= 1:
                b[i,k] = math.cos(math.pi*r/2)**2

def dump(b, delta, n, f):
    for i in range(b.shape[0]):
        for k in range(b.shape[1]):
            x, z = b_position((i,k), delta, n)
            if abs(b[i,k]) > 1e-14:
                print(x, z, b[i,k], file=f)

def forward_euler(b, u, dt):
    u_z = interpolate_z(ghost_z(u))
    w_z = interpolate_z(w)
    db_dx = grad_x(ghost_x(b), dx)
    db_dz = grad_z(b, dz)

    return b - dt * (interpolate_x(u_z * db_dx) + interpolate_z(ghost_z(w_z * db_dz)))

def three_stage_runge_kutta(b, u, dt):
    u_z = interpolate_z(ghost_z(u))
    w_z = interpolate_z(w)
    b_old = np.copy(b)
    db_old_dx = grad_x(ghost_x(b_old), dx)
    db_old_dz = grad_z(b_old, dz)

    for corr in range(3):
        db_dx = grad_x(ghost_x(b), dx)
        db_dz = grad_z(b, dz)
        b = b_old - 0.5*dt*(interpolate_x(u_z * db_dx) + interpolate_x(u_z * db_old_dx)) # TODO: w

    return b

dx = 1e3
dz = 0.5e3
delta = (dx, dz)

nx = 300
nz = 50
n = (nx, nz)

U = 10.0
b = np.zeros((nx,nz+1))
u = np.full((nx+1,nz), U)
w = np.full((nx,nz+1), 0.0)

init_schaer_radial(b, delta, n)

t = 0
T = 10000
dt = 25
directory = "build"

while t < T:
    if t % 1000 == 0:
        with open(os.path.join(directory, str(t) + ".b.dat"), "w") as f:
            dump(b, delta, n, f)

        b_analytic = np.zeros((nx,nz+1))
        init_schaer_radial(b_analytic, delta, n, centre=(-50e3+t*U, 9e3))
        b_error = b - b_analytic

        with open(os.path.join(directory, str(t) + ".berr.dat"), "w") as f:
            dump(b_error, delta, n, f)

    b = three_stage_runge_kutta(b, u, dt)

    t += dt
    print("t =",t, "min(b) =", np.amin(b), "max(b) =", np.amax(b))

with open(os.path.join(directory, str(t) + ".b.dat"), "w") as f:
    dump(b, delta, n, f)

b_analytic = np.zeros((nx,nz+1))
init_schaer_radial(b_analytic, delta, n, centre=(-50e3+t*U, 9e3))
b_error = b - b_analytic

with open(os.path.join(directory, str(t) + ".berr.dat"), "w") as f:
    dump(b_error, delta, n, f)
