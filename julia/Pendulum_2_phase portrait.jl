using DifferentialEquations, Plots
plotly()

function Pendulum!(du, u, p, t)
    a, T , g, L = p
    du[1] = u[2]                  # u[1] is θ
    du[2] = -a*u[2] + T - (g/L)*sin(u[1])    #u[2] is ω
end

function pendulum_energy(θ, ω, m, L, g)
    V = 0.1*0.5 * m * (L * ω)^2 + m * g * L * (1 - cos(θ)) - T*θ
    return V
end

n = 10      # number of lines
θ_range = range(-6*pi, 6*pi, length=n)
ω_range = range(-10, 10, length=n)

a = 0.1
g = 9.8
L = 9.8
T = 0.5
m = 1

tspan = (0.0, 100.0) # time span for simulation
p = [a, T , g, L] # parameters

θ₁ = asin(T / (g/L))  # g/L=K
#θ₁ = 0  

# Initialize the plot
plot_pendulum = plot(legend=false, xlims=(-3*pi, 3*pi), ylims=(-10, 10), xlabel="θ - θ₁", ylabel="ω", title="Pendulum Phase Portrait",size=(800, 600))

# Loop over the grid of initial conditions and plot the trajectories
for θ₀ in θ_range
    for ω₀ in ω_range
        local u₀ = [θ₀, ω₀] # initial state
        local prob = ODEProblem(Pendulum!, u₀, tspan, p)
        local sol = solve(prob, Tsit5(), reltol=1e-6, abstol=1e-6)
        local adjusted_angle = sol[1, :] .- θ₁
        local Z = [pendulum_energy(θ, ω, m, L, g) for (θ, ω) in zip(adjusted_angle, sol[2, :])]
        plot!(plot_pendulum, adjusted_angle, sol[2, :], Z, linewidth=1)
    end
end
# Display the phase portrait
display(plot_pendulum)
