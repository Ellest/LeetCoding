"""
Given a string S, you are allowed to convert it to a palindrome 
by adding characters in front of it. Find and return the shortest 
palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".
"""

def shortestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """        
    if len(s) < 2: return s
    
    # Adding a $ sentinel to the middle to force restart for reversed half
    process = s + '$' + s[::-1]
    pattern_array = [0 for c in process]
    j = 0
 	# KMP pattern generation
    for i in range(1, len(process)):
        while j > 0 and process[j] != process[i]:
            j = pattern_array[j-1]
        if process[j] == process[i]: 
            pattern_array[i] = j = j + 1
    longestPalindrome = pattern_array[-1] # length of longest palindrom starting from beginning
    return len(s) == longestPalindrome and s or s[longestPalindrome - len(s):][::-1] + s