"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
"""

def detectCapital(word):
	if not word: return True
	capitals = 0
	for c in word:
		captials += c.isUpper()
	return captials == len(word) or not capitals or captials == 1 and word[0].isUpper
	