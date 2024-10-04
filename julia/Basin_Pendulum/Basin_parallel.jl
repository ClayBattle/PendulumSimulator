using Plots
using DelimitedFiles

include("Pen_stable_check.jl")

n = 2000
θ_range = range(-pi, pi, length=n)
ω_range = range(-20, 20, length=n)

results = zeros(Int, n, n)

K = 1
T = 0.5
θ₁ = asin(T / K)

@time begin
    Threads.@threads for i in 1:n
        for (j, ω₀) in enumerate(ω_range)
            results[i, j] = is_stable(θ_range[i]+θ₁, ω₀)
        end
    end
end

# Find the stable (1) points
stable_points = [(i, j) for i in 1:n, j in 1:n if results[i, j] == 1]

# Convert index to angle and angular velocity
stable_points_xy = [(θ_range[i], ω_range[j]) for (i, j) in stable_points]

display(scatter(stable_points_xy, markershape=:circle, markercolor=:green, markerstrokewidth=0, 
label="Stable", xlabel="Angle Φ-Φ₁", ylabel="Frequency ω", 
xlims=(-pi, pi), ylims=(-20, 20), size=(800, 800), markersize=1))
readline()
# Save the results matrix to a CSV file
#output_filename = "n_2000.csv"
#writedlm(output_filename, results, ',')
