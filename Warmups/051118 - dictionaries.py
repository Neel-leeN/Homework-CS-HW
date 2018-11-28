from random import randint as r
from random import random as R 

#LHS
# Dict = {}
# for i in range(10):
# 	Dict[i] = 0 
# for i in range(10000):
# 	Dict[r(0,9)] += 1
# for key in Dict:
# 	print('num', key,':', Dict[key])

#RHS
d = {}
for i in range(10):
	d[i] = []
for i in range(21):
	n = R() * 10
	d[int(n)].append(round(n,2))
for key in d:
	print(key,':', d[key])