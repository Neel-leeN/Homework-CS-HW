'''
#1 - 5pts
import pygame
from time import sleep as Zzz

screen = pygame.display.set_mode((500, 500))
green = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if green<=255:
    	pygame.draw.circle(screen, (0, green, 0), (250, 250), 50)
    elif green<=510:
    	pygame.draw.circle(screen, (0, 510-green, 0), (250, 250), 50)
    else:
    	pygame.draw.circle(screen, (255,255,255), (250, 250), 50)

    green+=2
    Zzz(0.1)
    pygame.display.update()
pygame.quit()
'''
#7 - 20

import pygame
from random import randint as r 
from time import sleep as Zzz

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('iMeanuel')

x = r(0,599)
y = r(0,599)
x_list = []
y_list = []
x_list.append(x)
y_list.append(y)
pygame.draw.rect(screen, (255,255,255), ((x,y), (1,1)))
pygame.display.update()
Dir = r(1,4)

def repeat(x,y):
	Repeat = False
	for i in range(len(x_list)):
		if x == x_list[i]:
			if y == y_list[i]:
				Repeat = True
	return Repeat

def direction(x,y,Dir,old_d):
	if Dir == 1:
		new_x = x+1
	elif Dir == 2:
		x-=1	
	elif Dir == 3:
		y+=1
	elif Dir ==4:
		y-=1		
	if (old_d<3 and Dir>2) or (old_d>2 and Dir<3) and repeat(x,y) == False:
		return x,y,Dir
	else:
		return old_d

def movement(x,y, old_d):
	count = 0
	New_Dir = r(1,4)
	while 0<x<600 and 0<y<600 and count<r(10,50):
		pygame.draw.rect(screen, (255,255,255), ((x,y), (1,1)))
		x,y,Dir = direction(x,y,New_Dir,old_d)
		count += 1
		x_list.append(x)
		y_list.append(y)
		pygame.display.update()
	return x,y,Dir

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	pygame.draw.rect(screen, (255,255,255), ((x,y), (1,1)))
	x,y,Dir = movement(x,y,Dir)
pygame.quit()

'''
def Direction(x,y):
	if cant == None:
		cant = r(2,3)
	Dir = r(1,4)
	if Dir == 4 and cant <=2:
		x+=1
	elif Dir == 3 and cant <=2:
		x-=1
	elif Dir == 2 and cant >2:
		y+=1
	elif Dir == 1 and cant >2:
		y-=1
	else:
		Direction(x,y)
	return x,y
	

def Movement(x,y):
	Dir = r(1,4)
	count = 0
	limit = r(10,50)
	while (0<=x<=600) and (0<=y<=600) and (x != x_list[i] and y!= y_list[i] for i in range (0,len(x_list))) and count<limit:
		x_list.append(x)
		y_list.append(y)
		pygame.draw.rect(screen,(255,255,255), ((x,y),(1,1)))
		pygame.display.update()
		print (x,y)
		if Dir == 1:
			x+=1
		elif Dir == 2:
			x-=1
		elif Dir == 3:
			y+=1
		else:
			y-=1
		count+=1
		pygame.draw.rect(screen,(255,255,255), ((x,y),(1,1)))
	Zzz(0.01)
	pygame.display.update()
	return x,y


running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	#pygame.draw.rect(screen, (255, 255, 255), ((x, y), (3,3)))
	x,y = Movement(x,y)
	pygame.display.update()
pygame.quit()
'''