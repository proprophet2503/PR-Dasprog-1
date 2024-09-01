takeoff_velocity = 278/3.6 # km/hour
distance = 94

time_for_takeoff_velocity = 2*distance/takeoff_velocity
acceleration = takeoff_velocity/time_for_takeoff_velocity

print("The acceleration to takeoff is {} m/s^2".format(acceleration))




