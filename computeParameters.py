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
else:
	directory = 'data/mLarge/'
print('Loading data ...')
nMovies, nUsers, Links, Movies = getData.loadData(directory)
print('Data loaded')

n = 100
lamda = 0
alpha = 0.01
iterations = 1
step_size = 100000
X = np.random.rand(nMovies, n)
Theta = np.random.rand(nUsers, n)

# Minimizing Cost
start = timer()
X, Theta, Cost = costFunction.minimize(X, Theta, nMovies, nUsers, n, alpha, lamda, iterations, step_size, directory+'ratings.csv')
end = timer()
print(end - start)

# Just printing some data
it = np.array(range(step_size, step_size*(Cost.shape[0] + 1), step_size))
print(Cost)
plt.plot(it, Cost)
plt.show()