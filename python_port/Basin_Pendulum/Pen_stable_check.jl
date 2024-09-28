using DifferentialEquations, Plots, Statistics

function is_stable(θ₀, ω₀)
    function pendulum!(du, u, p, t)
        a, T , K = p
        du[1] = u[2]                  # u[1] is θ
        du[2] = -a*u[2] + T - K*sin(u[1])    #u[2] is ω
    end

    a = 0.1
    K = 1
    T = 0.5

    u₀ = [θ₀, ω₀] # initial state
    tspan = (0.0, 100.0) # time span for simulation
    p = [a, T , K] # parameters

    prob = ODEProblem(pendulum!, u₀, tspan, p)
    sol = solve(prob, Tsit5(), reltol=1e-5, abstol=1e-5)

    θ₁ = asin(T / K)
    adjusted_angle = sol[1, :] .- θ₁

    last_angle = adjusted_angle[end-10:end-1] - adjusted_angle[end-9:end]
    last_speed = sol[2, end-10:end-1]  - sol[2, end-9:end]
    sq_last = sum(last_angle.^2) + sum(last_speed.^2)

    return sq_last < 1
end
