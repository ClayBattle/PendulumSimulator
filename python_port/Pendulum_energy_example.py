#Pendulum energy function without initial torque  
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pendulum_energy

# Parameters
m = 1
L = 9.8
g = 9.8

# Number of points and ranges
n = 100
θ_range = range(-3*math.pi, stop=3*math.pi, step=n)
ω_range = range(-10, stop=10, step=n)

# Creating a grid of theta and omega values and calculating energy. 
#TODO optimize with numpy
V_values = []
for θ in θ_range:
    for ω in ω_range:
        V_values.append(pendulum_energy(θ, ω, m, L, g))

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
