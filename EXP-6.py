import numpy as np

time = np.array([0,1,2,3,4])
position = np.array([0,5,15,30,50])

avg_velocity = (position[-1] - position[0])/(time[-1] - time[0])

print("Average Velocity:", avg_velocity)
