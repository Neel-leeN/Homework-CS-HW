#1 
def small_2(lis1):
	lis1.sort()
	a = lis1[0]
	b = lis1[1]
	return a,b

lis = [54,3,54,3355,234,3,43,23,1,8]
print(small_2(lis))

#2
lis = [54,3,54,3355,234,3,43,23,1,8]
def remove_odd(lis2):
	lis3 = []
	for item in lis2:
		if item%2 == 0:
			lis3.append(item)
	return lis3

print(remove_odd(a))

#3
def split_words(lis4):
	lis4.split()
	return lis4