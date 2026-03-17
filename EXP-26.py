import numpy as np
import matplotlib.pyplot as plt

temp = np.array([25,30,35,40,28])
rain = np.array([100,80,60,40,90])

corr = np.corrcoef(temp,rain)[0,1]

print("Correlation:", corr)

plt.scatter(temp,rain)
plt.xlabel("Temperature")
plt.ylabel("Rainfall")
plt.show()
