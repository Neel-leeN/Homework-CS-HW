from matplotlib import pyplot as p

susceptible = [0.99]
infected = [0.01]
recovered = [0]
dead = [0]
beta = 0.4
gamma = 0.2
deathr = 0.02
steps = 100

for i in range(steps):
	new_infected = beta * infected[i] * susceptible[i]
	new_dead = deathr * infected[i]
	new_recovered = gamma * (infected[i]-new_dead)

	susceptible.append(susceptible[i] - new_infected)
	infected.append(infected[i] + new_infected - new_recovered - new_dead)
	recovered.append(recovered[i] + new_recovered)
	dead.append(dead[i] + new_dead)

p.figure()
p.plot(susceptible)
p.plot(infected)
p.plot(recovered)
p.plot(dead)
p.xlabel('Months')
p.ylabel('Population')
p.title('Disease Growth')
p.legend(['susceptible', 'infected', 'recovered', 'dead'],loc='upper right')
p.show()

print(int(susceptible[-1] + infected[-1] + dead[-1] + recovered[-1]))