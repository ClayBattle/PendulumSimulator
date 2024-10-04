import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define the pendulum system
def pendulum(t, u, a, T, K):
    theta, omega = u
    dtheta_dt = omega                  # u[0] is θ
    domega_dt = -a*omega + T - K*np.sin(theta)    # u[1] is ω
    return [dtheta_dt, domega_dt]

# Initial conditions
theta_0 = 0  # initial angle in radians
omega_0 = -20  # initial angular velocity in radians/s
u0 = [theta_0, omega_0] # initial state

# Parameters
a = 0.1
K = 1
T = 0.5

# Time span for the simulation
t_span = (0, 100)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

# Solve the system of ODEs
sol = solve_ivp(pendulum, t_span, u0, args=(a, T, K), t_eval=t_eval, rtol=1e-6, atol=1e-6)

# Extract the solution
theta = sol.y[0]
omega = sol.y[1]

# Adjust the angle by subtracting θ₁
theta_1 = np.arcsin(T / K)
adjusted_angle = theta - theta_1

# Calculate the sq_last value
last_angle = adjusted_angle[-10:-1] - adjusted_angle[-9:]
last_speed = omega[-10:-1] - omega[-9:]
sq_last = np.sum(last_angle**2) + np.sum(last_speed**2)

print(f"sq_last = {sq_last}")

# Plot the results
plt.figure(figsize=(10, 8))

# Plot adjusted angle
plt.subplot(2, 1, 1)
plt.plot(sol.t, adjusted_angle, label=r'$\theta - \theta_1$', color='b')
plt.xlabel("Time (s)")
plt.ylabel("Angle (rad)")
plt.legend()

# Plot angular velocity
plt.subplot(2, 1, 2)
plt.plot(sol.t, omega, label="Angular Velocity", color='r')
plt.xlabel("Time (s)")
plt.ylabel("Angular Velocity (rad/s)")
plt.legend()

plt.show()
