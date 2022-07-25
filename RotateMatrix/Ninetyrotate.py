class Ninetyrotate:

	def rotateMatrix(self, mat, n):
		for i in range(0,int(n/2)):
			for j in range(i,n-i-1):
				temp = mat[i][j]  
				mat[i][j] = mat[j][n-1-i]  
				mat[j][n-1-i] = mat[n-1-i][n-1-j]
				mat[n-1-i][n-1-j] = mat[n-1-j][i]
				mat[n-1-j][i] = temp
		return mat

if __name__ == '__main__':
	obj = Ninetyrotate()
	mat = [[0 for x in range(4)] for y in range(4)]
	mat = [[1, 2, 3, 4],
    	[5, 6, 7, 8],
    	[9, 10, 11, 12],
    	[13, 14, 15, 16]]
	res = obj.rotateMatrix(mat,4)
	for mat1 in mat:
		print(mat1)

		