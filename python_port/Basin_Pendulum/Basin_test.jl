using Plots

include("Pen_stable_check.jl")

n = 200
θ_range = range(-pi, pi, length=n)
ω_range = range(-20, 20, length=n)

results = zeros(Int, n, n)

for (i, θ₀) in enumerate(θ_range)
    for (j, ω₀) in enumerate(ω_range)
        results[i, j] = is_stable(θ₀, ω₀)
    end
end

# Find the stable (1) points
stable_points = [(i, j) for i in 1:n, j in 1:n if results[i, j] == 1]

# Convert index to angle and angular velocity
stable_points_xy = [(θ_range[i], ω_range[j]) for (i, j) in stable_points]


display(scatter(stable_points_xy, markershape=:circle, markercolor=:green, markerstrokewidth=0, 
label="Stable", xlabel="Initial Angle (rad)", ylabel="Initial Angular Velocity (rad/s)", 
xlims=(-pi, pi), ylims=(-20, 20), markersize=2))
