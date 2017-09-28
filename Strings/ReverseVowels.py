"""
Write a function that takes a string as input and reverse only the vowels of a string.
"""

def reverseVowels(s):
    vowels = set('aeiou')
    i, j = 0, len(s)-1
    return_string = [c for c in s]
    while i < j:
        if s[i].lower() not in vowels:
            i += 1
        elif s[j].lower() not in vowels:
            j -= 1
        else:
            return_string[i], return_string[j] = return_string[j], return_string[i] 
            i, j = i + 1, j - 1
    return ''.join(return_string)