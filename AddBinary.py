"""
Given two binary strings, return their sum (also a binary string).
"""

def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    shorter = longer = None
    if len(a) < len(b):
        shorter, longer = a, b
    else:
        shorter, longer = b, a
    carry = 0
    result = collections.deque()
    for i in range(1, len(shorter)+1):
        _sum = int(shorter[-i]) + int(longer[-i]) + carry
        result.appendleft(str(_sum % 2))
        carry = _sum // 2
    for i in range(len(longer)-len(shorter)-1, -1, -1):
        _sum = int(longer[i]) + carry
        result.appendleft(str(_sum % 2))
        carry = _sum //2
    if carry: result.appendleft('1')
    return ''.join(result)