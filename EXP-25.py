import numpy as np

data = np.array([10,20,30,40,50])

mean = np.mean(data)
var = np.var(data)

sample = np.random.choice(data, size=3)

print("Mean:", mean)
print("Variance:", var)
print("Sample:", sample)
