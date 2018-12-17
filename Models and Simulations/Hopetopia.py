#Importing all functions
from matplotlib import pyplot as p
from random import random as r

#Defining all variables
population = [91, 84]	
time = 0
max_pop = 800
death_rate = 0.05
exes = []
g_wise = []
b_wise = []

for i in range(40):
	for j in range(int(population[0])):
		if r() <= 0.15:
			population[0] += 1
		elif 0.15 < r() <= 0.3:
			population[1] += 1
	population[0] *= (1 - death_rate)
	population[1] *= (1 - death_rate)
	exes.append(i)
	g_wise.append(population[0])
	b_wise.append(population[1])
	# if population[0] + population[1] > max_pop:
	# 	death_rate **= 1/2
	# elif population[0] + population[1] <= max_pop:
	# 	death_rate = 0.05

p.figure()
p.plot(exes, g_wise, color = 'g')
p.plot(exes, b_wise, color = 'b')
p.xlabel('Months')
p.ylabel('Population')
p.title('Hopetopia Population Growth')
p.legend(['girls','boys'],loc='upper right')
p.show()