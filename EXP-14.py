import pandas as pd
import matplotlib.pyplot as plt
import string

data = pd.read_csv("data.csv")

text = " ".join(data['feedback']).lower()

for p in string.punctuation:
    text = text.replace(p,"")

words = text.split()

freq = {}

for w in words:
    freq[w] = freq.get(w,0)+1

top = sorted(freq.items(), key=lambda x:x[1], reverse=True)[:5]

words = [i[0] for i in top]
counts = [i[1] for i in top]

plt.bar(words,counts)
plt.show()
