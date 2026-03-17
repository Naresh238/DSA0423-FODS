import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Dataset
data = {
    'income':[20000,50000,80000,30000],
    'credit_score':[600,700,750,650],
    'debt_ratio':[0.5,0.3,0.2,0.4],
    'employment':[2,5,8,3],
    'risk':['High','Low','Low','High']
}

df = pd.DataFrame(data)

# Encode target
df['risk'] = df['risk'].map({'High':1,'Low':0})

# Features & target
X = df[['income','credit_score','debt_ratio','employment']]
y = df['risk']

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# ✅ NEW DATA as DataFrame (fixes warning)
new_data = pd.DataFrame({
    'income':[40000],
    'credit_score':[680],
    'debt_ratio':[0.35],
    'employment':[4]
})

# Prediction
pred = model.predict(new_data)

# Convert result to label
result = "High Risk" if pred[0] == 1 else "Low Risk"

print("Risk Prediction:", result)
