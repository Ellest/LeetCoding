"""
Given an absolute path for a file (Unix-style), simplify it.
"""

def simplifyPath(path):
    """
    :type path: str
    :rtype: str
    """
    stack = []
    for dir in path.split('/'):
        if dir == '..':
            if stack: stack.pop()
        elif dir and dir != '.':
            stack.append(dir)
    return '/' + '/'.join(stack)