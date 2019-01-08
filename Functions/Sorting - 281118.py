a = [1, -3, 5, 7, 15, -4, 0, -6, -10, -11, 12]

def bubble_sort(a):
	for i in range(len(a)):
		if a[i] > a[i+1]:
			var1 = a[i]
			a[i]=a[i+1]
			a[i+1]=a[i]

def odd_even_sort(a):
	deletes = 0
	for j in range(len(a)):
		i = j-deletes
		if a[i]%2 == 0:
			a.append(a.pop(i))
			deletes += 1 
	return a

def positive_negative_sort(a, deletes = len(a)):
	print(a.append(a.pop(i)) for j in range(len(a)) if a[j] <0)

positive_negative_sort(a)