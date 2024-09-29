#Pendulum energy function without initial torque  
import math
import matplotlib.pyplot as plt
import pendulum_energy
import numpy as np

# Parameters
m = 1
L = 9.8
g = 9.8


n = 100
θ_range = np.linspace(-3 * math.pi, 3 * math.pi, n)  # Using linspace for floating-point values
ω_range = np.linspace(-10, 10, n)

# Creating a grid of theta and omega values
θ_grid, ω_grid = np.meshgrid(θ_range, ω_range)

# Vectorized calculation of pendulum energy over the entire grid
pendulumCalc = np.vectorize(pendulum_energy.pendulum_energy)
V_values = pendulumCalc(θ_grid, ω_grid, m, L, g)


# 3D Plotting
# adjusted_angle = sol[1, :] .- θ₁

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot surface
surf = ax.plot_surface(ω_range, θ_range, V_values, cmap='viridis')

# Adding labels and title
ax.set_title("Pendulum Energy")
ax.set_xlabel("ω (rad/s)")
ax.set_ylabel("θ (rad)")
ax.set_zlabel("Energy (Joules)")

# Show color bar
fig.colorbar(surf)

# Display plot
plt.show()
