import numpy as np
import matplotlib.pyplot as plt

# Load the results matrix from the CSV file
input_filename = "n_2000.csv"
results = np.loadtxt(input_filename, delimiter=',', dtype=int)

# Generate the plot
n = results.shape[0]
theta_range = np.linspace(-np.pi, np.pi, n)
omega_range = np.linspace(-20, 20, n)


# Find the stable (1) points
stable_points = np.argwhere(results == 1)

# Convert index to angle and angular velocity
stable_points_xy = [(theta_range[i], omega_range[j]) for (i, j) in stable_points]

# Unzip stable points for plotting
stable_theta, stable_omega = zip(*stable_points_xy)

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(stable_theta, stable_omega, marker='o', color='green', s=1, label="Stable")
plt.xlabel("Angle Φ-Φ₁")
plt.ylabel("Frequency ω")
plt.xlim(-np.pi, np.pi)
plt.ylim(-20, 20)
plt.title("Stable Points Scatter Plot")
plt.legend()
plt.grid()
plt.show()
