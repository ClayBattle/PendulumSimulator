#Pendulum energy function without initial torque  
import math
import matplotlib.pyplot as plt
import pendulum_energy
import numpy as np


def generate_pendulum_energy_no_t(mass, length, grid_size):
    # Parameters
    m = mass # mass of pendulum
    L = length # Length of pendulum rod
    g = 9.8 # Acceleration due to gravity
    n = grid_size # Number of samples / resolution (defines number of points in our ranges)


    θ_range = np.linspace(-3 * math.pi, 3 * math.pi, n)  # Using linspace for floating-point values
    ω_range = np.linspace(-10, 10, n)

    # Create a grid of values for use in vectorized pendulum energy calculation
    θ_grid, ω_grid = np.meshgrid(θ_range, ω_range)

    # Vectorized calculation of pendulum energy over the entire grid
    pendulumCalc = np.vectorize(pendulum_energy.pendulum_energy)
    V_values = pendulumCalc(θ_grid, ω_grid, m, L, g)

    # 3D Plotting
    # adjusted_angle = sol[1, :] .- θ₁

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot surface
    surf = ax.plot_surface(ω_grid, θ_grid, V_values, cmap='viridis')

    # Adding labels and title
    ax.set_title("Pendulum Energy")
    ax.set_xlabel("ω (rad/s)")
    ax.set_ylabel("θ (rad)")
    ax.set_zlabel("Energy (Joules)")

    # Show color bar
    fig.colorbar(surf)
    fig.canvas.manager.set_window_title(f"Pendulum Energy (mass = {m}, length = {L}, grid_size = {n})")
    
    # Display plot
    plt.show()

if __name__ == "__main__":
    cont = "y"
    while(cont == "y"):
        print("Input values for the mass of pendulum bob, length of the pendulum rod, and grid sample size")
        mass = input("Enter the mass of the pendulum bob (in kg) [default: 1]: ")
        length = input("Enter the length of the pendulum rod (in meters) [default: 9.8]: ")
        grid_size = input("Enter the grid sample size (an integer) [default: 100]: ")

        # Assign default values if inputs are empty
        mass = float(mass) if mass else 1
        length = float(length) if length else 9.8
        grid_size = int(grid_size) if grid_size else 100

        # Call the main function with user inputs or defaults
        generate_pendulum_energy_no_t(mass, length, grid_size)
        
        cont = input("\nContinue? y/n: ")
        if(cont.strip().lower() != "y"):
            break