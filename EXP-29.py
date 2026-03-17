import pandas as pd
import scipy.stats as stats

df = pd.DataFrame({'rating':[4,5,3,4,5,4,3,5]})

mean = df['rating'].mean()
sem = stats.sem(df['rating'])

ci = stats.t.interval(0.95, len(df)-1, loc=mean, scale=sem)

print("Average Rating:", mean)
print("Confidence Interval:", ci)
