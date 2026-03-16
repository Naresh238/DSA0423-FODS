import pandas as pd

data = {'product':['A','B','C','A','B','A'],'quantity':[5,3,6,4,2,7]}

df = pd.DataFrame(data)

top = df.groupby('product')['quantity'].sum().sort_values(ascending=False).head(5)

print(top)
