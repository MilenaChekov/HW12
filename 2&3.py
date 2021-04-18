from scipy import stats
import numpy as np

X = [3, 4, 5, -6, 7, -8, 9, 10, 10]
Y = [-3, -4, -5, 6, -7, 8, -9, -10, -10]
Z = [3.2, 4.2, 5.2, -5.8, 7.2, -7.8, 9.2, 10.2, 10.2]

print(np.var(np.subtract(X, Y)))
print(stats.ttest_ind(X, Y))

print(stats.ttest_rel(X, Y))

print(stats.ttest_ind(X, Z))

print(stats.ttest_rel(X, Z))