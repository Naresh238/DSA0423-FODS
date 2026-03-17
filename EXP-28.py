import pandas as pd
import matplotlib.pyplot as plt

data = {
'price':[100,200,300,400],
'speed':[120,150,180,200],
'mileage':[15,18,20,22]
}

df = pd.DataFrame(data)

pd.plotting.scatter_matrix(df)
plt.show()
