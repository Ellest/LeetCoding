
"""
Input array sorted. Subarray of value <= k
"""
def lessSubarrayMedian(arr, k):
	if not arr or arr[0] > k: 
		return None
	end = len(arr)
	if arr[-1] > k:
		i, j = 0, len(arr)-1
		while i <= j:
			m = i + (j-i) // 2
			if arr[m] <= k:
				i = m + 1
			else:
				j = m - 1
		end = i
	mid = end // 2
	if end % 2: # odd
		return arr[mid]
	else:
		return (arr[mid] + arr[mid-1]) / 2.0

def greaterSubarrayMedian(arr, k):
	if not arr or arr[-1] < k:
		return None
	start = 0
	if arr[0] < k:
		i, j = 0, len(arr)-1
		while i <= j:
			m = i + (j-i) // 2
			if arr[m] >= k: 
				j = m - 1
			else:
				i = m + 1
		start = i
	length = len(arr) - start
	mid = (len(arr) + start) // 2
	if length % 2: # odd
		return arr[mid]
	else:
		return (arr[mid] + arr[mid-1]) / 2.0

if __name__ == '__main__':
	arr = [1,2,3,6,7,8,8,8,8,9,10,10,10,13]
	#print(lessSubarrayMedian(arr, 14))
	print(greaterSubarrayMedian(arr, 0))