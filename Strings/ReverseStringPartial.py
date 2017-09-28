"""
Given a string and an integer k, you need to reverse the first k characters for every 2k 
characters counting from the start of the string. If there are less than k characters left, 
reverse all of them. If there are less than 2k but greater than or equal to k characters, 
then reverse the first k characters and left the other as original.
"""

def reverse_string_k(str, k):
	reverse = [c for c in str]
	pivot = 0
	step = 2 * k
	while pivot < len(str):
		i, j = pivot, min(pivot + k, len(str)) - 1
		while i < j:
			reverse[i], reverse[j] = reverse[j], reverse[i]
			i, j =  i + 1, j - 1
		pivot += step
	return ''.join(reverse)
