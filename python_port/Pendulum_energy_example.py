#Pendulum energy function without initial torque  
import math
import matplotlib.pyplot as plt
import pendulum_energy
import numpy as np

# Parameters
m = 1 # mass of pendulum
L = 9.8 # Length of pendulum rod
g = 9.8 # Acceleration due to gravity
n = 100 # Number of samples / resolution (defines number of points in our ranges)


θ_range = np.linspace(-3 * math.pi, 3 * math.pi, n)  # Using linspace for floating-point values
ω_range = np.linspace(-10, 10, n)

# Create a grid of values for use in vectorized pendulum energy calculation
θ_grid, ω_grid = np.meshgrid(θ_range, ω_range)

# Vectorized calculation of pendulum energy over the entire grid
pendulumCalc = np.vectorize(pendulum_energy.pendulum_energy)
V_values = pendulumCalc(θ_grid, ω_grid, m, L, g)

# 3D Plotting
# adjusted_angle = sol[1, :] .- θ₁

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot surface
surf = ax.plot_surface(ω_grid, θ_grid, V_values, cmap='viridis')

# Adding labels and title
ax.set_title("Pendulum Energy")
ax.set_xlabel("ω (rad/s)")
ax.set_ylabel("θ (rad)")
ax.set_zlabel("Energy (Joules)")

# Show color bar
fig.colorbar(surf)

# Display plot
plt.show()
