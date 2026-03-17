import pandas as pd

df = pd.read_csv("players.csv")

print(df.nlargest(5,'goals'))
print(df.nlargest(5,'salary'))

avg_age = df['age'].mean()

print(df[df['age']>avg_age])
