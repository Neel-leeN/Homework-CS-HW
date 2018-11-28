'''#1 - Syntax error
var = 3
print var1

#1 - Run-time error
var = input('3')
for n in range (0,var):
	print(n)


#1 - Logic error
var = 3
while var1 > 3:
	print ('hi')

#2 - Zero division error
var = 3/0
print(var)

#2 - TypeError
var = 'one'
print(1+var)

#2 - ValueError
var1 = int('Crash this')

#2 - NameError
print (var)

#3 - Fixing errors

while True:
	try:
		var = int(input('reenter'))
	except:
		print('retype')
	else:
		break