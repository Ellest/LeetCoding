def rotate_square(matrix):
	N = len(matrix)
	# only need to process upper quadrant
	for i in range(N//2):  
		for j in range(N - N//2): # to avoid double processing for odd dimensions
			temp = matrix[i][j]
			r, c = i, j
			for _ in range(4): # 4 rotations
				r, c = ~c, r
				temp, matrix[r][c] = matrix[r][c], temp

def rotate_rectangle(matrix):
	return_matrix = [[0] * len(matrix) for _ in range(len(matrix[0]))]
	for r in range(len(matrix)):
		for c in range(len(matrix[0])):
			return_matrix[~c][r] = matrix[r][c]
	return return_matrix

def rotate(matrix):
	if matrix:
		if len(matrix) == len(matrix[0]):
			rotate_square(matrix)
		else:
			return rotate_rectangle(matrix)


if __name__ == '__main__':
	matrix = \
		[
			[1,2,3,4,5],
			[6,7,8,9,10],
			[11,12,13,14,15]
		]

	result = rotate_rectangle(matrix)

	for r in result:
		print(r)