import numpy as np

student_scores = np.array([
[80,70,90,85],
[75,85,88,92],
[90,80,85,87],
[70,75,80,78]
])

avg_scores = np.mean(student_scores, axis=0)

subjects = ['Math','Science','English','History']

print("Average Scores:", avg_scores)

highest = subjects[np.argmax(avg_scores)]
print("Highest Average Subject:", highest)
