from random import randint as r

A = []
B = []
R = []

for i in range(1,8):
	A.append(i)
for j in range(0,8):
	B.append(j+8)
print ("A: ", A, "\tB:", B)

for k in range(24):
	for i in range(3):
		varA = r(1,len(A))
		R.append(A.pop(varA-1))
	for i in range(4):
		varB = r(1,len(B))
		R.append(B.pop(varB-1))
	for i in range(7):
		varR = r(0,1)
		#print(varR)
		if varR == 0 and len(A) < 10:
			A.append(R.pop())
		elif varR == 1 and len(B) < 10:
			B.append(R.pop())
		elif varR == 0 and len(A) >= 10:
			B.append(R.pop())
		elif varR == 1 and len (B) >= 10: 
			A.append(R.pop())
	A.sort()
	B.sort()
	print("After", k," hour(s): A --> ", len(A), A, "\n\tB --> ",len(B), B)

print("End of the day: A --> ", len(A), A, "\n\tB --> ",len(B), B)