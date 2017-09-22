"""
Write a function to find the longest common prefix string amongst an array of strings.

"""

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
	if not strs: return ''
	shortest = min(strs, key = lambda x: len(x))
	index = len(shortest)
	for s in strs:
		i = 0
		while i < index and s[i] == shortest[i]:
			i += 1
		index = min(index, i)
	return shortest[:index]