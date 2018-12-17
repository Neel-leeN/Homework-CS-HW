#Importing all modules
from random import randint as r, triangular as t, random as R
from matplotlib import pyplot as p
from math import log as l

#Defining all variables
population = 1
step = 12
time = 0
birth_rate = 0.15
death_rate = 0.005
predator_rate = 0.05
exes = []
wise = []

for i in range(12):
	for j in range(population):
		k = int(t(1,10,7))
		for l in range(k):
			if R() <= birth_rate:
				population += 1
	population=int(round(population*(1-(death_rate+predator_rate))))
	print(population)
	exes.append(i*step)
	wise.append(population)

p.figure()
p.plot(exes,wise)
p.xlabel('Hours')
p.ylabel('Population')
p.title('Trebble Population Growth')
p.legend(['Trebble population'],loc='upper right')
p.show()