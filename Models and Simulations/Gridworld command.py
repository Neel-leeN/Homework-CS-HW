import pygame
from random import randint, random	
from Gridworld import GridWorld
from time import sleep as Zzz

running = True

world = GridWorld(60, 40, 10)
suspectible = (0, 0, 255)
infected = (255, 0, 0)
recovered = (0, 255, 0)
death_rate = 0.005

for i in range(100):
    world.set_cell(randint(0, 60), randint(0, 40), recovered)
    world.set_cell(randint(0, 60), randint(0,40), suspectible)
    world.set_cell(randint(0, 60), randint(0, 40), infected)
world.update()
Zzz(2)

for i in range(18):
	for i in range(60):
		for j in range(40):
			if world.get_cell( i, j) == suspectible:
				threeinfect = world.count_surroundings(i, j, 3, infected) - world.count_surroundings( i, j, 2, infected)
				twoinfect = world.count_surroundings(i, j, 2, infected) - world.count_surroundings( i, j, 1, infected)
				oneinfect = world.count_surroundings(i, j, 1, infected)
				infectability = (0.02*threeinfect) + (0.05*twoinfect) + (0.25*oneinfect)
				if infectability > 0.97:
					infectability = 0.97
				if random() <= infectability:
					world.set_cell( i, j, infected)
			elif world.get_cell( i, j) == infected:
				if random() <= death_rate:
					world.set_cell( i, j, ( 255, 255, 255))
				elif random() < 0.34:
					world.set_cell( i, j, recovered)
	world.update()
	Zzz(1)

while running:
    if world.process_events() == True:
        break
    world.update()
pygame.quit()