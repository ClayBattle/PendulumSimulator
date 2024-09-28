using DifferentialEquations, Plots

function pendulum!(du, u, p, t)
    a, T , K = p
    du[1] = u[2]                  # u[1] is θ
    du[2] = -a*u[2] + T - K*sin(u[1])    #u[2] is ω
end

n = 20      # number of lines
θ_range = range(-6*pi, 6*pi, length=n)
ω_range = range(-10, 10, length=n)

a = 0.1
K = 1
T = 0.5

tspan = (0.0, 100.0) # time span for simulation
p = [a, T , K] # parameters

θ₁ = asin(T / K)

# Initialize the plot
plot_pendulum = plot(legend=false, xlims=(-3*pi, 3*pi), ylims=(-10, 10), xlabel="θ - θ₁", ylabel="ω", title="Pendulum Phase Portrait")

# Loop over the grid of initial conditions and plot the trajectories
for θ₀ in θ_range
    for ω₀ in ω_range
        local u₀ = [θ₀, ω₀] # initial state
        local prob = ODEProblem(pendulum!, u₀, tspan, p)
        local sol = solve(prob, Tsit5(), reltol=1e-6, abstol=1e-6)
        local adjusted_angle = sol[1, :] .- θ₁
        plot!(plot_pendulum, adjusted_angle, sol[2, :], linewidth=1)
    end
end

# Display the phase portrait
display(plot_pendulum)
