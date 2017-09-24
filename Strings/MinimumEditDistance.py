"""
Given two words word1 and word2, find the minimum number of 
steps required to convert word1 to word2. (each operation is 
counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
"""


def minDistance(self, word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    if not word1: return len(word2)
    if not word2: return len(word1)
    row = range(len(word1)+1)
    for r in range(1, len(word2)+1):
        prev, row[0] = row[0], r
        for c in range(1, len(word1)+1):
            if word2[r-1] == word1[c-1]:
                prev, row[c] = row[c], prev
            else:
                prev, row[c] = row[c], min(row[c-1], row[c], prev) + 1
    return row[-1]


# For a shorter version

def minDistance(self, word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    if not word1: return len(word2)
    if not word2: return len(word1)
    row = range(len(word1)+1)
    for r in range(1, len(word2)+1):
        prev, row[0] = row[0], r
        for c in range(1, len(word1)+1):
        	v = min(row[c-1], row[c], prev) + 1 if word2[r-1] != word1[c-1] else prev
            prev, row[c] = row[c], v
    return row[-1]