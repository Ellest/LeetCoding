"""
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting 
some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
(ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.

"""

def numDistinct(self, s, t):
"""
:type s: str
:type t: str
:rtype: int
"""

    row = [1 for _ in range(len(s)+1)]
    for r in range(1, len(t)+1):
        prev, row[0] = row[0], 0
        for c in range(1, len(row)):
            val = row[c-1]
            if s[c-1] == t[r-1]: val += prev
            prev, row[c] = row[c], val
    return row[-1]

def numDistinct_more_concise(self, s, t):

    row = [1 for _ in range(len(s)+1)]
    for r in range(1, len(t)+1):
        prev, row[0] = row[0], 0
        for c in range(1, len(row)):
            prev, row[c] = row[c], row[c-1] + prev * (s[c-1] == t[r-1])
    return row[-1]