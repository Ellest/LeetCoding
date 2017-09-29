"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""

def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) < 2: return 0 
    validEndPoints = {}
    stack = []
    maxLength = 0
    for i,c in enumerate(s):
        if not stack or c == '(':
            stack.append(i)
        elif s[stack[-1]] == '(':
            start = stack.pop()
            while start and start-1 in validEndPoints:
                start = validEndPoints[start-1]
            validEndPoints[i] = start
            maxLength = max(maxLength, i-start+1)
    return maxLength