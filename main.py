"""
Module: main.py
Author: Sai Teja Dingari
Description: Orchestrates the 1D convection simulations and generates 
             comparative velocity profile plots for verification.
"""

import numpy as np
import matplotlib.pyplot as plt
from convection_solver.py import ConvectionSolver1D

def run_simulations():
    print("Initializing 1D Convection Solver...")
    
    # --- 1. Linear Convection Simulation ---
    # Set up grid configuration
    solver_linear = ConvectionSolver1D(nx=81, domain_length=2.0, c=1.0)
    
    # Capture initial state profile
    u_initial = solver_linear.set_hat_initial_condition().copy()
    
    # Solve forward in time
    u_linear_final = solver_linear.solve_linear(steps=25, dt=0.027)
    
    # --- 2. Non-Linear Convection Simulation ---
    solver_nonlinear = ConvectionSolver1D(nx=81, domain_length=2.0)
    solver_nonlinear.set_hat_initial_condition()
    u_nonlinear_final = solver_nonlinear.solve_nonlinear(steps=25, dt=0.02)
    
    # --- 3. Plotting & Visualization ---
    plt.figure(figsize=(10, 6))
    
    # Plot profiles
    plt.plot(solver_linear.x, u_initial, 'k--', label='Initial Profile (t=0)')
    plt.plot(solver_linear.x, u_linear_final, 'b-', label='Linear Convection (Upwind)')
    plt.plot(solver_nonlinear.x, u_nonlinear_final, 'r-', label='Non-Linear Convection (Burgers)')
    
    # Format graph
    plt.title("1D Convection Velocity Profile Propagation Comparison")
    plt.xlabel("Domain Space (x) [m]")
    plt.ylabel("Velocity Magnitude (u) [m/s]")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    # Save the output visualization plot for the portfolio presentation
    plt.savefig('convection_results.png', dpi=300)
    print("Simulation complete! Results visualization saved as 'convection_results.png'.")

if __name__ == "__main__":
    run_simulations()
