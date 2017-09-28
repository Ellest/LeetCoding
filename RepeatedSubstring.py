"""
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. 
You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
"""

# abcdabcdabcd

def repeated(word):
	if not word: return True
	pattern = [0 for _ in word]
	j = 0
	for i in range(1, len(word)):
		while j > 0 and word[j] != word[i]:
			j = pattern[j-1]
		if word[j] == word[i]: pattern[i] = j = j + 1
	prefix_length = len(word) - pattern[-1]
	return pattern[-1] != 0 and not len(word) % prefix_length