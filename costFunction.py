import numpy as np

def minimize(X, Theta, nMovies, nUsers, n, alpha, lamda, iterations, step_size, file):
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
				J = J + (d - c)**2 / step_size
				d = alpha * (d - c)
				d = d / (nX[b]**(0.25) * nTheta[a]**(0.25))
				X[b,:] = (1 - lamda)*X[b,:] - d*Theta[a,:]
				Theta[a,:] = (1 - lamda)*Theta[a,:] - d*X[b,:]
				#print(J)
				nTheta[a] = nTheta[a] + 1
				nX[b] = nX[b] + 1

				k = k + 1
				if(k%step_size == 0):
					print(k, J/step_size)
					Cost = Cost + [J/step_size]
					J = 0

	return X, Theta, np.array(Cost)