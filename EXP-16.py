from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np

X = np.array([[25,120],[30,130],[45,150],[50,160]])
y = ['Good','Good','Bad','Bad']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train,y_train)

print(model.predict(X_test))
