import pandas as pd
import matplotlib.pyplot as plt

data = {
'shoe_size':[7,8,9,7,8,9,10],
'quantity':[10,15,20,5,10,15,8]
}

df = pd.DataFrame(data)

freq = df.groupby('shoe_size')['quantity'].sum()

print(freq)

plt.bar(freq.index, freq.values)
plt.xlabel("Shoe Size")
plt.ylabel("Frequency")
plt.title("Shoe Size Distribution")
plt.show()
