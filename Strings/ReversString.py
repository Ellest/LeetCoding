"""

Write a function that takes a string as input and returns the string reversed.
"""

def reverseString(s):
	reverse = [c for c in s]
	for i in range((len(s)+1)//2):
		swap = len(s)-1-i
		reverse[i], reverse[swap] = reverse[swap], reverse[i]
	return ''.join(reverse)