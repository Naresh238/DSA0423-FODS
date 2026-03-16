import numpy as np

fuel = np.array([25,30,28,35])

avg = np.mean(fuel)

improvement = ((fuel[3] - fuel[0])/fuel[0])*100

print("Average Efficiency:", avg)
print("Improvement %:", improvement)
