import numpy as np
from scipy.integrate import solve_ivp

def pendulum(t, u, a, T, K):
    # u[0] is θ, u[1] is ω
    du = np.zeros_like(u)
    du[0] = u[1]
    du[1] = -a * u[1] + T - K * np.sin(u[0])
    return du

def is_stable(theta_0, omega_0):
    a = 0.1
    K = 1
    T = 0.5

    u_0 = [theta_0, omega_0]  # initial state
    t_span = (0.0, 100.0)  # time span for simulation
    t_eval = np.linspace(t_span[0], t_span[1], 1000)  # evaluate at 1000 points for resolution
    params = (a, T, K)  # parameters

    # Solve ODE
    sol = solve_ivp(pendulum, t_span, u_0, args=params, t_eval=t_eval, rtol=1e-5, atol=1e-5)

    theta_1 = np.arcsin(T / K)
    adjusted_angle = sol.y[0] - theta_1

    last_angle = adjusted_angle[-10:-1] - adjusted_angle[-9:]
    last_speed = sol.y[1][-10:-1] - sol.y[1][-9:]
    sq_last = np.sum(last_angle**2) + np.sum(last_speed**2)

    return sq_last < 1

# # Example usage
# stable = is_stable(np.pi/4, 0)  # Example initial conditions
# print("Is stable:", stable)
