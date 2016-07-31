from timeit import default_timer as timer
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import getData
import costFunction

# Initialize
data_type = 'float64'
isSmall = bool(int(input('Enter 1 for small: ')))
print(isSmall)
if(isSmall):
	directory = 'data/mSmall/'
	iterations = 10
	step_size = 1000
else:
	directory = 'data/mLarge/'
	iterations = 1
	step_size = 50000
print('Loading data ...')
nMovies, nUsers, Links, Movies, Means = getData.loadData(directory, data_type)
print('Data loaded')

n = 500
lamda = 0
Lamdas = np.array([0, 0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30, 100, 300, 1000])
#Lamdas = np.array([5, 10, 20, 40, 70, 130])
alpha = 0.001
X_init = np.random.rand(nMovies, n)
Theta_init = np.random.rand(nUsers, n)

# Minimizing Cost, calculating regularization automatically
start = timer()
mini = 10**100
for i in range(Lamdas.shape[0]):
	X, Theta, Cost_train = costFunction.minimize(X_init, Theta_init, alpha, Lamdas[i], iterations, step_size, directory+'ratings_train.csv')
	Cost_cv = costFunction.cvCost(X, Theta, step_size, directory+'ratings_cv.csv')
	J_train = np.sum(Cost_train[-Cost_cv.shape[0]:]) / Cost_cv.shape[0]
	J_cv = np.sum(Cost_cv) / Cost_cv.shape[0]
	print('Lamda = %f, Cost. Train = %f, CV = %f' %(Lamdas[i], J_train, J_cv))
	if(J_cv < mini):
		mini = J_cv
		lamda = Lamdas[i]

print('The best lamda found = ', lamda)
X, Theta, Cost_train = costFunction.minimize(X_init, Theta_init, alpha, lamda, iterations, step_size, directory+'ratings_train.csv')
Cost_cv = costFunction.cvCost(X, Theta, step_size, directory+'ratings_cv.csv')
Cost_test = costFunction.cvCost(X, Theta, step_size, directory+'ratings_test.csv')
J_train = np.sum(Cost_train[-Cost_cv.shape[0]:]) / Cost_cv.shape[0]
J_cv = np.sum(Cost_cv) / Cost_cv.shape[0]
J_test = np.sum(Cost_test) / Cost_test.shape[0]
print('Cost. Train = %f, CV = %f, Test = %f' %(J_train, J_cv, J_test))
end = timer()
print(end - start)

# Just printing some data
it = np.array(range(step_size, step_size*(Cost_train.shape[0] + 1), step_size))
#print(Cost)
plt.plot(it[-Cost_cv.shape[0]:], Cost_train[-Cost_cv.shape[0]:], 'b')
plt.plot(it[-Cost_cv.shape[0]:], Cost_cv, 'g')
plt.plot(it[-Cost_test.shape[0]:], Cost_test, 'r')
plt.show()

# User movie recommendation check
Y1 = X.dot(Theta[0,:].transpose())
Y1 = Y1 + Means
for i in range(Y1.shape[0]):
	if(Y1[i] > 4.5):
		print(i, Y1[i], Movies.loc[i])

# Saving some data, maybe be helpful later
np.save(directory+'Theta.npy', Theta)
np.save(directory+'X.npy', X)