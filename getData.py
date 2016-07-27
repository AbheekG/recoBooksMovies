import numpy as np
import pandas as pd

def loadData(directory):
	Movies = pd.read_csv(directory + 'movies.csv', sep=',', header=None, index_col=0, dtype=str)
	Links = pd.read_csv(directory + 'links.csv', header=None, index_col=0, dtype=np.int32, usecols=[0,1])
	nMovies = Movies.shape[0]
	nUsers = 0
	with open(directory + 'ratings.csv', 'rb') as fh:
		fh.seek(-30, 2)
		last = fh.readlines()[-1].decode()
		nUsers = int(last[:last.index(',')]) + 1

	return nMovies, nUsers, Links, Movies