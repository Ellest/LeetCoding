def scrambled(scr, ori, memo):
    pair = (scr, ori)
    if pair in memo: 
        return memo[pair]
    if len(scr) <= 2: 
        return sorted(scr) == sorted(ori)
    if sorted(scr) != sorted(ori): # if char counts do not match up
        return False
    memo[pair] = False
    for i in range(1, len(scr)):
        sPre, sSuf = scr[:i], scr[i:]
        if (scrambled(sPre, ori[:i], memo) and scrambled(sSuf, ori[i:], memo)) \
            or (scrambled(sPre, ori[-i:], memo) and scrambled(sSuf, ori[:-i], memo)):
            memo[pair] = True
            break
    return memo[pair]

def isScramble(self, s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    return scrambled(s2, s1, {})