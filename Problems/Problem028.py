"""Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

[21, 22, 23, 24, 25],
[20,  7,  8,  9, 10],
[19,  6,  1,  2, 11],
[18,  5,  4,  3, 12],
[17, 16, 15, 14, 13]]


It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?"""

def createGrid(n):
	grid = [0,]*n*n
	grid[(n**2-1)/2] = 1
	# for r,row in enumerate(grid):
	# 	if r >0:
	# 		#for c in enumerate(row):
	# 		grid[r][0] = grid[r-1][0]-1
	# print grid
	#grid =[21, 22, 23, 24, 25,20,  7,  8,  9, 10,19,  6,  1,  2, 11,18,  5,  4,  3, 12,17, 16, 15, 14, 13]
	return diagSum(array(grid,n),n)

def array(grid,n):
	return [grid[i:i+n] for i in xrange(0,len(grid),n)] 

def diagSum(grid,n):
	return sum([grid[r][r] + grid[r][n-r-1] for r in range(n)])-1

print createGrid(5)