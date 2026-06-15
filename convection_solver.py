"""
Module: convection_solver.py
Author: Sai Teja Dingari
Description: 1D Linear and Non-Linear Convection solver using Finite Difference 
             methods with a Forward-Time/Backward-Space (Upwind) discretization scheme.
"""

import numpy as np

class ConvectionSolver1D:
    def __init__(self, nx=81, domain_length=2.0, c=1.0):
        """
        nx: Number of grid points
        domain_length: Physical length of the 1D domain (meters)
        c: Constant wave speed (for linear convection)
        """
        self.nx = nx
        self.dx = domain_length / (nx - 1)
        self.c = c
        
        # Initialize grid coordinates
        self.x = np.linspace(0, domain_length, nx)
        
        # Initialize velocity field 'u'
        self.u = np.ones(nx)
        
    def set_hat_initial_condition(self):
        """
        Sets a classic 'Hat function' initial velocity profile:
        u = 2 between x = 0.5 and x = 1.0; u = 1 everywhere else.
        """
        self.u = np.ones(self.nx)
        self.u[int(0.5 / self.dx):int(1.0 / self.dx + 1)] = 2.0
        return self.u

    def solve_linear(self, steps=25, dt=0.027):
        """
        Solves du/dt + c * du/dx = 0 using a first-order Upwind scheme.
        """
        u_current = self.u.copy()
        
        for _ in range(steps):
            u_next = u_current.copy()
            # Loop through interior grid points (Backward Space scheme)
            for i in range(1, self.nx):
                u_next[i] = u_current[i] - self.c * (dt / self.dx) * (u_current[i] - u_current[i - 1])
            u_current = u_next.copy()
            
        self.u = u_current
        return self.u

    def solve_nonlinear(self, steps=25, dt=0.02):
        """
        Solves non-linear convection (Inviscid Burgers' Equation):
        du/dt + u * du/dx = 0 where the wave speed is the fluid velocity itself.
        """
        u_current = self.u.copy()
        
        for _ in range(steps):
            u_next = u_current.copy()
            for i in range(1, self.nx):
                # The wave speed 'c' is replaced by the local fluid velocity u_current[i]
                u_next[i] = u_current[i] - u_current[i] * (dt / self.dx) * (u_current[i] - u_current[i - 1])
            u_current = u_next.copy()
            
        self.u = u_current
        return self.u
