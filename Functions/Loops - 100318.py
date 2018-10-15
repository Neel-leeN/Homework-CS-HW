#1
max =  8
min =- 3
def count_down(max,min):
	while max>=min:
		print(max)
		max -= 1

count_down(max,min)

#2
max = 10
def is_odd(var):
	return var%2

for n in range(0,max):
	if is_odd(n) == 1:
		print(n)

#3
from random import randint as rand
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

def dice_roll():
	var = rand(1,6)
	return var

for For in range(0, max):
	var = dice_roll()
	if var == 1:
		one += 1
	elif var ==2:
		two += 1
	elif var == 3:
		three += 1
	elif var == 4:
		four += 1
	elif var == 5:
		five += 1
	else:
		six += 1

print (one, two, three, four, five, six)

#Extension