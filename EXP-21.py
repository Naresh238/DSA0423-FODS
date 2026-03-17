from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Dataset
weight = [150, 170, 140, 130, 160]
color = ['red','orange','red','yellow','orange']
texture = ['smooth','rough','smooth','smooth','rough']
type_fruit = ['apple','orange','apple','banana','orange']

# Encode categorical data
le_color = LabelEncoder()
le_texture = LabelEncoder()
le_type = LabelEncoder()

color_enc = le_color.fit_transform(color)
texture_enc = le_texture.fit_transform(texture)
y = le_type.fit_transform(type_fruit)

# Features
X = np.column_stack((weight, color_enc, texture_enc))

# Model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# New fruit prediction
new = [[155, le_color.transform(['red'])[0], le_texture.transform(['smooth'])[0]]]
pred = model.predict(new)

print("Predicted Fruit:", le_type.inverse_transform(pred))
