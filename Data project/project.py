import codecs
import pickle

heading = []
types = []
movie_data = []
with codecs.open('movies.txt','r',encoding='utf-8') as f:#utf-b8: universal characters list
	line = f.readline()
	heading = line.strip().split(';')

	# print(heading)
	
	f.readline()
	#types = line.split().strip(';')

	for line in f.readlines():
		line = line.strip('\t').split(';')
		line = tuple(line)
		movie_data.append(line)

	# for item in movie_data:
	# 	for n in range(len(item)):
	# 		print(item[n])

# print(types)
# print(len(movie_data))
with codecs.open('movies.tsv','w',encoding='utf-8' ) as f:
	for movie in movie_data:
		for item in movie:
			# item = item.replace('\t',' ')
			f.write(item)
			f.write('\t')
			# print(item)
		f.write("\n")

by_year = {}
for n in range(len(movie_data)):
	year = movie_data[n][0]
	try:
		by_year[year].append(movie_data[n])
	except KeyError:
		by_year[year] = [movie_data[n]]

# for key in by_year:
# 	print(key,':')
# 	for item in by_year[key]:
# 		print(', ', item[2], end = '')
# 	print('\n')

by_actor = {}
for n in range(len(movie_data)):
	actor = movie_data[n][4]
	try:
		by_actor[actor].append(movie_data[n])
	except KeyError:
		by_actor[actor] = [movie_data[n]]

# for key in by_actor:
# 	print(key,':')
# 	for item in by_actor[key]:
# 		print(item[2], end = ', ')
# 	print('\n')

by_actress = {}
for n in range(len(movie_data)):
	actress = movie_data[n][5]
	try:
		by_actress[actress].append(n)
	except KeyError:
		if len(actress)>2:
			by_actress[actress] = [n]

# for key in by_actress:
#	print(key,':',movie_data[by_actress[key]][2])

by_director = {}
for n in range(len(movie_data)):
	director = movie_data[n][6]
	try:
		by_director[director].append(n)
	except KeyError:
		by_director[director] = [n]

# for key in by_director:
# 	print(key,':',movie_data[by_director[key]][2])

av_runtim = []
for key in by_year:
	# print(key)
	Sum = 0
	Count = 0
	for item in by_year[key]:
		if len(item[1])>0 :
			Sum += int(item[1])
			# print(Sum)
			Count+=1
	# print(Sum)
	# print(Count)
	# print(key,':', round(Sum/Count))
	av_runtim[key] = round(Sum/Count)
	with open('av_runtim.pickle','wb') as f:
		pickle.dump(av_runtim,f)
# print(av_runtim)

X = 0
actor_by_movies={}
for key in by_actor:
	count = 0
	# print(key, end = ': ')
	for item in key:
		if len(item) > X:
			count+=1
	try:
		actor_by_movies[count].append(key)
	except KeyError:
		actor_by_movies[count] = [key]

try:
	print(actor_by_movies[10])
except KeyError:
	print(' ')