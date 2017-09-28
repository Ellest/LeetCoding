"""

Given a string S and a string T, find the minimum window in S 
which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

"""

def minWindow(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    minLength, start = len(s) + 1, 0
    i = j = 0
    chars = collections.Counter(t)
    required = len(t)
    while j < len(s) or not required:
        if not required:
            if j - i < minLength: # check for new min
                minLength, start = j - i, i
            if s[i] in chars:
                chars[s[i]] += 1
                # only increment if our current window does not fulfill the requirements for this char
                if chars[s[i]] > 0: required += 1
            i += 1
        else:
            if s[j] in chars:
                chars[s[j]] -= 1
                # only decrement var if we the requirement for this char has not been fulfilled
                if chars[s[j]] >= 0: required -= 1
            j += 1
    return minLength <= len(s) and s[start:start+minLength] or ''