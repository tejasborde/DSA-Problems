import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')

# A Program to prints common element
# in all rows of matrix

M = 4
N = 5

def printCommonElements(mat):

	mp = dict()
	for j in range(N):
		mp[mat[0][j]] = 1

	for i in range(1, M):
		for j in range(N):
			if (mat[i][j] in mp.keys() and
							mp[mat[i][j]] == i):
								
				mp[mat[i][j]] = i + 1

				# If this is last row
				if i == M - 1:
					print(mat[i][j], end = " ")

mat = [[1, 2, 1, 4, 8],
	[3, 7, 8, 5, 1],
	[8, 7, 7, 3, 1],
	[8, 1, 2, 7, 9]]

printCommonElements(mat)

