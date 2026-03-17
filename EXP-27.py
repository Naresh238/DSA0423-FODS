import numpy as np
import scipy.stats as stats

data = np.random.randint(100,500,100)

mean = np.mean(data)
sem = stats.sem(data)

ci = stats.t.interval(0.95, len(data)-1, loc=mean, scale=sem)

print("Mean:", mean)
print("95% CI:", ci)
