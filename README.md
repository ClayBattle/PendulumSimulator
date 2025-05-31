# PendulumSimulator Background
For Complex Systems Research with Professor Chiu. This was code given to me in the start of my research to familiarize myself with the  general flow of mathematical python and related python packages. Moving forward, it could potentially be useful when modeling stability of some generator systems. 

# Repo Structure
The julia Directory contains the original Julia code sent to me. If my memory serves me correctly, most of it is functional. However, some scripts may require some modifications to work as intended.

The python_port Directory contains the Julia code ported to Python, cross referenced with the original code's output/generations to ensure correctness. The files are as follows:
* Pendulum_1.py: Simulates and plots the motion of a damped driven pendulum using numerical integration.
* Pendulum_3_phase portrait_energy.jl (Julia file) Generates a phase portrait and energy surface for a pendulum system. I did not finish translating this to python as priorities changed.
* pendulum_energy_graph.py: Provides a user interface to generate and visualize pendulum energy surfaces, with or without torque. Params are configurable.
* pendulum_energy_no_torque.py: Same as pendulum_energy_graph.py but without torque. Params are configurable.
* pendulum_energy_torque.py: Same as pendulum_energy_graph.py but with torque. Params are configurable.
* pendulum_energy.py: Contains functions to compute the total energy of a pendulum given its state and parameters.
* Pendulum.py: Defines the pendulum system's equations of motion.

Within the python_port directory is the Basin_Pendulum directory, which contains partially finished scripts and modules for analyzing the stability and basins of attraction of pendulum systems. Note that generating the stable regions for these systems can take a long time. The files are organized as follows:
* Pendulum_1.py: Same as previous Pendulum_1.py
* Pen_stable_check.py: Contains functions to numerically check if a given pendulum initial condition is stable (i.e.  small perturbations around that state won’t cause the motion to diverge uncontrollably).
* Basin_test.py: Brute-force script to evaluate and plot the stability of a grid of pendulum initial conditions (slow, for testing).
* Basin_parallel.py/Basin_parallel_attempt_2.py: my attempt to speed up Basin_test with parallelization. Unfortunately, the code is still very slow, and may not work.
* Plot_csv.py: Loads a CSV file of stability results (from Basin_test, or a Basin_parallel run) and generates a scatter plot of stable points in phase space. This visualizes the stability of the system.



