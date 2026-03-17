from scipy import stats
import numpy as np

control = np.array([50,55,60])
treatment = np.array([65,70,75])

t,p = stats.ttest_ind(control,treatment)

print("P-value:",p)
