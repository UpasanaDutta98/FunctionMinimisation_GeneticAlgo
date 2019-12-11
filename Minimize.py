import numpy as np
import random
class Genetic(object):
	
	def __init__(self, f, pop_size = 500, n_variables = 1):
		self.f = f
		self.minim = -65536
		self.maxim = 65536
		self.pop_size = pop_size
		self.n_variables = n_variables
		self.population = self.initializePopulation()
		#print(self.population)
		#self.evaluatePopulation()

	def initializePopulation(self):
		return [np.random.randint(self.minim, self.maxim, size=(self.n_variables)) for i in range(self.pop_size)]
		# np.random.randint returns a random integer from self.minim (inclusive) to self.maxim (exclusive).
		# size is the output shape. If the given shape is, e.g., (m, n, k), then m * n * k samples are drawn. Here, size is 1. So random integers are returned in the form of array([-29777]), or array([34246]).
		# if no size is mentioned, then single random numbers are returned, but not in the form of any array / list.
		# so we start with 'population_size' number of random numbers in our population.

	def evaluatePopulation(self):
		#for i in self.population:
		#	print(i)
		return [self.f(i[0]) for i in self.population]
		# evaluate the values of f(x) for all values of x in the population and return that in a list of size population_size.
		# Here i[0] is used because the random integers are present inside self.population in the form of lists of length 1.

	def nextGen(self):
		results = self.evaluatePopulation()
		# results is just a simple list of size 'population_size'

		children = [self.population[np.argmin(results)]]
		#print("Current best - ", children[0]) -------------------------------------------------------------------------------------
		# so np.argmin(results) gives the index of the minimum value in list - 'results' (results contains f(x) values)
		# so children is a list containing the random integer, say [x1], that has the minimum f(x) value. And children list becomes the population for the next generation at the end. So we ARE retaining the best x values for the next generation!

		while len(children) < self.pop_size:
		# Parents are selected by Tournament selection


			#print(children)
			randA, randB = np.random.randint(0, self.pop_size), \
				       np.random.randint(0, self.pop_size)
			# randA, randB are random index numbers (range is 0 to population_size)


			#print("\n\n\n\n")
			#for i in self.population:
			#	print(i, end = " ")
			if results[randA] < results[randB]: #results is a list of f(x) values of all the x in population.
				p1 = self.population[randA]
			else: 
				p1 = self.population[randB]
			# so after tournament, choose p1 as that [x] whose f(x) value is lesser.




			randA, randB = np.random.randint(0, self.pop_size), \
				       np.random.randint(0, self.pop_size)  
			if results[randA] < results[randB]: 
				p2 = self.population[randA]
			else: 
				p2 = self.population[randB]   
			# so after tournament, choose p2 as that [x] whose f(x) value is lesser.




			signs = []
			if p1[0] < 0: 
				signs.append(-1)
			else: 
				signs.append(1)
			if p2[0] < 0: 
				signs.append(-1)
			else: 
				signs.append(1)
			#print(signs)
			#So the 'sign' list contains signs of p1 and p2 (p1 and p2 contains are lists of size one, like [x5] ... [x10])





			# Convert values of parent1 and parent2 to binary
			p1 = format(abs(p1[0]), '010b')
			p2 = format(abs(p2[0]), '010b')


			# p1 and p2 are now binary numbers.
			#print(p1, p2)  gives - 11011101000100 11011101000100
			#print(tuple(zip(p1, p2)))  gives - (('1', '1'), ('1', '0'), ('0', '0'), ('0', '0'), ('1', '0'), ('0', '1'), ('1', '1'), ('1', '1'), ('0', '1'), ('0', '0'), ('0', '1'), ('0', '1'), ('0', '0'), ('0', '1'), ('1', '1'))




			# Recombination / Crossover
			
			child = []
			'''
			for i, j in zip(p1, p2):
				for k, l in zip(i, j):
					if k == l:
						child.append(k) # if same position bits are similar in parent1 and parent2, it goes to child.
					else: 
						a = np.random.randint(0,2) # else the child gets the bit of a random parent.
						child.append(str(a))
						#print(str(a))
			'''
			# ARITHMETIC CROSSOVER (AND)
			for i, j in zip(p1, p2):
				for k, l in zip(i, j):
					if k == l:
						child.append(k) # if same position bits are similar in parent1 and parent2, it goes to child.
					else: 
						child.append(str(0))


			# MUTATION WITH MUTATION RATE OF 0.01
			#for i in range(len(child)) :
			x = np.random.randint(1, 101)
			if x == 100 :
				i = np.random.randint(0, len(child))
				if child[i] == '0' :
					child[i] = '1'
				else :
					child[i] = '0'




			child = ''.join(child)
			# join function converts a list to a string.
			# so child is a binary string.



			# // means integer division.
			#g1 = child[0:len(child)//2]	# g1 is the first half of the child string
			#g2 = child[len(child)//2:len(child)]	# g2 is the second half of the child string
			

			x = random.choice([signs[0], signs[1]])
			#print("children = ", np.asarray([x*int(child, 2)]))
			children.append(np.asarray([x*int(child, 2)]))


			# Arijit's code - 
			# children.append(np.asarray([signs[0]*int(g1, 2)]))#,
                                        #signs[1]*int(g2, 2)]))
		self.population = children

	def run(self):
		ix = 0
		while ix < 2000:
			ix += 1
			self.nextGen()
		return self.population[0] # return the first element of the population

f = lambda x: (x)**2-50*x+10
gen = Genetic(f)
minim = gen.run()
print('\n\nMinimum value of function found with X =', minim[0], "\n\n")

