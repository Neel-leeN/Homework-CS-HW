from random import randint
from time import sleep
from matplotlib import pyplot as p

def two_to_one(money,betted):
	land = circle[randint(0,37)]
	if land in bet:
		money = round(money + betted,2)
	else:
		money = round(money - betted,2)
	return money, land

def three_to_one(money,betted):
	land = circle[randint(0,37)]
	if land in bet:
		money = round(money + 2*betted, 2)
	else:
		money = round(money - betted, 2)
	return money, land

def thirty_six_to_one(money,betted):
	land = circle[randint(0,37)]
	if land in bet:
		money = round(money + 35*betted, 2)
	else:
		money = round(money - betted, 2)
	return money, land

def average_list(li):
	ave_li = []
	for i in range(len(li[0])):
		ave = 0
		for j in range(10000):
			ave += li[j][i]
			if ave < 20:
				break
		ave_li.append(round((ave/10000), 2))
	return ave_li

circle = [str(i) for i in range(0,37)]
circle.append('00')

step = []
test = []

odd = circle[1:36:2]
even = circle[2:37:2]
red = ["1","3","5","7","9","12","14","16","18","19","21","23","25","27","30","32","34","36"]
black = ["2","4","6","8","10","11","13","15","17","20","22","24","26","28","29","31","33","35"]
FirstTwelve = circle[1:13]
SecondTwelve = circle[13:25]
ThirdTwelve = circle[25:37]

bets = [odd, even, red, black, FirstTwelve, SecondTwelve, ThirdTwelve]
TwoToOne = (odd, even, red, black)
ThreeToOne = (FirstTwelve, SecondTwelve, ThirdTwelve)
ThirtySixToOne = []

for i in range(38):
	bets.append(circle[i])
	ThirtySixToOne.append(circle[i])

for i in range(2,7):
	cash_total = []
	for j in range(10000):	
		money = 1000
		cash = [money]
		for k in range(100):
			betted = round(money/i,2)
			bet = bets[randint(0,len(bets)-1)]
			if bet in TwoToOne:
				money, land = two_to_one(money, betted)
			elif bet in ThreeToOne:
				money, land = three_to_one(money, betted)	
			elif bet in ThirtySixToOne:
				money, land = thirty_six_to_one(money, betted)
			cash.append(money)
			# print(i+1, 'role has elapsed, ', 'in this round, the ball landed on ',land, " and you betted $", betted,"so now you have $", money)
		cash_total.append(cash)
	cash_ave = average_list(cash_total)
	test.append(cash_ave)


p.figure()
p.plot(test[0], color = 'r')
p.plot(test[1], color = 'g')
p.plot(test[2], color = 'b')
p.plot(test[3], color = 'y')
p.plot(test[4], color = 'purple')
p.xlabel('Rolls')
p.ylabel('Money')
p.title('Roulette Model; betting x% of money each time')
p.legend(['bet 50%', 'bet 33%', 'bet 25%', 'bet 20%', 'bet 17%'],loc='upper right')
p.show()