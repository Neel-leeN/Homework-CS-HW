#1a --> 34
#1b --> 16
#1c --> 27

#2
a = 10
b = 20
c = 30

def foo1(a):
	a = b + c
	print(a)

foo1(3)

#3
def foo2(d,e,f):
	var1 = d + e + f
	var2 = a + b + c
	return var1, var2

print(foo2(3,4,5))

#4
def add(num1,num2):
	return num1 + num2

def triple(num):
	return add(num + add(num,num))

def quadruple(num):
	return add(num + triple(num))

#5 - 9 ; in main.py

#10
import math as m
print(m.fabs(-29))
print(m.factorial(4))
print(m.e)
print(m.log(25,5))
print(m.pi)

#11
from math import sqrt
print(sqrt(25))