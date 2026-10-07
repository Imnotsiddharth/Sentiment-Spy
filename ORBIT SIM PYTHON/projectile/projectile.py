import numpy as np
import matplotlib.pyplot as plt
import math

print("PROJECTILE SIMULATION")
angle_input = float(input("Enter the launch angle (in degrees):"))
speed_input = float(input("Enter the speed of the launch (in m/s):"))

angle_input_radians = np.radians(angle_input)
g = 9.8

vox = math.cos(angle_input_radians) * speed_input
voy = math.sin(angle_input_radians) * speed_input
T = (2*voy)/g
H= (voy**2)/(2*g)
R = vox * T


time_array = np.linspace (0,T,2000)
t = time_array
x = vox * t
y = (voy * t) - (0.5 * g * t**2)

print(f"Time of flight: {T:.2f} s")
print(f"Range: {R:.2f} m")
print(f"Height: {H:.2f} m")

print(H)
print(np.max(y))
print(R)
print(x[-1])

print(f"Height difference: {H - np.max(y):.6f} m")
print(f"Range difference:  {R - x[-1]:.6f} m")

"""plt.plot(x,y)
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.title("Projectile Simulation")
plt.show()"""