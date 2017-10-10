# [a, b, c, d, e, f, ... ]

# maxsum[i] = max(maxsum[i-2] + arr[i], maxsum[i-1]) 

def maxSumNonAdjacent(arr):
	if not arr: return 0
	if len(arr) < 3: return max(arr)
	curr, prev = arr[0], max(arr[0], arr[1])
	maxVal = prev
	for i in range(2, len(arr)):
		curr, prev = prev, max(curr + arr[i], prev)
		maxVal = max(maxVal, prev)
	return maxVal


if __name__ == '__main__':
	arr = [1, 0, 3, 9, 2]
	print maxSumNonAdjacent(arr)