l = [1,22,13,41,25,16]

#1
def foo1(li):
	if li[-1] == 6 or li[1] == 6:
		return True
	else:
		return False

print(foo1(l))

#2
def foo2(li):
	l = []
	for i in range(1,len(li)):
		l.append(li[-i])
	l.append(li[0])
	return l

print(foo2(l))

#3
def foo3(li):
	l = []
	l.append(li[0])
	l.append(li[-1])
	return l

print(foo3(l))

#4
def foo4(li):
	two_3 = False
	for item in li:
		if item == 2 or item == 3:
			two_3 == True
	return two_3

print(foo4(l))

#5
def foo5(li):
	even_count = 0
	for item in li:
		if item%2 == 0:
			even_count += 1
	return even_count

print(foo5(l))

#6
def foo6(li):
	total = 0
	for item in range(len(li)):
		if li[item] != 13 and li[item-1] != 13:
			total += li[item]
	return total

print(foo6(l))

#7
def foo7(li):
	li.sort()
	li.pop()
	li.pop(0)
	return sum(li)/len(li)

print(foo7(l))

#8
def foo8(li):
	Palandrome = True
	for i in range(len(li)):
		if li[i] != li[len(li)-i-1]:
			Palandrome = False
	return Palandrome

print(foo8(l))

#9
str_l = ["HI","hi","hI","Hi","ByE","Bye"]

def foo9(li):
	new_li = []
	for i in range(len(li)):
		repeat = False
		for j in range(0,i):
			if li[i].lower() == li[j].lower():
				repeat = True
		new_li.append(li[i].lower()) if repeat is False else print()
	return new_li

print(foo9(str_l))

#10
from random import randint as R

def foo10a():
	li = []
	for i in range(5):
		li.append((R(-100,100),R(-100,100),R(-100,100)))
	return li

def foo10b(li):
	min_distance = 600
	for i in range(len(li)):
		for j in range(i+1,len(li)):
			il = li[i]
			jl = li[j]
			var = abs(il[0]-jl[0]) + abs(il[1]-jl[1]) + abs(il[2] - jl[2])
			if var<min_distance:
				min1 = i
				min2 = j
	return min1,min2

li = foo10a()
print(li)
print(foo10b(li))

def foo11():
	l = []
	total = 0
	for i in range(100):
		l.append(R(0,1000))
	for item in l:
		count = 0
		for Item in l:
			if abs(item-Item) <=20:
				count+= 1
		if count <= 1:
			total +=1
	return total

print(foo11())