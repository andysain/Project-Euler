"""
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20x20 grid?"""

n = 21
grid = [[0,]*n]*n
grid[0] = [1,]*n
for r,row in enumerate(grid):
	grid[r][0] = 1 
	#print row

for r,row in enumerate(grid):
	for c,col in enumerate(row):
		if c > 0 and r>0:
			grid[r][c] = grid[r][c-1] + grid[r-1][c]
	#print row
routePoss = grid[n-1][n-1]
print len(str(routePoss))