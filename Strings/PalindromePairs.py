"""
Given a list of unique words, find all pairs of distinct indices (i, j) 
in the given list, so that the concatenation of the two words, 

i.e. words[i] + words[j] is a palindrome.

"""

def isPalindrome(word):
    i, j = 0, len(word)-1
    while i < j:
        if word[i] != word[j]: return False
        i, j = i + 1, j - 1
    return True

def palindromePairs(words):
    """
    :type words: List[str]
    :rtype: List[List[int]]
    """
    # generate a map with each word mirrored as the key
    mirrorMap = {w[::-1]:i for i,w in enumerate(words)}
    result_set = []
    for i, word in enumerate(words):
        if word:
            # take care of blanks separately to avoid double counting
            if '' in mirrorMap and isPalindrome(word):
                result_set.append([mirrorMap[''], i])
            for j in range(len(word)):
                pre, suf = word[:j], word[j:] # generating substring partition by index j
                # if there is a mirror of suffix and prefix is a palindrome
                # * exclude when mirror is it self (this will be when entire string is a palindrome)
                if suf in mirrorMap and mirrorMap[suf] != i and isPalindrome(pre):
                    result_set.append([mirrorMap[suf], i])
                # if there is a mirror of prefix and suffix is a palindrome
                if pre in mirrorMap and isPalindrome(suf):
                    result_set.append([i, mirrorMap[pre]])
    return result_set