"""

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).
"""
def removeInvalidParentheses(self, s):
    """
    :type s: str
    :rtype: List[str]
    """
    def validate(state):
        cnt = 0
        for i in range(len(state)):
            if state[i] == '(':
                cnt += 1
            elif state[i] == ')':
                if not cnt: return False
                cnt -= 1
        return cnt == 0
        
    if validate(s): return [s]
    _map = set()
    queue = collections.deque([s]) # de queue 
    res = []
    while not res and queue: # result is empty or queue is empty
        for _ in range(len(queue)): # for all states in current lv
            state = queue.popleft()
            for i in range(len(state)):
                if state[i] in ('(', ')'): # if not parenthesis, ignore
                    nxt = state[:i] + state[i+1:] # take upto and after each char
                    if nxt not in _map: # check for containment
                        _map.add(nxt) # mark as processed
                        if validate(nxt): # found
                            res.append(nxt)
                        else:
                            queue.append(nxt)
    return res