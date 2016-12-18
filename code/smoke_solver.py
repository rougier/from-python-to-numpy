# -----------------------------------------------------------------------------
# From Numpy to Python
# Copyright (2017) Nicolas P. Rougier - BSD license
# More information at https://github.com/rougier/numpy-book
# -----------------------------------------------------------------------------
"""
Real-Time Fluid Dynamics for Games by Jos Stam (2003).

Copyright (c) 2015 Alberto Santini - MIT License
Code adapted from Alberto Santini implementation available at:
https://github.com/albertosantini/python-fluid
"""
import numpy as np


def set_bnd(N, b, x):
    """We assume that the fluid is contained in a box with solid walls.

    No flow should exit the walls. This simply means that the horizontal
    component of the velocity should be zero on the vertical walls, while the
    vertical component of the velocity should be zero on the horizontal walls.
    For the density and other fields considered in the code we simply assume
    continuity. The following code implements these conditions.
    """

    if b == 1:
        x[0, 1:-1] = -x[1, 1:-1]
        x[-1, 1:-1] = -x[N, 1:-1]
    else:
        x[ 0, 1:-1] = x[1, 1:-1]
        x[-1, 1:-1] = x[N, 1:-1]
    if b == 2:
        x[1:-1,  0] = -x[1:-1, 1]
        x[1:-1, -1] = -x[1:-1, N]
    else:
        x[1:-1,  0] = x[1:-1, 1]
        x[1:-1, -1] = x[1:-1, N]

    x[ 0,  0] = 0.5 * (x[1,  0] + x[ 0, 1])
    x[ 0, -1] = 0.5 * (x[1, -1] + x[ 0, N])
    x[-1,  0] = 0.5 * (x[N,  0] + x[-1, 1])
    x[-1, -1] = 0.5 * (x[N, -1] + x[-1, N])


def lin_solve(N, b, x, x0, a, c):
    """lin_solve."""

    for k in range(20):
        x[1:-1, 1:-1] = (x0[1:-1, 1:-1] +
                         a * (x[:N, 1:-1] + x[2:, 1:-1] +
                              x[1:-1, :N] + x[1:-1, 2:])) / c
        set_bnd(N, b, x)


def add_source(N, x, s, dt):
    """Addition of forces: the density increases due to sources."""
    x += dt * s


def diffuse(N, b, x, x0, diff, dt):
    """Diffusion: the density diffuses at a certain rate.

    The basic idea behind our method is to find the densities which when
    diffused backward in time yield the densities we started with. The simplest
    iterative solver which works well in practice is Gauss-Seidel relaxation.
    """

    a = dt * diff * N * N
    lin_solve(N, b, x, x0, a, 1 + 4 * a)


def advect(N, b, d, d0, u, v, dt):
    """Advection: the density follows the velocity field.

    The basic idea behind the advection step. Instead of moving the cell
    centers forward in time through the velocity field, we look for the
    particles which end up exactly at the cell centers by tracing backwards in
    time from the cell centers.
    """

    dt0 = dt * N

    I, J = np.indices((N, N))
    I += 1
    J += 1
    X = I - dt0 * u[I, J]
    Y = J - dt0 * v[I, J]

    X = np.minimum(np.maximum(X, 0.5), N+0.5)
    I0 = X.astype(int)
    I1 = I0+1
    S1 = X - I0
    S0 = 1 - S1

    Y = np.minimum(np.maximum(Y, 0.5), N+0.5)
    J0 = Y.astype(int)
    J1 = J0 + 1
    T1 = Y - J0
    T0 = 1 - T1

    d[I, J] = (S0 * (T0 * d0[I0, J0] + T1 * d0[I0, J1])
             + S1 * (T0 * d0[I1, J0] + T1 * d0[I1, J1]))

    set_bnd(N, b, d)


def project(N, u, v, p, div):
    """ Projection """

    h = 1.0 / N
    div[1:-1, 1:-1] = (-0.5 * h *
                       (u[2:, 1:-1] - u[0:N, 1:-1] +
                        v[1:-1, 2:] - v[1:-1, 0:N]))
    p[1:-1, 1:-1] = 0
    set_bnd(N, 0, div)
    set_bnd(N, 0, p)
    lin_solve(N, 0, p, div, 1, 4)
    u[1:-1, 1:-1] -= 0.5 * (p[2:, 1:-1] - p[0:N, 1:-1]) / h
    v[1:-1, 1:-1] -= 0.5 * (p[1:-1, 2:] - p[1:-1, 0:N]) / h
    set_bnd(N, 1, u)
    set_bnd(N, 2, v)


def dens_step(N, x, x0, u, v, diff, dt):
    # Density step: advection, diffusion & addition of sources.
    add_source(N, x, x0, dt)
    x0, x = x, x0  # swap
    diffuse(N, 0, x, x0, diff, dt)
    x0, x = x, x0  # swap
    advect(N, 0, x, x0, u, v, dt)


def vel_step(N, u, v, u0, v0, visc, dt):
    # Velocity step: self-advection, viscous diffusion & addition of forces

    add_source(N, u, u0, dt)
    add_source(N, v, v0, dt)
    u0, u = u, u0  # swap
    
    diffuse(N, 1, u, u0, visc, dt)
    v0, v = v, v0  # swap
    
    diffuse(N, 2, v, v0, visc, dt)
    project(N, u, v, u0, v0)
    u0, u = u, u0  # swap
    v0, v = v, v0  # swap
    
    advect(N, 1, u, u0, u0, v0, dt)
    advect(N, 2, v, v0, u0, v0, dt)
    project(N, u, v, u0, v0)
