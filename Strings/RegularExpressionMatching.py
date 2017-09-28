"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

"""

def isMatch(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """          
    if not p: return len(s) == 0
    if p[0] == '*': return False
    row = [False for _ in range(len(p)+1)]
    row[0] = True
    for i in range(1, len(row)):
        if p[i-1] == '*':
            row[i] = row[i-2]
    for r in range(1, len(s)+1):
        row[0], prev = False, row[0]
        for c in range(1, len(row)):
            v = None
            if p[c-1] == s[r-1] or p[c-1] == '.': # if match
                v = prev
            elif p[c-1] == '*':
                # row[c-2] -> None of preceding element
                # latter -> one or more of preceding element check if current char is == to the
                #           preceding element and the pattern matched up to the previous char
                v = row[c-2] or ((p[c-2] == s[r-1] or p[c-2] == '.') and row[c])
            else:
                v = False
            row[c], prev = v, row[c]
    return row[-1]