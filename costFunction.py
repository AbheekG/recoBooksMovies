import numpy as np
import math

def minimize(X_init, Theta_init, alpha, lamda, iterations, step_size, file):
	X = X_init.copy()
	Theta = Theta_init.copy()
	nMovies = X.shape[0]
	nUsers = Theta.shape[0]
	n = X.shape[1]
	nX = np.ones(nMovies)
	nTheta = np.ones(nUsers)
	Cost = []
	k = 0
	J = 0
	for ite in range(iterations):
		with open(file) as f:
			for line in f:
				if(line[0] > '9' or line[0] < '0'): continue

				i = line.index(',')
				j = line.index(',', i+1)
				
				a = int(line[:i])
				b = int(line[i+1:j])
				c = float(line[j+1:])
				#print(a,b,c)

				d = X[b,:].dot(Theta[a,:])
				#print(X[b,:], Theta[a,:])
				#print(d)
				d = d - c
				J = J + d**2 / (2 * step_size)

				if(math.isnan(J)):
					print(a,b,c)
					print(d,J,k)

				X[b,:] = (1 - lamda*alpha / nX[b]**0.5) * X[b,:] - (alpha / nX[b]**0.5) * d * Theta[a,:]
				Theta[a,:] = (1 - lamda*alpha / nTheta[a]**0.5) * Theta[a,:] - (alpha / nTheta[a]**0.5)* d * X[b,:]
				#print(J)
				nTheta[a] = nTheta[a] + 0.1
				nX[b] = nX[b] + 0.1

				k = k + 1
				if(k%step_size == 0):
					#print(k, J)
					Cost = Cost + [J]
					J = 0

	return X, Theta, np.array(Cost)

def cvCost(X, Theta, step_size, file):
	Cost = []
	J = 0
	k = 0
	with open(file) as f:
		for line in f:
			if(line[0] > '9' or line[0] < '0'): continue

			i = line.index(',')
			j = line.index(',', i+1)
			
			a = int(line[:i])
			b = int(line[i+1:j])
			c = float(line[j+1:])

			d = X[b,:].dot(Theta[a,:])
			J = J + (d - c)**2 / (2 * step_size)
			
			k = k + 1
			if(k%step_size == 0):
				#print(k, J)
				Cost = Cost + [J]
				J = 0

	return np.array(Cost)