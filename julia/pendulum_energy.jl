# Function to calculate the total energy
function pendulum_energy(θ, ω, m, L, g)
    V = 0.5 * m * (L * ω)^2 + m * g * L * (1 - cos(θ))
    return V
end