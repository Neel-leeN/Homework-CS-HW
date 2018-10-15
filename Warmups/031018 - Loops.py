'''#Easy
count = 0
while count < 10:
	print(count*10)
	count += 1

#Medium
total=-23
count=0
while total <= -5:
	total+=0.2
	print(round(total),2)
	count+=1

#Easy
b = 2
a = 1
for n in range(0,5):
	a = b * a + n
print (a)

#Medium
for n in range(1,101):
	if n%3 > 0 and n%8 >0:
		print(n)
'''
#Difficult
height = 9	
space = " "
print(height*space+"*")
for i in range(1,height):
	print((height-i)*space + "*" + (2*i-1)*space + "*")
for i in range(1,height-1):
	print((i+1)*space+"*" + (2*(height - i-1)-1)*space + "*")
print(height*space+"*")