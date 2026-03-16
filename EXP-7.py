import numpy as np

house_data = np.array([
[3,1200,200000],
[5,2000,500000],
[4,1500,300000],
[6,2500,700000]
])

bedrooms = house_data[:,0]
prices = house_data[:,2]

avg_price = np.mean(prices[bedrooms>4])

print("Average Price:", avg_price)
