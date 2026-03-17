products = ['A','B','A','C','B','A','D']

freq = {}

for p in products:
    freq[p] = freq.get(p,0)+1

print("Frequency:", freq)

most = max(freq, key=freq.get)
print("Most Popular Product:", most)
