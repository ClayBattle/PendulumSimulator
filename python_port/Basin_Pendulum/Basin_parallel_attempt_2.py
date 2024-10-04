import numpy as np
import matplotlib.pyplot as plt
import Pen_stable_check  # Assuming this is already implemented in Python
from concurrent.futures import ThreadPoolExecutor, as_completed



def check_stability(i, ω0):
    return Pen_stable_check.is_stable(θ_range[i] + θ1, ω0)

# Parameters
n = 200
θ_range = np.linspace(-np.pi, np.pi, n)
ω_range = np.linspace(-20, 20, n)
results = np.zeros((n, n), dtype=int)

K = 1
T = 0.5
θ1 = np.arcsin(T / K)

# Stability check
import time
start_time = time.time()



# Multithreading
# Multithreading without immediate .result() call
import time
start_time = time.time()

tasks = []

with ThreadPoolExecutor() as executor:
    # Submit all tasks to the executor
    for i in range(n):
        for ω0 in ω_range:
            tasks.append(executor.submit(check_stability, i, ω0))
    
    # Collect results as they complete
    for future in as_completed(tasks):
        i, ω0, result = future.result()
        j = np.where(ω_range == ω0)[0][0]  # Find index of ω0 in ω_range
        results[i, j] = result

print(f"Execution time: {time.time() - start_time} seconds")


# Find the stable (1) points
stable_points = np.argwhere(results == 1)

# Convert index to angle and angular velocity
stable_points_xy = [(θ_range[i], ω_range[j]) for (i, j) in stable_points]

# Unzip stable points for plotting
stable_theta, stable_omega = zip(*stable_points_xy)


# # Find stable points (1)
# stable_points = [(i, j) for i in range(n) for j in range(n) if results[i, j] == 1]

# # Convert index to angle and angular velocity
# stable_points_xy = [(θ_range[i], ω_range[j]) for (i, j) in stable_points]

# Plotting the results
stable_points_xy = np.array(stable_points_xy)
plt.scatter(stable_theta, stable_omega, c='green', s=1, label="Stable")

# Formatting the plot
plt.xlabel("Angle Φ - Φ₁")
plt.ylabel("Frequency ω")
plt.xlim(-np.pi, np.pi)
plt.ylim(-20, 20)
plt.title("Stability of Nonlinear System")
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

# Save the results matrix to a CSV file
# output_filename = "n_2000.csv"
