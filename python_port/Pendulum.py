import math

# modifies its arguments in original julia code
def Pendulum(du, u, p, t):
    a, T , g, L = p
    du[1] = u[2]                  # u[1] is θ
    du[2] = -a*u[2] + T - (g/L)*math.sin(u[1])    #u[2] is ω
