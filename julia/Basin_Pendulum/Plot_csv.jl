using Plots
using DelimitedFiles

# Load the results matrix from the CSV file
input_filename = "n_2000.csv"
results = readdlm(input_filename, ',', Int)

# Generate the plot1
n = size(results, 1)
θ_range = range(-pi, pi, length=n)
ω_range = range(-20, 20, length=n)


scatter(results, markershape=:circle, markercolor=:green, markerstrokewidth=0, 
label="Stable", xlabel="Angle Φ-Φ₁", ylabel="Frequency ω", 
xlims=(-pi, pi), ylims=(-20, 20), markersize=1)