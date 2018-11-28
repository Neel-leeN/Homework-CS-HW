
#Easy
my_list = ['a','z','d','g']
print (my_list)
var1 = my_list[0]
my_list.append(var1)
var1 = my_list[3]
my_list.pop(3)
my_list[0] = var1
print (my_list)

#Medium
my_list = ['a','z','d','g']
var1 = ['a','z','d','g']
my_list[3] = var1[0]
my_list += var1[3]
my_list.pop(0)
my_list += var1[1] + var1[2]

#Hard
my_list = ['a','z','d','g']
print (my_list[1::2],my_list[0::2])

#Easy
my_list = ['a','z','d','g']
for i in range(0,len(my_list)):
	print (5*my_list[i])

#Medium
from random import randint as r
a = []
while len(a) < 100:
	var = r(0,100)
	if var%7>0 and var%2>0:
		a.append(var)
	#print(a)

#Dictionaries - Easy
d = {'a':r(0,99),'b':r(0,99),'c':r(0,99)}
print (d)

#Dictionaries - Medium
d2 = {}
for i in range(100):
	var = chr(r(0,26))
	print (var)