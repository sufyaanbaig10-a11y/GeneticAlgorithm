import Reporter
import numpy as np
from numpy import random
import math
import numba
from numba import njit, prange


@njit
def fitness(individual, distanceMatrix):
	n = individual.shape[0]
	if n == 0:
		return 0.0
	distance = distanceMatrix[individual[-1], individual[0]]
	for idx in range(n - 1):
		distance += distanceMatrix[individual[idx], individual[idx + 1]]
	return distance

# Modify the class name to match your student number.
class r0948769:

	def __init__(self):
		self.reporter = Reporter.Reporter(self.__class__.__name__)
		self.popNum = 1 #  this is later multiplied by sqrt(N), where N is total number of cities
		self.mutProb = 0.05
		self.topK = 3

	# The evolutionary algorithm's main loop
	def optimize(self, filename):
		# Read distance matrix from file.		
		file = open(filename)
		distanceMatrix = np.loadtxt(file, delimiter=",")
		file.close()

		#Generator for random number generation
		rng = random.default_rng(12345)

		numCities = distanceMatrix.shape[0]
		self.popNum = math.ceil(numCities**(1/2))



		def selection(population):
			parents = np.zeroes(self.popNum)
			for i in range(self.popNum):
				chosenIndividualsIdx = rng.integers(low=0, high=numCities, size=3)
				fitVals = np.zeros(3)
				for j in range(self.topK):
					fitVals[j] = fitness(population[chosenIndividualsIdx[j]])
				parents[i] = population[chosenIndividualsIdx[np.argsort(fitVals)[0]]]

			return parents

		#idea is to implement edge recombination, like group 27
		#parents is a 2D array with two individuals, at least for now
		def recombination(parents):
			child = np.zeros(numCities)
			for i in range(numCities):
				if rng.random() <= 0.5:
					child[i] = parents[0, i]
				else:
					child[i] = parents[1, i]

			return 0

		#Portfolio of mutations just like in our group project
		def mutation(population):
			if rng.random() < self.mutProb:
				rndmDummy = rng.random()
				if rndmDummy < 0.65:
					#mutation 1
					pass
				elif (rndmDummy >= 0.65 and rndmDummy < 0.85):
					#mutation 2
					pass
				else:
					#mutation 3
					pass
			return 0


		def elimination(population):

			return 0


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
	test = r0948769()
	test.optimize("C:\Users\sufya\PycharmProjects\GeneticAlgorithm\tour50")

	pass