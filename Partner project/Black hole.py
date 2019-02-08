from random import randint

grid = [['0'] * 4 for i in range(4)]
movement = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Player = *, Black Hole = 1, Prize = $
for i in holes:
    grid[i[0]][i[1]] = 1

grid[0][0] = '*'
asterix = [0,0]
grid[1][1] = '2'
grid[1][1] = '2'
grid[1][1] = '2'
grid[3][3] = '$'


for i in range(10):
	print(grid)
	move = randint(0,3)
	grid[asterix[0]+movement[move][0]][asterix[1]+movement[move][1]] = '*'
print(holes)
