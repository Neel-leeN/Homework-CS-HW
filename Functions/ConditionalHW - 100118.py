#1
def driver_age(age):
	print("Can I drive?")
	if age >= 18:
		Legal = True
	else:
		Legal = False
	return Legal

var1 = 23
print(driver_age(var1))

#2
def triangle_type(big, med, small):
	if big>med+small:
		print ("Its not a triangle")
	elif big*big > med*med + small*small:
		print ("Its obtuse")
	elif big*big == med*med + small*small:
		print ("right angled triangle")
	else:
		print ("its acute")

a=5
b=4
c=3
triangle_type(a,b,c)

#3
def fizzbuzz(var):
	if var%5 == 0 and var%3 == 0:
		print("FIZZ BUZZ!")
	elif var%5 == 0:
		print("BUZZ!")
	elif var%3 == 0:
		print("FIZZ!")
	else:
		print("Huh?")

var2 = 2423424
fizzbuzz(var2)

#4
from math import factorial as f
def combination(n,r):
	return (f(n))/((f(r))*(f(n-r)))

var1 = 5
var2 = 1
print(combination(var1,var2))

#5
from random import random as rand, randint as randi
print(rand())
print(randi(0,100))

def comment(name):
	print(name + ', ' + reply[randi(0,len(reply)-1)])

reply = ["You're the best", "You're IQ is lower than Peter", "Einstein?", "Go home, you're out of place in smart areas"]
comment("Neel")

#6
def RNG(guess1,guess2,guess3):
	count = 0
	if guess1 == randi(1,6):
		count+=1
	if guess2 == randi(1,6):
		count+=1
	if guess3 == randi(1,6):
		count+=1
	print("You got ", count ,"guess(es) right")

varI = 2
varII = 5
varIII = 3

RNG(varI,varII,varIII)