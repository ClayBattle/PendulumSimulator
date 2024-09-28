import math

# Function to calculate the total energy
def pendulum_energy(θ, ω, m, L, g):
    V = 0.5 * m * (L * ω)^2 + m * g * L * (1 - math.cos(θ))
    return V
