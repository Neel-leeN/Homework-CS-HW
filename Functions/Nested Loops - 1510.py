#1
import pygame
print('Hello')
print('Goodbye')

print('Hello', end = ' ')      #Ends line in a blank space
print('Goodbye')

for Range in range(0,5):
	for rAnge in range(0,10):
		print('*', end = '')
	print("") 

#2
Height = 5
for Pyramid in range(1, Height+1):
	print((Height - Pyramid) * " ", end="") 
	for Asterix in range(0, 2*Pyramid-1):
		print("*", end="")
	print("")

#3
Height = 7
var = int((Height-3)/2)
Width = 9
Width = Height - var
print((Width) * "* ")
for raNge in range(1,var+1):
	print("*" + (raNge)*" " + "*" + 2*(var-raNge)*" " + " *" + (raNge)*" " + "*")
for ranGe in range(0,var+1):
	print("*" + (var+1-ranGe)*" " + "*",end="")
	if ranGe>0:
		print((2*(ranGe)-1)*" " + "*" + (var-ranGe+1)*" "+ "*")
	else:
		print(((var-2*(ranGe)+1)*" "+ "*"))
print((Width) * "* ")

#4
# x = 0
# y = 0
# screen = pygame.display.set_mode((500, 500))

running = True
while running:
   	for event in pygame.event.get():
   		if event.type == pygame.QUIT:
   			running = False

   	for x in range(0,600,100):
	    for y in range(0,600,100):
 		   	if (x==200 and x==y) or (x==400 and x==y) or (x==0 and x==y):
 		   		pygame.draw.rect(screen, (255, 255, 255), ((x,y), (100 , 100)))
 		   	elif (y==200 and y==400-x) or (y==400 and y==400-x) or (y==0 and y==400-x):
 		   		pygame.draw.rect(screen, (255, 255, 255), ((x, y), (100, 100)))
 		   	elif (x==300 and y%200==100) or (x==100 and y%200==100):
 		   		pygame.draw.rect(screen, (255, 255, 255), ((x, y), (100, 100)))
 		   	elif (x==200 and y%200==0):
 		   		pygame.draw.rect(screen, (255, 255, 255), ((x, y), (100, 100)))
 		   	elif (y==200 and x%200==0):
 		   		pygame.draw.rect(screen, (255, 255, 255), ((x, y), (100, 100)))
	pygame.display.update()
pygame.quit()

#5
import pygame
from time import sleep as Zzz
from random import randint as rand
screen = pygame.display.set_mode((450, 500))

running = True
while running:
	red = rand(0,255)
	green = rand(0,255)
	blue = rand(0,255)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	for x in range(0,600,50):
		for y in range(0,600,50):
			if x==200  and y==0:
				pygame.draw.rect(screen, (rand(0,255), rand(0,255), rand(0,255)), ((x, y), (50, 100)))
			elif (150<=x<=250) and y==100:
				pygame.draw.rect(screen, (rand(0,255), rand(0,255), rand(0,255)), ((x, y), (50, 100)))
			elif 100<=x<=300 and y==200:
				pygame.draw.rect(screen, (rand(0,255), rand(0,255), rand(0,255)), ((x, y), (50, 100)))
			elif 50<=x<=350 and y==300:
				pygame.draw.rect(screen, (rand(0,255), rand(0,255), rand(0,255)), ((x, y), (50, 100)))
			elif 0<=x<=400 and y==400:
				pygame.draw.rect(screen, (red, green, blue), ((x, y), (50, 100)))
	Zzz(0.1)
	pygame.display.update()
pygame.quit()
