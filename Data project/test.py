import codecs

#opening a file
# f = open('data.txt','r')

#printing the lines
#for line in f.readlines():
#	print(line,end="")
#	print(line.strip())

#list making
# lines = []
# for line in f.readlines():
# 	line = line.strip()
# 	line = line.split(',')
# 	line = tuple(line)
# 	lines.append(line)
# print(lines)


# lines = []
# with open('data.txt','r',encoding='utf-8') as f:#utf-b8: universal characters list
# 	for line in f.readlines():
# 		line = line.strip()
# 		line = line.split(',')
# 		line = tuple(line)
# 		lines.append(line)
# print(lines)
#f.close()

#try 2
paragraphs = []
with open('randtxtgen.txt','r',encoding='utf-8') as f:#utf-b8: universal characters list
	for line in f.readlines():
		line = line.strip()
		line = line.split('.')
		paragraphs.append(line)
		#print (line)
for item in paragraphs:
	for n in range(len(item)):
		if len(item[n]) > 0:
			print(item[n] + '.')