# uncomment the next line if running in a notebook
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

# mass, spring constant, initial position and velocity
m = 6.42*(10**23)
grav = constants.G
r = np.array([3789500,0,0])
v = np.array([0,3362,0])

def a(position):
    accel = (-grav * m * position)/(np.linalg.norm(position)**3)
    return accel

# simulation time, timestep and time
t_max = 10000
dt = 1
t_array = np.arange(0, t_max, dt)

# Verlet integrator approximately stable until dt = 2

# initialise empty lists to record trajectories
r_list = []
r_list_verlet = []
v_list = []
v_list_verlet = []

# Euler integration
for t in t_array:

    # append current state to trajectories
    r_list.append(r)
    v_list.append(v)

    if len(r_list) < 3:
        r_list_verlet.append(r)
        v_list_verlet.append(v)
    else:
        r_verlet = 2*r_list_verlet[-1] - r_list_verlet[-2] + (dt**2)*(a(r_list_verlet[-1])) 
        r_list_verlet.append(r_verlet)
        v_verlet = (1/dt) * (r_list_verlet[-1] - r_list_verlet[-2])
        v_list_verlet.append(v_verlet)

    # calculate new position and velocity
    acc = a(r)
    r = r + dt * v
    v = v + dt * acc

# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
r_array = np.array(r_list)
v_array = np.array(v_list)

# for verlet integral
r_ver_array = np.array(r_list_verlet)
v_ver_array = np.array(v_list_verlet)

altitude = np.array([np.linalg.norm(pos) - 3390*(10**3) for pos in r_array])
altitude_ver = np.array([np.linalg.norm(pos) - 3390*(10**3) for pos in r_ver_array])

# plot the position-time graph
plt.figure(1)
plt.clf()
# plt.xlabel('time (s)')
plt.grid()
plt.plot(r_ver_array[:,0], r_ver_array[:,1])
# plt.plot(t_array, v_array, label='v (m/s)')
# plt.plot(t_array, altitude, label='alt (m)')
# plt.plot(t_array, altitude_ver, label='alt verlet (m)')
# plt.legend()
plt.show()
