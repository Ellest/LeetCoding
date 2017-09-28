"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

def validParentheses(s):
	parentheses = set('([{')
	closing = {'}' : '{', ']' : '[', ')' : '('}
	stack = []
	for c in s:
		if c in parentheses:
			stack.append(c)
		elif c in closing:
			if not stack or stack[-1] != closing[c]: return False
			stack.pop()
	return len(stack) == 0
