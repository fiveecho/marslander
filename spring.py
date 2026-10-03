# uncomment the next line if running in a notebook
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

# mass, spring constant, initial position and velocity
m = 1
k = 1
x = 0
v = 1

# simulation time, timestep and time
t_max = 100
dt = 2
t_array = np.arange(0, t_max, dt)

# Verlet integrator approximately stable until dt = 2

# initialise empty lists to record trajectories
x_list = []
x_list_verlet = []
v_list = []
v_list_verlet = []

# Euler integration
for t in t_array:

    # append current state to trajectories
    x_list.append(x)
    v_list.append(v)

    if len(x_list) < 3:
        x_list_verlet.append(x)
        v_list_verlet.append(v)
    else:
        x_verlet = 2*x_list_verlet[-1] - x_list_verlet[-2] + (dt**2)*(-k * x_list_verlet[-1] / m) 
        x_list_verlet.append(x_verlet)
        v_verlet = (1/dt) * (x_list_verlet[-1] - x_list_verlet[-2])
        v_list_verlet.append(v_verlet)

    # calculate new position and velocity
    a = -k * x / m
    x = x + dt * v
    v = v + dt * a

# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
x_array = np.array(x_list)
v_array = np.array(v_list)

# for verlet integral
x_ver_array = np.array(x_list_verlet)
v_ver_array = np.array(v_list_verlet)

# plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
# plt.plot(t_array, x_array, label='x (m)')
# plt.plot(t_array, v_array, label='v (m/s)')
plt.plot(t_array, x_ver_array, label='x verlet (m)')
plt.plot(t_array, v_ver_array, label='v verlet (m/s)')
plt.legend()
plt.show()
