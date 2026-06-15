# Pure Python 1D CFD Solvers

This repository contains educational 1D Computational Fluid Dynamics (CFD) solvers built from scratch in Python. It demonstrates the implementation of finite difference discretization schemes to solve partial differential equations governing fluid transport without relying on external commercial software wrappers.

## 📐 Governing Mathematics

### 1. Linear Convection Equation
The standard linear wave equation represents the pure advection of a scalar quantity (like velocity or temperature) through a continuous fluid medium at a constant wave speed $c$:

$$\frac{\partial u}{\partial t} + c \frac{\partial u}{\partial x} = 0$$

### 2. Non-Linear Convection (Inviscid Burgers' Equation)
A foundational non-linear transport equation where the advection speed is directly coupled with the local fluid velocity field $u$, leading to wave steepening and shock formation:

$$\frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} = 0$$

---

## 💻 Numerical Discretization Scheme

The spatial derivatives are discretized using a first-order **Forward-Time/Backward-Space (Upwind)** scheme to maintain numerical stability along the characteristic direction of flow transport ($c > 0$):

$$u_i^{n+1} = u_i^n - c \frac{\Delta t}{\Delta x} (u_i^n - u_{i-1}^n)$$

For the non-linear configuration, the local wave propagation speed updates dynamically across the spatial coordinates:

$$u_i^{n+1} = u_i^n - u_i^n \frac{\Delta t}{\Delta x} (u_i^n - u_{i-1}^n)$$

---

## 🛠️ Code Architecture

The solver framework utilizes a modular, object-oriented design structure:
* `convection_solver.py`: Holds the mathematical solver class logic, space grid initializations, and state boundary updates.
* `main.py`: The execution orchestrator that configures simulation boundaries, runs time-marching steps, and plots velocity profile outputs.

## 📊 Expected Output Visualization
Running `main.py` solves the transport equations from an initial square wave "hat function" condition and exports an engineering verification plot named `convection_results.png`. The visualization clearly showcases numerical diffusion inherent to upwind finite difference grids alongside the non-linear wave steepening characteristic of Burgers' formulation.
