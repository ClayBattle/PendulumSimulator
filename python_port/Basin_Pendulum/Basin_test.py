import numpy as np
import matplotlib.pyplot as plt
import Pen_stable_check

# Assuming the is_stable function from the previous example is defined

#warning, this test runs exceedingly slow

n = 200 #originally 200
theta_range = np.linspace(-np.pi, np.pi, n)
omega_range = np.linspace(-20, 20, n)

# Initialize results array
results = np.zeros((n, n), dtype=int)

print("Evaluating stable points...")
# Evaluate stability for each combination of initial angle and angular velocity
for i, theta_0 in enumerate(theta_range):
    for j, omega_0 in enumerate(omega_range):
        results[i, j] = Pen_stable_check.is_stable(theta_0, omega_0)
print("stable points evaluated")

# Find the stable (1) points
stable_points = np.argwhere(results == 1)

# Convert index to angle and angular velocity
stable_points_xy = [(theta_range[i], omega_range[j]) for (i, j) in stable_points]

# Unzip stable points for plotting
stable_theta, stable_omega = zip(*stable_points_xy)

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(stable_theta, stable_omega, marker='o', color='green', s=2, label="Stable")
plt.xlabel("Initial Angle (rad)")
plt.ylabel("Initial Angular Velocity (rad/s)")
plt.xlim(-np.pi, np.pi)
plt.ylim(-20, 20)
plt.title("Stable Points of the Pendulum")
plt.legend()
plt.grid()
plt.show()
