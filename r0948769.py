import Reporter
import numpy as np
from numpy import random
import math
import numba
from numba import jit


@jit((numba.int32, numba.float32)(numba.float32[:], numba.float32[:,:]))
def fitness(individual, distanceMatrix):
	n = individual.shape[0]
	if n == 0:
		return 0.0
	distance = distanceMatrix[individual[-1], individual[0]]
	infinities = 0
	for idx in range(n - 1):
		a = individual[idx]
		b = individual[idx+1]
		if a != np.inf and b != np.inf:
			distance += distanceMatrix[a, b]
		else:
			infinities += 1
	return np.array([infinities, distance])

# Modify the class name to match your student number.
class r0948769:

	def __init__(self):
		self.reporter = Reporter.Reporter(self.__class__.__name__)
		self.popNum = 1 # this is later multiplied by sqrt(N), where N is total number of cities
		self.mutProb = 0.05
		self.topK = 3
		self.tournamentSize = 3

	# The evolutionary algorithm's main loop
	def optimize(self, filename):
		# Read distance matrix from file.		
		file = open(filename)
		distanceMatrix = np.loadtxt(file, delimiter=",")
		file.close()

		# Generator for random number generation
		rng = random.default_rng(12345)

		numCities = distanceMatrix.shape[0]
		self.popNum = math.ceil(numCities**(1/2))

		def selection(population):
			parents = np.zeroes(self.popNum)
			for i in range(self.popNum):
				chosenIndividualsIdx = rng.integers(low=0, high=self.popNum, size=3)
				fitVals = np.zeros(self.tournamentSize)
				fitInfs = np.zeros(self.tournamentSize)
				for j in range(self.tournamentSize):
					fitInfs[j] = fitness(population[chosenIndividualsIdx[j]])[0]
					fitVals[j] = fitness(population[chosenIndividualsIdx[j]])[1]

				parents[i] = chosenIndividualsIdx[np.lexsort((fitVals, fitInfs))[0]]

			return parents

		# idea is to implement edge recombination, like group 27
		# in the return statement we already merge offspring with population
		def recombination(population, parents):
			offspring = np.zeros(len(parents)//2)
			child = np.zeros(numCities)
			for i in range(numCities):
				if rng.random() <= 0.5:
					child[i] = parents[0, i]
				else:
					child[i] = parents[1, i]

			popAndOff = np.concatenate((population, offspring), axis=0)
			return popAndOff

		# Portfolio of mutations just like in our group project
		def mutation(population):
			if rng.random() < self.mutProb:
				rndmDummy = rng.random()
				if rndmDummy < 0.65:
					# mutation 1
					pass
				elif 0.65 <= rndmDummy < 0.85:
					# mutation 2
					pass
				else:
					# mutation 3
					pass
			return 0

		def elimination(popAndOff):
			fitInfs = np.zeros(len(popAndOff))
			fitVals = np.zeros(len(popAndOff))
			for idx in range(len(popAndOff)):
				fitInfs[idx] = fitness(popAndOff[idx])[0]
				fitVals[idx] = fitness(popAndOff[idx])[1]

			idxSorted = np.lexsort((fitVals, fitInfs))
			survivors = np.delete(popAndOff, idxSorted[:-len(popAndOff)-self.popNum])
			return survivors

		# Your code here.
		yourConvergenceTestsHere = True
		while( yourConvergenceTestsHere ):
			# Your code here.
			meanObjective = 0.0
			bestObjective = 0.0
			bestSolution = np.array([0,1,2,3,4,5,6])



			# Call the reporter with:
			#  - the mean objective function value of the population
			#  - the best objective function value of the population
			#  - a 1D numpy array in the cycle notation containing the best solution 
			#    with city numbering starting from 0
			# Leave the next three lines as they are.
			timeLeft = self.reporter.report(meanObjective, bestObjective, bestSolution)
			if timeLeft < 0:
				break

		# Your code here.
		return 0


__build_hash__ = "447be2744c11fd5d50e5995e5c1801e89fee68b5f22965aecff55f0978405c24"
if __name__ == '__main__':
	pass
