print("The height of the dam is 170 meters and the flow from the top to the bottom of the dam is 1.30 x 10^3 m^3/s.")
efficiency = 0.9
flow = 1.30 * 10**3
height = 170
g = 9.80
mass = 1000
potential_energy = mass * g * height

electrical_energy = potential_energy * efficiency
MegaWatts = electrical_energy * 10**-6
print("The dam produced", MegaWatts, "megawatts of electricity")
