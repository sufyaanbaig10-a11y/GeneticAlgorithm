import Reporter
import numpy as np
from numpy import random
import math
import numba
from numba import jit


@jit()
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
	# the return statement might not be supported by Numba
	return np.array([infinities, distance])

@jit(numba.float32[:,:](numba.float32[:], numba.float32[:]))
def adjacencySet(parent1, parent2, numCities):
	adjSet = np.zeros(numCities)
	idx = 0
	for city in parent1:
		numNeighbors = 4
		idxP2 = np.argsort(parent2)[city]

		n1 = parent1[idx-1]
		n2 = parent1[idx+1]
		n3 = parent2[idxP2-1]
		n4 = parent2[idxP2+1]

		# edges present in both parents are a multiple of pi
		if n1 == n3:
			numNeighbors -= 1
			n1 = n1*np.pi
			n3 = -1
		elif n1 == n4:
			numNeighbors -= 1
			n1 = n1*np.pi
			n4 = -1

		if n2 == n3:
			numNeighbors -= 1
			n2 = n2*np.pi
			n3 = -1
		elif n2 == n4:
			numNeighbors -= 1
			n2 = n2 * np.pi
			n4 = -1

		possibleNeighbors = np.array((n1, n2, n3, n4))

		neighbors = np.zeroes(numNeighbors)
		for i in range(possibleNeighbors.shape[0]):
			if possibleNeighbors[i] != -1:
				neighbors[i] = possibleNeighbors[i]

		adjSet[city] = neighbors
		idx += 1

		return adjSet

		# Adjacency set with directed feasibility controls
		# if distanceMatrix[n1, city] != np.inf:
		# 	neighborsCity[0] = n1
		#
		# if distanceMatrix[city, parent1[idx + 1]] != np.inf:
		# 	neighborsCity[1] = parent1[idx + 1]
		#
		# if distanceMatrix[parent2[idxP2 - 1], city] != np.inf:
		# 	neighborsCity[2] = parent2[idxP2 - 1]
		# 	if
		#
		# if distanceMatrix[city, parent2[idxP2 + 1]] != np.inf:
		# 	neighborsCity[3] = parent2[idxP2 + 1]


@jit(numba.int16[:,:](numba.int16[:,:], numba.int16))
# changing the city to a negative value constitutes removing that city
def removeCity(adjacencySet, city):
	adjacencySet[city] = -1 * adjacencySet[city] - 1
	for neighbors in adjacencySet:
		for i in neighbors:
			if i == city:
				i = -1
	return adjacencySet


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
			offspring = np.zeros(parents.shape[0]//2)
			idxParents = parents.shape[0]-1

			if parents.shape[0]%2 != 0:
				parents = np.concatenate((population[rng.integers(low=0, high=self.popNum, size=1)], parents))
			while idxParents >= 1:
				p1 = parents[idxParents]
				p2 = parents[idxParents-1]
				adjSet = adjacencySet(p1, p2, numCities)

				child = np.zeros(numCities)
				child[0] = p1[0]



				idxParents -= 2

			popAndOff = np.concatenate((population, offspring), axis=0)
			return popAndOff

		def chooseNextEdge(adjacencySet, possibleEdges):
			for i in possibleEdges:

				if i%np.pi == 0:
					return i
				elif

			return chooseNextEdge(adjacencySet, )
			return 0

		def mutation(popAndOff):
			idx = popAndOff.shape[0]-1
			while idx >= 0:
				if rng.random() < self.mutProb:
					mutate = popAndOff[idx]
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
				idx -= 1
			return 0

		def elimination(popAndOff):
			fitInfs = np.zeros(popAndOff.shape[0])
			fitVals = np.zeros(popAndOff.shape[0])
			for idx in range(popAndOff.shape[0]):
				fitInfs[idx] = fitness(popAndOff[idx])[0]
				fitVals[idx] = fitness(popAndOff[idx])[1]

			idxSorted = np.lexsort((fitVals, fitInfs))
			numOffspring = popAndOff.shape[0]-self.popNum
			survivors = np.delete(popAndOff, idxSorted[:-numOffspring])
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
