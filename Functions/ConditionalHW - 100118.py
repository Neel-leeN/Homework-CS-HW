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
def combination()