"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.
"""

def lengthOfLastWord(s):
	i = len(s)-1
    while i >= 0 and s[i] == ' ':
        i -= 1
    length = 0
    while i >= 0 and s[i] != ' ':
        length, i = length + 1, i - 1
    return length