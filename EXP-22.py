from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Dataset
data = {
    'age':[25,35,45,20],
    'income':[30000,60000,80000,20000],
    'browsing':[5,10,15,3],
    'device':['mobile','desktop','mobile','tablet'],
    'purchase':['No','Yes','Yes','No']
}

df = pd.DataFrame(data)

# Create encoders
le_device = LabelEncoder()
le_purchase = LabelEncoder()

# Fit and transform
df['device'] = le_device.fit_transform(df['device'])
df['purchase'] = le_purchase.fit_transform(df['purchase'])

# Features and target
X = df[['age','income','browsing','device']]
y = df['purchase']

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# IMPORTANT: Use same encoder for new data
new_device = le_device.transform(['mobile'])[0]

new_data = [[30,50000,8,new_device]]

prediction = model.predict(new_data)

# Convert back to label
result = le_purchase.inverse_transform(prediction)

print("Prediction:", result)
