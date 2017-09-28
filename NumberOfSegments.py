"""
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.
"""

def numberOfSegments(s):
	cnt = 0
	for i in range(len(s)):
		if s[i] != ' ' and (i == 0 or s[i-1] == ' '):
			cnt += 1
	return cnt

def numberOfSegments_pythonic(s):
	return sum(s[i] != ' ' and (i == 0 or s[i-1] == ' ') for i in range(len(s)))