"""
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

"""

def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    row = [False for c in range(len(p)+1)]
    row[0] = True
    for i in range(1, len(row)):
        if p[i-1] != '*': break
        row[i] = True
    for r in range(1, len(s)+1):
        prev, row[0] = row[0], False
        for c in range(1, len(row)):
            val = False
            if p[c-1] in (s[r-1], '?'):
                val = prev
            elif p[c-1] == '*':
                val = row[c] or row[c-1]
            prev, row[c] = row[c], val
    return row[-1]
