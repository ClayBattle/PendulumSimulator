import python_port.Pendulum_energy_torque as Pendulum_energy_torque
import Pendulum_energy_no_torque

def main():
    cont = "y"
    while(cont == "y"):
        print("Input values for the mass of pendulum bob, length of the pendulum rod, and grid sample size")
        mass = input("Enter the mass of the pendulum bob (in kg) [default: 1]: ")
        length = input("Enter the length of the pendulum rod (in meters) [default: 9.8]: ")
        grid_size = input("Enter the grid sample size (an integer) [default: 100]: ")
        has_torque = input("Include Torque (y/n)? [Default: y]: ")
        
        # Assign default values if inputs are empty
        mass = float(mass) if mass else 1
        length = float(length) if length else 9.8
        grid_size = int(grid_size) if grid_size else 100
        if(has_torque.strip().lower() == "n"):
            has_torque == False
        else:
            has_torque == True


        if(has_torque):
            torque_amount = input("Enter the torque [Default: .5]: ")
            torque = float(torque_amount) if torque_amount else .5

            Pendulum_energy_torque.generate_pendulum_energy_t(mass, length, grid_size, torque)
        else:
            Pendulum_energy_no_torque.generate_pendulum_energy_no_t(mass, length, grid_size)
        
        cont = input("\nContinue? y/n: ")
        if(cont.strip().lower() != "y"):
            break



if __name__ == "__main__":
    main()
    