"""
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""

def strStr(haystack, needle):
    if not needle: return 0
    pattern = [0 for c in needle]
    itr = 0
    # generate pattern array
    for i in range(1, len(needle)):
        while itr > 0 and needle[i] != needle[itr]:
            itr = pattern[itr-1]
        if needle[itr] == needle[i]: pattern[i] = itr = itr + 1
    
    # pattern matching
    itr = 0
    for i in range(len(haystack)):
        while itr > 0 and haystack[i] != needle[itr]:
            itr = pattern[itr-1]
        if needle[itr] == haystack[i]: itr += 1
        if itr == len(pattern): return i - len(pattern) + 1
    return -1


