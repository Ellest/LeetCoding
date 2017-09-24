"""
Given a non-negative integer num represented as a string, 
remove k digits from the number so that the new number is 
the smallest possible.
"""

def removeKdigits(num, k):
    """
    :type num: str
    :type k: int
    :rtype: str
    """
    if k < 1 or not num: return num
    stack = []
    i = 0
    while i < len(num) and k > 0: 
        v = int(num[i])
        if not stack or stack[-1] <= v:
            stack.append(v)
            i += 1
        else:
            stack.pop()
            k -= 1
    if k > 0: 
        stack = stack[:-k]
    else:
        stack.extend(int(c) for c in num[i:])
    return str(int(''.join(str(i) for i in stack))) if stack else '0'
